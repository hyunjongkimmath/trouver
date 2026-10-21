# VaultNote cache — where the performance speedups are (discussion notes, 2026-10-19)

**Status 2026-10-20: COMPLETE.** Every ranked task shipped or closed:
`md_files_in_dir` os.walk rewrite; fix #2 `_stale` guard (`1aeb608`);
fix #3 rename pre-check (`c9d0019`); fix #4 `to_regex` bracket exclusion
(`67a2197`); §2.2 step-1 audit + step-2 hot-spot threading (`8ecee8a`);
item-2 hygiene sweep closed as moot (see the CLOSED note in the fix #2
section). Only optional future work: Phase B threading (glossary/ml_50,
per the step-1 audit's ranking) and having batch drivers actually pass a
prebuilt map. The "Ranked speedup tasks" / "Suggested order" sections
below are kept as the original plan — read the *Implemented* sections
for outcomes.

Synthesis of `Python/trouver/audit/findings_factoring_perf_2026-10-19.md` (§2.2, §2.3)
plus a read of the actual cache machinery (`03_obsidian_07.vault_cache.ipynb`,
`03_obsidian_08.vault_path.ipynb`, `03_obsidian_10.vault_file_crud.ipynb`).

## Framing: clearing is already free

- `clear_cache()` is `cls.cache = {}` — O(1), nothing to gain there.
- The cost people feel is the **rebuild that follows a clear** (or a name-miss):
  `update_cache(vault)` → `all_paths_to_notes_in_vault` → `md_files_in_dir`,
  a full directory walk over the vault, O(#files).

## Ranked speedup tasks

### 1. Merge the two full-vault traversals (audit §2.2) — biggest structural win
A typical run walks the vault twice:
- cache build: one full directory walk for name→paths;
- `all_links_in_vault` (`03_obsidian_70.vault_and_links.ipynb:158`): a second full
  pass that *reads every file* for links.

Fix: build the link map once per run and thread it as a parameter (the codebase
already threads shared state this way — `note_data`, `cache` dicts in
`sieve_potential_relied_notes`). Collapses 2–4 passes into one.

### 2. Stop triggering redundant lazy full rebuilds
Any name-lookup miss calls `identify_rel_path(update_cache=True)` → full O(vault) walk.
Concrete instances:
- `03_obsidian_10.vault_file_crud.ipynb:183` — the delete path does
  `self.exists(update_cache=True)`, which can force a **complete** cache rebuild just to
  confirm existence, and *then* calls `_remove_single_entry_to_cache` (single-entry).
  Checking existence by path is cheap; the full rebuild is wasted.
- Any sequence of name-based lookups after `clear_cache()` pays a full walk on the
  first lookup. CRUD already uses incremental `_add/_remove_single_entry_to_cache`
  (create @ line 97, delete @ line 185) — remaining task: audit `clear_cache()` call
  sites and replace "clear + lazy rebuild" with targeted single-entry updates where
  the change is known.

### 3. `VaultNote.rename` pre-check (audit §2.3) — biggest cache-*consuming* win
Rename is O(vault) by nature: walks the whole `cache[str(vault)]`, reads every note,
runs **three full-text regex passes per note** (`03_obsidian_10.vault_file_crud.ipynb`,
cell `8830213c`). Fix: `if self.name not in original_text: continue` after the read —
skips all three regex passes for the ~95% of notes that don't mention the renamed note.
Also drop the redundant `file.close()` (the `with` block already closes).

## Not worth doing
- §2.4 `substring_generator` deletion is a correctness/maintenance win, not a cache speedup.
- The walk itself is already a single pass and the cache stores only paths (never
  contents) — cold-build cost is irreducibly O(#files); every gain comes from *not
  rebuilding repeatedly* and *not traversing twice*.

## Suggested order
§2.2 link-map threading → `exists(update_cache=True)` fix in delete → §2.3 rename
pre-check. First two are small/localized; the rename fix is one line plus a test.

## Grep-by-name vs cache — measured (2026-10-19)

Question: replace the cache with glob-by-name (`all_note_paths_by_name`, i.e.
`vault.glob('**/name.md')`), or use grep on cache-miss instead of the full
rebuild? Bench: `_tmp/bench_grep_vs_cache_tmp.py` (median of 5, this machine,
notes spread over 30 nested dirs).

| vault size | rebuild (glob+dict) | rebuild via `os.scandir` | grep hit | grep miss | warm dict lookup |
|---|---|---|---|---|---|
| 200    | 0.0045s | 0.0025s | 0.0024s | 0.0025s | 0.20µs |
| 2 000  | 0.0311s | 0.0189s | 0.0093s | 0.0090s | 0.20µs |
| 10 000 | 0.1330s | 0.0828s | 0.0269s | 0.0280s | 0.20µs |

Re-bench of the same script **after the os.walk rewrite shipped** (2026-10-20;
`rebuild` row now measures the new `md_files_in_dir`, other rows unchanged):

| vault size | rebuild (os.walk, new) | rebuild via `os.scandir` (bench's manual stack) | grep hit | grep miss | warm dict lookup |
|---|---|---|---|---|---|
| 200    | 0.0017s | 0.0025s | 0.0026s | 0.0023s | 0.20µs |
| 2 000  | 0.0060s | 0.0222s | 0.0105s | 0.0095s | 0.20µs |
| 10 000 | 0.0249s | 0.0867s | 0.0318s | 0.0314s | 0.20µs |

The shipped rewrite beats the hand-rolled stack walk too (per-directory
`relpath`, and `os.walk`'s C-level `scandir` iteration). Rebuild is now
*faster than a single grep* at every size — which moots the "grep on miss"
proposal's premise (its break-even assumed rebuild ≈ 5× grep; it is now ≈ 1×):
any miss count ≥ 1 favors just rebuilding. See *Implemented* below.

Why grep ≈ rebuild/5 at scale: both pay the same directory walk, but the
rebuild additionally calls `relpath` on every file and inserts every name into
the dict; a targeted glob rejects ~all names at the fnmatch stage for free.

**Verdicts:**
- *Grep instead of cache* — **no.** Per lookup: 27ms (grep) vs 0.2µs (warm
  dict), ~10⁵×. Any run doing more than a handful of `VaultNote(name=...)`
  constructions (all ML/linking workflows do thousands) loses catastrophically.
- *Grep on miss instead of full rebuild* — **yes for straggler misses, no for
  bulk staleness.** Break-even ≈ rebuild/grep ≈ **2–5 distinct missing names
  per session**: fewer → grep wins ~5×; more (vault moved/git-pulled) → one
  rebuild indexes them all. Insert the grep result into the cache so repeat
  lookups of a found name are O(1). Also softens the existing negative-lookup
  pathology (a nonexistent name with `update_cache=True` triggers a *full
  rebuild on every single lookup* — grep makes each such walk ~5× cheaper,
  though negatives still aren't memoized).
  **CORRECTED by the post-os.walk re-bench above and CLOSED 2026-10-20:**
  with rebuild ≈ 1× grep at every size, even one miss favors a plain
  rebuild — final verdict for grep-on-miss is **no**, nothing to implement.
  (The negative-lookup pathology it worried about was separately killed by
  the fix #2 `_stale` guard: misses on a fresh cache no longer walk at all.)
- *Semantic caveat:* on Windows `glob` is case-insensitive (`note.md` matches
  `Note.MD`) while the cache dict is case-sensitive — grep-on-miss would find
  notes the current code reports as not-found. Probably desirable (matches
  Obsidian's link resolution) but it is a behavior change; decide explicitly.

**Bonus finding (independent of the above):** rebuilding with a manual
`os.scandir` walk instead of `Path.glob('**/*.md') + relpath + dict` is
**1.6× faster at every size** (133→83ms @ 10k). Free cold-start win regardless
of miss strategy — worth a ranked task of its own.

## Implemented: os.walk rewrite of `md_files_in_dir` (2026-10-20)

Task from the bonus finding, done via test-net-first (testing.md rule 6):
characterization cells added to `01_helper_03.files_and_folders.ipynb` and run
green against the *old* code first; then the rewrite swapped in.

Implementation: `os.walk` loop (stdlib iterator — itself `scandir`-based),
relative paths assembled per-directory (no per-file `relpath`), names via a
single `splitext(basename)` pass, guard-clause filter. Depth 3, 16 exec lines;
passed through the checker's new snippet gate before cell insert.

Re-bench (`bench_grep_vs_cache_tmp.py`, median of 5): rebuild @ 10k files
**0.133s → 0.0249s (5.3×)** — better than the hand-rolled scandir bench,
which paid `relpath` per file. The spec-conformant flat shape was also the
fast shape.

Direct old-vs-new comparison (`bench_old_vs_new_md_files_tmp.py`: pre-rewrite
body verbatim vs shipped function, same process, identical trees, median of 5,
outputs asserted equal modulo walk order):

| vault | list mode | dict mode (what the cache uses) |
|---|---|---|
| 200 nested      | 5.8 → 2.9ms (2.0×)   | 6.3 → 2.7ms (2.4×) |
| 2 000 nested    | 24 → 7.0ms (3.4×)    | 31 → 6.6ms (4.7×) |
| 10 000 nested   | 105 → 24ms (4.3×)    | 121 → 25ms (4.8×) |
| 10 000 flat     | 93 → 20ms (4.7×)     | 111 → 17ms (6.4×) |

Reading: the multiplier *grows with n* because every saving is per-file (Path
object + regex fnmatch + `relpath` normalization + two name computations →
`endswith` + one `splitext` on the bare basename + append); dict mode gains
most because the old code computed every name twice (key-prebuild pass +
append pass) vs once via `setdefault`. Summary: ~2× at hundreds of notes,
~5× (to 6.4×) dict-mode at 10k. Absolute ms are this machine with warm OS
cache; the ratios are the stable result.

One intentional behavior change (pinned first, then flipped with an in-cell
note): directories named `*.md` are no longer reported — old `glob` had no
file-only filter, but dirs are not notes and must not enter the name→paths
cache. Everything else is exact parity (duplicate-name grouping, `.md`-stem
edge via splitext, dir≠root prefixing, empty-dir boundary).

~~Still open from the ranked list: §2.2 link-map threading, delete-path
`exists(update_cache=True)` fix, §2.3 rename pre-check, grep-on-miss
decision.~~ — all closed later on 2026-10-20; see the sections below.

Official harness record (`bench_vault_cache.py`, median of 3, flat vault):

| target | 2 000 | 10 000 | reading |
|---|---|---|---|
| rebuild      | 0.0034s | 0.0156s | new `md_files_in_dir` walk |
| link_pass    | 0.1084s | 0.5929s | full read pass (audit §2.2) |
| delete       | 0.0033s | 0.0166s | ≈ rebuild → dominated by the lazy rebuild the `exists(update_cache=True)` fix removes |
| rename       | 0.2365s | 1.1076s | §2.3 pre-check target — biggest single number here |
| link_reads   | 0.1741s | 0.8533s | no map (read per call) |
| link_thread  | 0.1375s | 0.6771s | prebuilt `link_map` — note: the `link_map=` param already exists; §2.2 status needs a fresh audit, this doc may be stale on it → **audited + threaded same day**, see step-1/step-2 sections below |

## Implemented: `_stale` staleness guard (fix #2, 2026-10-20)

One bit per vault — `VaultNote._stale[vault]` = "cache mutated since the last
full walk". A miss with `update_cache=True` re-walks only while stale. Chosen
over an epoch/walked-at counter pair after review: single-threaded, so one
bool carries exactly the decision's information; no sentinel defaults to get
wrong. (Epoch design preserved in `_tmp/proposed_delete_exists_tmp.py`.)

Writers (the only ones — all cache mutations flow through these four):
- `update_cache` → False (walk just completed)
- `clear_cache` → `{}` (absent = never walked = stale)
- `_add_single_entry_to_cache` / `_remove_single_entry_from_cache` → True

Decision site: `identify_rel_path` — the single funnel used by the constructor,
`exists(update_cache=True)` (hence `delete`), `reference_directory`, and the ML
call sites. `exists` itself unchanged; `delete` got a cosmetic guard-clause form.

Walk counts pinned by characterization cells in `03_obsidian_07.vault_cache.ipynb`
(spy = `mock.patch.object(VaultNote, 'update_cache', wraps=...)`), pre-guard → post:
warm-existing delete 0→0; cold-existing 1→1 (irreducible); cold-nonexistent 2→1;
5-missing-name warm probe loop 10→0; post-mutation miss-loop 1 walk per burst.

Accepted staleness (test `char_5`): a file created out of band stays invisible
until a trouver mutation or explicit `VaultNote.update_cache(vault)`.

Fallout fixed: notebook 10 cell `2b31120e` mocked `all_paths_to_notes_in_vault`
then relied on name lookups re-walking; now identifies by `rel_path` instead.

Remaining from item 2 (separate follow-up): ~~audit `VaultNote(..., update_cache=True)`
re-constructions after `create()` in `08_ml_66/67/70`, `05_personal_vault_25:279`,
GUI — replace with `_add_single_entry_to_cache` where the path is known.~~
**CLOSED 2026-10-20 — nothing to sweep.** Call-site audit found (a) post-guard,
`update_cache=True` re-walks only *while stale* (`identify_rel_path`, nb 07), so
the ml_66/ml_67 entry-point calls are no-ops on a fresh cache and the GUI's is
both one-shot and staleness-gated; (b) the ml_70 `except NotePathIsNotIdentifiedError`
re-constructions know only the name, not the path — `_add_single_entry_to_cache`
is inapplicable, and they already walk only on miss+stale; (c) `05_personal_vault_25`
cell 12 is an intentional test-fixture warm-up on a fresh temp vault. No edits made.

Harness (10k notes, post-guard): new `probe_missing` target = 0.0173s — one
walk is the explicit warm-up rebuild inside the timed call; the 5 missing-name
probes add ~0 (pre-guard they would have added ~10 walks ≈ 0.16s). Spy-based
notebook tests remain the authoritative walk-count evidence (10 → 0).

## Implemented: rename substring pre-check (fix #3, 2026-10-20)

`rename` swept every note in the vault with **three regex replacement passes**
per note. All three `ObsidianLink` patterns embed `old_name` as a *literal*
substring of what they can match — so a note whose text does not contain
`old_name` cannot reference the renamed note and needs no passes at all. The
read-all pass is the irreducible floor (references can be anywhere); only the
regex work was waste.

Changes (`03_obsidian_10.vault_file_crud.ipynb`, cell `8830213c`):
- `old_name = self.name` captured **before** `move_to` (which rebinds
  `self.name` to the new name — the old code built its patterns before the
  move for exactly this reason).
- New exported helper `_replace_links_all_styles(text, old_name, new_name)`
  holds the three-pass pattern list; `rename` calls it only when
  `old_name in original_text`.
- Dropped the redundant `file.close()` inside the `with open(...)` block.
- Shape: was exec=24/depth=4 (R1+R3 flagged); now both functions clean, and
  `check_function_shape.py nbs` no longer flags rename.

Test added (cell `f3x9nearms`, notebook 10): a bystander note containing only
NEAR MISSES (`renamex`, `"rename me"`, `renamexe`) is left byte-identical by
the pre-check; a referrer containing the literal old name still gets all three
styles rewritten (alias wikilink, embed, markdown `.md` link).

Incidental finding (pre-existing, NOT fixed): `replace_links_in_text` mangles
text when several link styles share ONE line — e.g.
`[[x|a]] ![[x]] [y](x.md)` after the 2nd pass collapses to a single broken
link. One style per line is fine (matches the existing fixture's convention);
the test keeps one style per line and comments this. Worth its own audit item.

Measured (`bench_vault_cache.py`, 10k notes, median of 3):
rename 1.2897s → 0.7898s (~1.63×). Floor reference: `link_pass` (pure
read-all) = 0.59s; the remaining ~0.2s is per-note `VaultNote(...)` +
`exists()` + `text()` construction, same as any full-vault sweep.

## Implemented: to_regex markdown wildcard bracket exclusion (fix #4, 2026-10-20)

The incidental finding above, fixed. `ObsidianLink.to_regex()` built the
MARKDOWN pattern's display-text wildcard as `(.*?)?` — brackets allowed, and
Python `re` is leftmost-first: on a line with an earlier `[`, one
`[...](old.md)` match could START at a wikilink's bracket and swallow every
preceding link; `replace_links_in_text` then rebuilt the whole span as one
link (dropping embeds, grafting `.md` onto the wrong target).

Fix (`03_obsidian_50.links.ipynb`, `to_regex`): wildcard -> `([^\[\]]*?)?`.
Display text may not contain brackets, so a markdown-link match can no
longer start inside an earlier link. One-line semantic change; all caller
notebooks (10/50/60/70 + `05_personal_vault_05`, `08_ml_50`) green.

Test: characterization cell at the end of notebook 50 (rule 6 — pinned the
corrupted output against old code first, then flipped): each style alone and
one-style-per-line regression guards, plus the mixed-styles-one-line case
now rewritten correctly. Notebook 10's rename test additionally pins that a
link to a LONGER name (`[[renamednow_but_different]]`) passes the substring
pre-check but is NOT rewritten by the regexes (false-positive safety).

Note: `to_regex` remains R1-flagged (exec=33) — pre-existing, unrelated.

## §2.2 step-1 audit: link_map call sites (2026-10-20)

Premise update first: the doc's original "merge cache-walk + link-pass" is
moot — post-os.walk the walk is 0.025s vs the 0.59s read pass (~4%). The
win is **map reuse across repeated overlapping queries**. `link_map=`
already exists on `notes_linked_in_note` / `notes_linked_in_notes_linked_in_note`
(nb `05_personal_vault_10`, with docstring + examples) — but the ONLY
callers passing it are its own example cells. Full dump:
`_tmp/link_map_audit_tmp.txt`. Ranked by query volume per pipeline run:

| site | reads per call | calls per run | verdict |
|---|---|---|---|
| `08_ml_67 sieve_potential_relied_notes` | full 2-hop fan-out of the reference index (`notes_linked_in_notes_linked_in_note`) | **once per origin note** → same neighborhood re-read n times: quadratic | thread — biggest win |
| `08_ml_70 _get_preceding_info_notes_in_section` | section-index links | once per info note in the section → same index re-read per note: quadratic within a section | thread |
| `08_ml_70 notat_linking_data_from_notation_notes`, `_info_notes_for_reference` | 2-hop fan-out per reference | once per reference (or fewer) | thread (cheap once map exists) |
| `06_notation_15 glossary _resolve_info_notes_for_index` | direct + two-hop fan-out | once per index note; indices overlap in two-hop sets | thread — moderate |
| `08_ml_50 note_data_from_reference` | index + each section index | once per reference; mostly disjoint reads | marginal |
| `05_personal_vault_15 _files_in_reference_folder_via_index_notes`, `05_pv_20 _note_not_in_index_note` | 1 + small fan-out | interactive/lookup volume | skip |
| GUI (`09_app_00_gui` cells 35/42), ml_10 test cells | single actions / tiny vaults | — | skip |

Break-even math: map build = one full read pass (0.59s @10k); direct reads
≈ 0.85s·(k/n) for k queries over n notes → threading pays from ~70% of
notes queried, and pays *quadratically-to-linearly* where the same fan-out
is re-read per origin note (the two ml_70/67 rows).

Staleness decision: pipelines are read-only during data gathering; build
the map at phase start, document rebuild-after-mutation at the driver
level. (The threaded map has no `_stale`-style auto-invalidation — by
design, it is a snapshot.)

Proposed scope: Phase A = ml_67 sieve + ml_70 notation-linking threading
(optional `link_map=` params built once per run/driver; default None keeps
current behavior). Phase B = glossary (+ maybe note_data_from_reference).
Skip GUI/reference/GUI-adjacent sites.


## Implemented: link_map threading of the two hot spots (§2.2 step 2)

Both functions gained an optional `link_map` parameter (default `None` =
existing behavior, passed straight to `notes_linked_in_note*`). Batch
callers can now build one map per vault once and reuse it; single-shot
callers keep the cheap direct-read path.

- `sieve_potential_relied_notes` (`08_machine_learning_67`, cell
  `e5eb6fa6`): forwards to its two-hop lookup. Set-based consumer, so the
  default deduplicated map from `all_links_in_vault(vault)` is fine.
- `_get_preceding_info_notes_in_section` (`08_machine_learning_70`):
  forwards to its one-hop lookup. **Order-dependent** (walks links until
  the target name), so its comment requires a map built with
  `all_links_in_vault(vault, multiplicities=True)` — the default dedupes
  and loses text order.

Tests (equivalence-first, per the additive-parameter discipline):
- ml_67 new cell after `0b584fb5`: (1) forwarding — mock asserts the map
  reaches `notes_linked_in_notes_linked_in_note`; (2) real temp-vault
  equivalence — sieve result identical with and without the map.
- ml_70 new cell after the def cell: temp vault whose section index links
  `[[a]] [[b]] [[a]] [[c]]` (duplicate pins text-order-with-duplicates);
  ordered results identical with a `multiplicities=True` map, plus the
  target-first empty case.

Not done (out of approved scope): Phase B threading (glossary, ml_50) and
updating internal single-shot callers to build maps (a full-vault map costs
~0.6s at 10k notes — only worth it when many queries follow).

Both notebooks green (`nbdev test`); export diff contains exactly the two
threading edits (plus cosmetic header-hash churn in the id-less ml_70
notebook, same as fix #4's links.py).
