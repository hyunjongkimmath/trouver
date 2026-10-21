# Factoring & Performance Audit — `trouver\nbs`

**Purpose:** exact factor-out and performance changes across the 101 notebooks. Each item states the current excerpt, the change, and why.

**Method:** scanner `_nbdev_development/spec_checkers/check_dupes_perf.py` (full report: re-run it); every Tier A item below verified by reading both copies.

---

## 1. Factor-out candidates

### A1 ~~`helper.packages` is exported by TWO notebooks (nbdev module collision)~~ ✅ RESOLVED 2026-10-21

`star.ipynb` deleted outright after diffing: its four export cells matched
`01_helper_10.packages.ipynb` except star's copy had *lost* the type hints on
`check_package_version_with_version_attribute` — and because `s` sorts after
`0`, star was winning every full export, so the generated module had carried
the untyped copy since 2024. Provenance: born in the same 2024-12 GUI commit as
the real notebook; a scratch sandbox (copied frontmatter, abandoned half-typed
cell) never edited again. Post-delete export: `packages.py` parent is now
`01_helper_10.packages.ipynb`, typed signature restored, `_modidx.py` doc links
moved off `star.html`; notebook test green. Sole exporter =
`01_helper_10.packages.ipynb`.

### A2 ~~`is_number` duplicated verbatim~~ ✅ RESOLVED 2026-10-21

> Shipped in 08b780c: def deleted from `04_latex_15.formatting`, which now
> imports `is_number` from `trouver.helper.numbers` (its assert suite stays
> there). No consumer imported it from `latex.formatting`; notebook tests green.


**Current:** identical body in `01_helper_09.numbers.ipynb:58` and `04_latex_15.formatting.ipynb:82`:

```python
def is_number(x: Union[float, int, complex, str]) -> bool:
    if isinstance(x, (float, int, complex)):
        return True
    if x is None:
        return False
    if x and x[0] == '-': x = x[1:]
    return x.replace(".", "1", 1).isdigit()
```

**Change:** delete the def in `04_latex_15.formatting`; add `from trouver.helper.numbers import is_number` to its import cell (first confirm no *other* notebook imports it from `trouver.latex.formatting`).

**Why:** one tested copy (`helper_09` has the assert suite) instead of two that can drift; the `x.replace(".", "1", 1).isdigit()` trick is subtle enough that a second copy invites divergence.

### A3 ~~`create_method` lambda factory ×3~~ ✅ RESOLVED 2026-10-21

> Shipped in 08b780c: `01_helper_28.latex.augment` already exported an
> identical `_create_method`, and all three ML notebooks already imported
> from that module — so the nested defs were deleted and `_create_method`
> appended to each existing import. Tests green.


**Current:** identical in `08_ml_15.tokenize…classification`, `08_ml_25.notation_summarization`, `08_ml_35.definition_and_notation_naming`:

```python
def create_method(method, p, scale):
    return lambda x: method(x, p=p*scale)
```

**Change:** define once in `01_helper_28.latex.augment` (home of `augment_text`, which these all call); the three ML notebooks import it.

**Why:** it's the closure factory for the augmentation pipeline; if the `p=p*scale` scaling rule changes, three copies must change in lockstep.

### A4 ~~markdown-link extractors duplicated between `note_data` and `notation_linking`~~ ✅ RESOLVED 2026-10-21

> Shipped in 08b780c as proposed — signatures verified identical before the
> merge. `note_data`'s copies are now public (`linked_note_names_from_content`,
> `linked_notat_note_names_from_content`) with docstrings; `notation_linking`
> imports them and its two test cells moved to `note_data` (the mock-patch
> targets `'__main__.VaultNote'`/`'__main__.note_is_of_type'` only resolve
> where the names are looked up). No import cycle: nothing imported
> `notation_linking`. Tests green in both notebooks.


**Current:** identical in `08_ml_50.note_data.ipynb:1158` and `08_ml_70.notation_linking.ipynb`:

```python
def _linked_note_names_from_content(content: str) -> list[str]:
    linked_note_names = []
    for match in re.findall(MARKDOWNLINK_CAPTURE_PATTERN, content):
        link_name = match[1]
        if link_name.endswith('.md'):
            link_name = link_name[:-3]
        linked_note_names.append(link_name)
    return linked_note_names
# + _linked_notat_note_names_from_content (same shape)
```

**Change:** keep in `note_data`, drop the underscore (it becomes cross-module API), and in `notation_linking` replace both defs with:

```python
from trouver.machine_learning.note_data import (
    linked_note_names_from_content, linked_notat_note_names_from_content)
```

(`notation_linking` already imports from `trouver.machine_learning.*`, so this fits the existing pattern.)

**Why:** link-parsing is exactly the logic that changes when Obsidian's link syntax edge cases are discovered; two copies = two bug-fix sites.

### A5 ~~`make_example_vault` fixture builder ×2~~ ✅ RESOLVED 2026-10-21 (deviation)

> Shipped in 08b780c, going straight to the audit's longer-term home: the
> builder (+ its note-text constant) moved to `trouver.helper.tests` next to
> `_test_directory`, per `testing.md`. Deviation from "keep in
> `03_obsidian_40.file`": that notebook was mid-edit by another session, and
> its copy turned out to be unflagged anyway — never exported. So
> `obsidian_49` now imports from `helper.tests`, and **follow-up: switch
> `obsidian_40`'s private copy to the same import once that session's work
> lands.** Tests green in helper_01/obsidian_49.



**Current:** identical in `03_obsidian_40.file.ipynb` and `03_obsidian_49.file_write.ipynb:207`:

```python
def make_example_vault(temp_dir: PathLike):
    temp_dir = Path(temp_dir)
    os.mkdir(temp_dir / 'algebraic_geometry')
    os.mkdir(temp_dir / 'algebraic_geometry' / 'a1_homotopy_theory')
    # … nested tree + note files
```

**Change:** keep in `03_obsidian_40.file`; delete from `03_obsidian_49` (its import cell already has `from trouver.obsidian.file import …` — just add the name). Longer-term, per `testing.md` ("fixture data lives in `_tests/`"), move the builder next to `_test_directory` in `trouver.helper.tests`.

**Why:** test fixture that must stay in sync with what the tests assert about the tree shape.

### A6 — `MockTokenizer`/`MockPipeline` duplicated (test mocks, not production)

**Current:** identical mock classes in test cells of `08_ml_21.…_mark` and `08_ml_22.…_main_workflow`:

```python
class MockPipeline:
    """Mocks the TokenClassificationPipeline."""
    def __init__(self, preds):
        self.tokenizer = MockTokenizer()
        self._preds = preds
    def __call__(self, text):
        return self._preds
```

**Change:** move both mocks to `trouver.helper.tests` (already hosts `_test_directory`, imported by test cells across notebooks); import in ml_21/ml_22. Same treatment for `mock_note_data` (ml_60 vs ml_64, Tier B).

**Why:** (initial guess of a production-class split was wrong on verification — these are test doubles; the fix is shared test helpers, cheaper than A4.)

### Tier B — name collisions to eyeball (not verified as dupes)

| Name | Locations | Check |
|---|---|---|
| `from_note` | `03_obsidian_01.vault`, `08_ml_50.note_data` | same contract? import if so |
| `_split_text_by_html_data_parts` | `08_ml_15`, `08_ml_35` | private + same name in two ML nbs → likely copy |
| `make_tag` | `06_notation_10_management`, `06_notation_15.glossary` | compare bodies |
| `mock_note_data` | `08_ml_60.…sieve`, `08_ml_64.…augmentation` | → `helper.tests` with A6 |

Excluded false positive: `path`/`exists`/`create` in `08_ml_35` are a test mock class, not a reimplementation of `03_obsidian_08.vault_path`.

## 2. Performance opportunities

### 2.1 Fuzzy-similarity hot path (biggest runtime win) ✅ RESOLVED 2026-10-21 (parts 1+3 shipped; part 2 rejected)

> **Update 2026-10-21 (7da7ee0):** parts 1 and 3 shipped —
> `partial_ratio_with_alphabet` is now `@lru_cache(maxsize=4096)` (helper_02,
> cache-hit test added), and `similar_notat_notes_in_note` takes an optional
> precomputed `latex_texts` param which `sieve_potential_relied_notes` computes
> once per origin note and forwards to every call (ml_67; equivalence +
> forwarding tests). **Part 2 rejected as mathematically wrong:** partial ratio
> slides the shorter string over the longer, so a perfect window match scores
> 100 no matter how large the length gap (`\dim M` inside
> `X: M \rightarrow T M`) — an `abs(len diff)` cutoff drops true positives.
> The existing quadratic containment penalty in
> `latex_str_in_latex_str_fuzz_metric` already demotes one-sided matches.

**Current:** `01_helper_02.init.ipynb:371` — slides the shorter string over the longer, full Levenshtein DP per window:

```python
for i in range(len2 - len1 + 1):          # ~len2 windows
    substring = s2[i:i+len1]
    d = [[0] * (len1 + 1) for _ in range(2)]
    for j in range(1, len1 + 1):
        ...                                # O(len1^2) DP per window
```

Called per pair from `08_ml_67.note_linking_vault_operations.ipynb:81`:

```python
for notation_note in notation_notes:              # every notation note
    notation = notation_in_note(notation_note, include_dollar_signs=False)
    for latex_text in latex_texts_in_origin_note:  # every $…$ snippet in origin
        if latex_str_is_likely_in_latex_str(notation, latex_text, threshold=threshold):
```

and `latex_texts_in_origin_note` is re-derived (`origin_note.text()` + `latex_indices`) on **every call** — `sieve_potential_relied_notes` calls this across many origin notes.

**Change (three parts):**
1. ✅ `@lru_cache(maxsize=4096)` on `partial_ratio_with_alphabet` — done 2026-10-21.
2. ~~Length pre-filter before the metric in `similar_notat_notes_in_note`: skip a pair when `abs(len(notation) - len(latex_text)) > max_len` (partial ratio can't exceed threshold if lengths differ too much).~~ **REJECTED 2026-10-21** — premise false, see update note above.
3. ✅ Hoist latex extraction — done 2026-10-21 as an optional `latex_texts` param on `similar_notat_notes_in_note`, forwarded by `sieve_potential_relied_notes` (per-origin-note, not a global map — the sieve only ever parses its current origin note).

**Why:** vault-wide cost is O(#origin notes × #notation notes × #snippets × DP) with zero caching anywhere in the codebase (report §F: no `@lru_cache`/`@cache` in any of the 101 notebooks).

### 2.2 ~~Vault files re-read multiple times per run~~ ✅ RESOLVED 2026-10 (cache-perf cycle)

Shipped as proposed (minimal version): `notes_linked_in_note` and
`notes_linked_in_notes_linked_in_note` take an optional
`link_map: dict[str, list[str]] | None` param — callers holding an
`all_links_in_vault(vault)` result skip all note re-reads; threaded through both
levels, with tests comparing map-path vs read-path (`05_personal_vault_10.notes`).

### 2.3 ~~`VaultNote.rename` — wasted regex passes + redundant close~~ ✅ RESOLVED 2026-10 (cache-perf cycle)

All of it, in `03_obsidian_10.vault_file_crud`: substring guard
(`if old_name not in original_text: continue`) before any regex work; the three
`replace_links_in_text` calls consolidated into one `_replace_links_all_styles`
helper with an early skip when text is unchanged; stray `file.close()` dropped.

### 2.4 `substring_generator` — dead O(n²) trap

**Current:** `01_helper_02.init.ipynb:66`:

```python
def substring_generator(input_string: str):
    length = len(input_string)
    for i in range(length):
        for j in range(i + 1, length + 1):
            yield input_string[i:j]
```

Grep evidence: only `sublist_generator` (its sibling) is imported anywhere (`01_helper_21.latex`, `01_helper_27_latex.processing`); `substring_generator` has **zero** references.

**Change:** delete it (or drop `#| export` if it's kept for the generated API).

**Why:** an exported n²-substring generator invites exactly the misuse §2.1 warns about.

### 2.5 Semantic search re-ingestion (verify)

`08_ml_90.semantic_search`: `_get_all_paths` + `ingest_files` rescan the tree on every run. Candidate: path→mtime dict so unchanged files skip embedding. *Not yet read in detail — confirm before committing.*

## 3. Action order

1. ~~**A1** (module collision — correctness, not just tidiness)~~ — done 2026-10-21.
2. ~~**§2.1** caching + pre-filter (biggest runtime win, localized to `01_helper_02` + `08_ml_67`)~~ — parts 1+3 done 2026-10-21 (7da7ee0); part 2 (pre-filter) rejected, see §2.1 update.
3. ~~**A2–A5** pure import swaps (zero behavior change)~~ — done 2026-10-21 (08b780c; A5 went to `helper.tests`, see its deviation note).
4. ~~**§2.2/§2.3** link-map threading + rename micro-fixes~~ — done in the cache-perf cycle.
5. **A6 + Tier B** shared test helpers; delete `substring_generator` (§2.4).

## State — COMPLETE (all Tier A verified against source)

Re-verified 2026-10-21 against current notebooks: §2.2 and §2.3 resolved
(cache-perf cycle), A1 resolved (star.ipynb deleted); §2.1 closed 2026-10-21
(parts 1+3 shipped in 7da7ee0, part 2 rejected — see its update note);
A2–A5 closed 2026-10-21 (08b780c; A5 follow-up: obsidian_40's private
fixture copy still pending that session).
Remaining open: A6 + Tier B, §2.4, §2.5.

Re-run scanner: `python _nbdev_development/spec_checkers/check_dupes_perf.py Python/trouver/nbs > _tmp/_dupes_perf_report_tmp.txt`.
