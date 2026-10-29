# Findings: LaTeX divide/convert pipeline audit (2026-10-25)

Scope: `trouver.latex.divide` (numbering engine), `trouver.latex.convert` (label/ref
resolution, note creation), `trouver.latex.preamble`, `trouver.latex.folders`, plus the
corpus data side (`latex_full`). Motivating complaint: running the latex setup on
`C:\Users\hyunj\Documents\Obsidian\Chores\math\text_corpus\latex_image_data\latex_full`
yields "numberings not being correct". Line numbers cite the generated `trouver/latex/*.py`
as of 2026-10-25 (source of truth: the `nbs/04_latex_*` notebooks).

## 1. Correctness — why numbering comes out wrong on real documents

**N1 (main suspect): equation counter forced to reset per section.**
**Status: fixed 2026-10-25** — test net added first (cells `n1t1`–`n1t8` + example in
`04_latex_00.divide.ipynb`, real-doc fixtures under `_tests/latex_examples/`; three red,
guards green), then the default block removed and the two old pins flipped. Full-notebook
exec 0 failures; §6 repro re-run shows global numbering on synthetic + real files. The N10
hybrid on equation-sharing theorem envs survives this fix (pinned by `n1t7`). `n1t8`
(2026-10-25) extends the net to `kass_wickelgren_ekl`, the one corpus file with numbered
equations on both sides of its first `\section` (the reset-benefit case). Note: equation
counter values do not surface in `divide_latex_text` titles for this shape — `equation` is
in `DEFAULT_ENVIRONMENTS_TO_NOT_DIVIDE_ALONG`, so the pins are at hierarchy level.

`get_counter_hierarchy` (`divide.py:320-348`) ended with a hardcoded default:

```python
if 'equation' not in explicit_resets:
    hierarchy['equation'] = 'section'   # "Ensure equation climbs to section by default"
```

In standard LaTeX (`article`/`amsart`) `equation` is a **global** counter — no reset at
`\section`, numbers run `(1), (2), …` across the document. This line makes the pipeline
(a) reset equation numbering at every `\section` and (b) format numbers as
`section.equation` (`2.1` instead of `5`). It feeds both display formatting
(`get_formatted_number`) and reset logic (`get_reset_hierarchy` → `_recursive_reset`), so
every derived artifact inherits it. Real arXiv sources in `latex_full` use global
numbering, so this is the most likely cause of the reported errors.

Pinned by tests (deliberate at some point): `test_get_reset_hierarchy` case 2
("UPDATED EXPECTATION: section resets subsection AND the default equation") and the
`get_formatted_number('equation', …) == "1.2.5"` test in `04_latex_00.divide.ipynb`.
Fixing requires a test-net-first flip (spec rule 3).

**N2: `manual_envs` hack pollutes equation numbering.**
**Status: fixed 2026-10-26** — test net added first (cells `n2t1`–`n2t3` in
`04_latex_00.divide.ipynb`; `n2t1` unnumbered styled box red, `n2t2` custom
`\refstepcounter`/`\stepcounter` envs red, `n2t3` `\newtheorem`-wins guard green),
then the hack block + scaffolding comments removed and replaced by definition-based
mapping: new helpers `_braced_group_after` / `_newenvironment_counters` map a
`\newenvironment` to the counter its begin body steps (`\refstepcounter{X}`/
`\stepcounter{X}`); an explicit `\newtheorem` wins via `setdefault`. The existing
`test_manual_environment_mapping` stayed green unchanged (its remark definition does
contain `\refstepcounter{equation}`). Full-notebook exec 0 failing cells; full export clean.

`numbered_newtheorems_counters_in_preamble` (`divide.py:195-256`) maps any document that
uses `\begin{remark}`/`example`/`heuristic`/`warning` without a `\newtheorem` definition to
the **equation counter**. A plain styled-box environment (no `\refstepcounter`) then
increments and displays equation numbers — subsequent equations are off by one.
Data-dependent behavior in generic code, wrapped in `# --- ADD THIS LOGIC ---` scaffolding
comments plus a commented-out block. Pinned by `test_manual_environment_mapping`.

**N3 (data side): the corpus has broken labels.**
12 `latex_full` files contain empty/duplicate labels: `\label{remark:}` ×105,
`\label{equation:}` ×19, `\label{definition:}` ×14, plus literal `\label{#1}` from
unexpanded macros (e.g. `ellenberg_landesman_hsghssgqtfff/…tex` — 45 such labels alone,
lines 606/621/2150…). Even a correct compiler resolves `\ref{remark:}` to the *last*
duplicate — some "wrong numberings" in that corpus are unrecoverable without source
cleanup.

**N4 (design): `\ref` is never resolved to a number.**
`_add_links_to_refs` (`convert.py:363-381`) wraps refs as `[[note|\ref{label}]]` — the
display text stays the literal `\ref{…}`. No LaTeX compiler exists anywhere in the
project, so note bodies never show actual numbers; only part titles carry computed
counters. Undefined labels (defined in a missing `\input` file) are silently left as-is
with no warning.

**Other correctness bugs:**
- **N5** `divide_preamble` (`preamble.py:13-23`): `match.span()` with no `None` check —
  any file without `\begin{document}` (common among OCR'd sources) crashes with
  `AttributeError`.
  **Status: fixed 2026-10-27** — test-net-first: cell `n5t1` in
  `04_latex_10.preamble.ipynb` (`ExceptionExpected(ValueError, …)` on a `\section{…}`
  fragment; red under the old `AttributeError`, green after). The guard raises
  `ValueError("no \begin{document} found in `text` (e.g. an \input fragment without a
  document environment)")`. Full-notebook exec 0 failing cells; full export clean.
  Scope note: this makes the failure *clear* at the divide entry point; the corpus walker
  (outside trouver) still feeds all 204 document-less files to it — file-level skip/log
  belongs there, and see **N14** for the design question behind those inputs.
- **N6** `_find_labels` (`convert.py:345-359`): duplicate labels silently last-wins, no
  warning — combined with N3 this misroutes refs with zero signal. **Fixed 2026-10-28:**
  a label redefined in a *different* note now issues a `UserWarning` naming the label
  and both notes (last-wins kept — it matches LaTeX aux-file semantics); repeats within
  one note stay quiet. Pinned by test cells `n6t1`/`n6t2` in `04_latex_20.convert`.
  Corpus sanity: `ellenberg_landesman_hsghssgqtfff.tex` (an N3 broken-label file) yields
  35 warnings over its 350 parts, the first naming `remark:`.
- **N7** `_replace_includegraphics_with_embedded_links_in_parts` (`convert.py:399-440`):
  the no-extension search loop leaves `filename` stale from a previous match when nothing
  is found (broken `![[base]]` links); matches on basename only (drops subfolder path);
  picks arbitrarily among multiple matches; re-walks the image folder per `\includegraphics`.
- **N8** `_recursive_reset` (`divide.py:792-799`) / `_is_numberedwithin`
  (`divide.py:553-562`): no cycle guard — any self- or mutual-loop in the reset
  hierarchy recurses to `RecursionError`. **Root cause identified (N13, below):** the
  only corpus crash (`kudo_harashita_scg4sc\main.tex`) is a *self*-loop `pf -> pf`,
  produced by a parse bug, not by the document. **Fixed 2026-10-28:** `_recursive_reset`
  now carries an optional `_seen` visited-set — a self- or mutual-loop in the reset
  hierarchy terminates after one pass instead of recursing forever. Pinned by test cell
  `n8t1` (mutual loop `a↔b`: no raise, child counters still reset).
- **N13** `\newtheorem` display-name parse bug — `numbered_newtheorems_counters_in_preamble`
  cannot distinguish a **braced display name** from a `[counter]` argument. Confirmed:

  | source | parsed | correct |
  |---|---|---|
  | `\newtheorem{pf}{Proof}` | `('pf', None)` | ✓ |
  | `\newtheorem{pf}{{\it Proof}}` | `('pf', 'pf')` | ✗ phantom self-reset; should be `('pf', None)` |
  | `\newtheorem{pf}{Proof}[pf]` | `('pf', 'pf')` | ✓ genuinely self-resetting |

  So any `\newtheorem{X}{{…}}` (braced/italic display name, no counter arg) gets a phantom
  reset-by-self → self-loop in `get_reset_hierarchy`. If that env is used in the body it
  crashes via N8; if not, the reset hierarchy is silently wrong. Corpus: 411 such
  definitions across 2 files; `kudo_harashita_scg4sc` is the one whose self-reset env
  (`pf`) is actually invoked → the single `RecursionError`. **Fixed 2026-10-28:** the
  None-defaulting moved out of `_search_counters_by_pattern` (which now returns the raw
  captured group, `dict[str, str | None]`) into `_combine_second_and_third_paramter_results`,
  where it applies only to the second-parameter path (a missing capture there means "own
  counter"); on the third-parameter path a missing capture now correctly leaves the
  reset-by slot as `None`. Pinned by test cells `n13t1` (braced display name →
  `('pf', None)`) and `n13t2` (plain name + genuine `[counter]` guards). Corpus
  re-verified: `kudo_harashita_scg4sc/main.tex` parses to `('pf', None)` and
  `divide_latex_text` completes (133 parts, no `RecursionError`).
- **N9** `swap_numbers_invoked` (`divide.py:1267-1275`): substring test — a macro like
  `\swapnumbersXYZ` false-positives.
- **N10 (format/reset divergence)** — see §6: global counter values formatted with
  hierarchical prefixes (and vice versa via N1) produce numbers matching neither real
  global nor `\numberwithin` numbering.
- **N11** `\tag{…}` ignored by the counter engine — corpus has 5,306 occurrences. Tagged
  equations carry *literal* numbers while the equation counter keeps incrementing, so any
  theorem-like env sharing the equation counter is shifted by the number of tagged
  equations before it.
- **N12** `\eqref` missing from `_add_links_to_refs`' ref regex (`convert.py:378` covers
  `cref/Cref/autoref/ref/pageref/vref/nameref`) — corpus has 5,198 occurrences; those refs
  are never wrapped into links.
- **N14 (design flag, 2026-10-27): should divide expand `\input`/`\include` before dividing?**
  The pipeline walks every `.tex` file and divides each independently — there is no
  main-file notion. In `latex_full`, 204 of 1,328 files (15.3%) lack
  `\begin{document}`: **192 are `\input` chapter fragments** (sibling main file with a
  document environment exists, e.g. `alberts_sfgcg/alberts_sfgcg.tex` +
  `Introduction.tex`, `Towers.tex`, …) and **12 are standalones** (e.g.
  `deligne_edpsr/deligne_edpsr.tex`, `milnor_olm/{imsmark,main,shead}.tex`). As of the N5
  fix these fail with a clear `ValueError` at `divide_preamble`; dividing them as-is would
  produce garbage (no preamble → no counter definitions). Options: (a) leave it — walker
  skips/logs non-document files; (b) expand `\input`/`\include` into the main file before
  dividing (one document per paper, matching how LaTeX compiles them), which also fixes
  N4's "label defined in a missing `\input` file" case for refs. Owner decision.

## 2. Standards violations (per `_nbdev_development/specs/CODING_STANDARDS/`)

| # | Violation | Where (generated file, 2026-10-25) | Spec |
|---|-----------|------------------------------------|------|
| S1 | **Duplicate defs, last wins** (PROGRESS.md F2) | `get_formatted_number` ×2 (`divide.py:375`, `1147`); `_build_number_string` ×2 (`998`, `1029`, first appears dead) | lifecycle: one def per name |
| S2 | **Commented-out dead code** — old versions of ~8 functions left in place | `divide.py` (286-317, 490-518, 625-642, 934-946, 1089-1201…); `preamble.py:28-73`; `folders.py:17-18,25-26,32-35` | lifecycle |
| S3 | **Print-only pseudo-tests** (PROGRESS.md F3) | `04_latex_20.convert.ipynb` | testing rule 2 |
| S4 | **Scaffolding comments** (`# --- ADD THIS LINE ---`) in shipped code | `divide.py:338`, `195-256` | documentation/lifecycle |
| S5 | Copy-paste docstring ("Return True if…" on a name-returning function) | `_environment_name_of_text` `divide.py:707-714` | documentation |
| S6 | Dead exports (`_node_numbering` exported, zero live callers; `_numbering_helper` likely unused) | `divide.py:949`, `905` | lifecycle |

**S1+S2 Status: fixed 2026-10-27** (closes PROGRESS.md F2). `04_latex_00.divide`: 7
pure-dead cells deleted (commented-out old versions of `get_counter_hierarchy`,
`_title_for_section_subsection_subsubsection_node` ×3, `_title_for_environment_node` ×2,
plus the first live `get_formatted_number` def and the first typed `_build_number_string`
def — both verified dead: `git show HEAD:` shows the earlier `get_formatted_number` was the
old implementation while the module shipped the later one via last-wins; the surviving
defs were moved ahead of their test cells, which pass unchanged against them). 6
commented blocks stripped from live cells (`_setup_numberwithins`,
`_setup_all_numberwithins`, `_section_title`, `_is_numbered`, `_node_numbering`, and a
trailing block inside `_title_for_section_subsection_subsubsection_node`).
`04_latex_10.preamble`: 48-line commented-out old `replace_inclusion_of_style_file_with_code`
stripped. `04_latex_05.folders`: 8 unreachable/commented lines removed (post-`return` node
checks, commented signature params). All three notebooks exec with 0 failing cells; full
export clean — 0 commented defs and exactly one def per name in the generated files. S6
remains open (deferred follow-up).

## 3. Performance

- **P1** `divide_latex_text` (`divide.py:1418`) parses the preamble **~10 times** — each
  `divide_preamble` + `remove_comments` is O(n) over the whole document: via
  `numbered_newtheorems_counters_in_preamble`, `numberwithins_in_preamble`,
  `get_counter_hierarchy` (re-calls both *and* `divide_preamble` directly),
  `get_reset_hierarchy` (→ `get_counter_hierarchy` again), `display_names_of_environments`,
  plus a final pass. Compute once, thread the result through.
- **P2** `_replace_includegraphics…` `os.walk`s the image folder per no-extension
  `\includegraphics` (see N7).

## 4. Test coverage

18 `numbering_example_*` fixtures in `nbs/_tests/latex_examples/` pin the current
behavior — a good net, but it pins N1/N2 as *expectations*, so the suite is green while
real documents come out mis-numbered. `mcp_monorepo/servers/tex_component_tools/server.py`
(`rename_latex_component`, `extract_environments`, `find_references`, `check_label_exists`,
`build_cref_cache`, `lint_tex_file`, `fix_tex_file`) has **no tests at all**.

## 5. Proposed remediation (worst-first; each step test-net-first per spec rule 3)

1. **N1** — drop the hardcoded `equation → section` default; hierarchy reflects only what
   the document declares (`\numberwithin`, `\@addtoreset`, `[counter]` args). Flip the two
   pinning tests with in-cell notes (characterize current behavior first, then flip).
2. **N2** — remove the `manual_envs` hack; map an environment to a counter only when its
   definition actually contains `\refstepcounter{…}`/`\stepcounter{…}`. Update
   `test_manual_environment_mapping`.
3. **S1+S2** — delete dead duplicate defs and commented-out blocks in `divide.py`,
   `preamble.py`, `folders.py` (closes PROGRESS.md F2).
4. **N5/N6/N7/N8/N9** — robustness: `None` guard in `divide_preamble` (**done 2026-10-27**,
   see N5 status; plus design flag N14); cycle guard in `_recursive_reset` + the N13
   parse fix it was fed by (**done 2026-10-28**, see N8/N13 status); duplicate-label
   warning in `_find_labels` (**done 2026-10-28**, see N6 status); includegraphics search fix; word-boundary test for
   `\swapnumbers`. N4 (ref display text) is a design decision, not a bug fix — flag
   separately.
5. **P1** — single preamble parse threaded through `divide_latex_text`.

## 6. Reproduction (executed 2026-10-25)

Script `_tmp/audit_divide_numbering_tmp.py` (manifest row in `_tmp/MANIFEST.md`) runs
`divide_latex_text` on two synthetic documents plus three real `latex_full` files.
Output (venv `trouver_py312_venv`):

**Synthetic A** — plain `article`, two sections, one equation each (real LaTeX numbers
them `(1)`, `(2)` globally):

```
counter hierarchy: {'section': 'part', 'subsection': 'section',
                    'subsubsection': 'subsection', 'paragraph': 'subsubsection',
                    'equation': 'section'}          ← N1 default injected, no \numberwithin in doc
```

**Synthetic B** — `\newenvironment{remark}` (no `\refstepcounter`, unnumbered in real
LaTeX), then one equation:

```
part titles:        '1. Intro', 'Remark 1.1.', '1'
newtheorem counters: {'remark': ('equation', None), ...}   ← N2: remark stole equation number 1
```

The unnumbered remark consumed equation value 1 (displayed `1.1`); the real equation's
title is inconsistent with it. In real LaTeX the remark has no number and the equation
is `(1)`.

**N5 confirmed live**: a document without `\begin{document}` crashes
`AttributeError: 'NoneType' object has no attribute 'span'` in `divide_preamble`.

**Real files** — part titles from `divide_latex_text`:

```
achter_dcgff:  … 'Theorem 1.', 'Situation 2.', … 'Lemma 2.1.2.', 'Lemma 2.1.3.',
               'Proposition 2.1.4.'
achter_oafacs: … 'Theorem 2.1.', … 'Proposition 3.1.', … 'Lemma 3.2.'
```

New manifestation (call it **N10**): the final digit runs *globally* across the document
(1, 2, then 2, 3, 4 for lemmas/propositions in §2.1) while a section/subsection prefix is
still prepended — so `Lemma 2.1.2` means "subsection 2.1, second theorem *in the whole
document*". If the counter were genuinely `\numberwithin{…}{subsection}`, real LaTeX would
print `2.1.1, 2.1.2, 2.1.3`; if global, just `2, 3, 4`. The pipeline's hybrid (global
count + hierarchical prefix, governed by the "parent > 0" rule in `get_formatted_number`)
matches **neither** — this is the concrete shape of "numberings not being correct" on
`latex_full` files. Fixing N1 alone is insufficient: formatting and resetting must both
derive from the same declared hierarchy.

## 7. Full-corpus sweep (executed 2026-10-25)

`sweep_latex_full_divide_tmp.py` ran `divide_latex_text` over **all 1,056 `.tex` files**
in `latex_full` (704 folders; some hold several files). Output:
`_tmp/latex_full_sweep_report_tmp.jsonl`.

- **852 files processed OK; 204 crashed (19.3%)**:
  - 203 × `AttributeError: 'NoneType' object has no attribute 'span'` — N5 (no
    `\begin{document}`; OCR'd sources and flattened multi-file extracts). The pipeline
    cannot even start on ~1 in 5 corpus files.
  - 1 × `RecursionError: maximum recursion depth exceeded` — **identified**:
    `kudo_harashita_scg4sc\main.tex`. Root cause is N13 (phantom self-reset from a braced
    `\newtheorem` display name) feeding the unguarded `_recursive_reset` (N8). No mutual
    `\numberwithin` cycle exists in the corpus.
- **Numbered-environment title shapes** across the 852 OK files (~15,054 titles):

  | components | count | example |
  |---|---|---|
  | 1 | 29 | `Theorem 12` |
  | 2 | 1,371 | `LEMME 2.` |
  | 3 | 8,136 | `Example 1.1.` |
  | 4 | 3,871 | `Lemma 2.1.2.` |
  | 5 | 1,687 | `Example 1.1.1.1.` |

  3–5-component titles (≈94%) are the N1/N10 hierarchical-prefix pattern; a 5-component
  number on an *example* counter is not producible by any standard LaTeX class — direct
  evidence the prefix chain is being applied beyond what the document declares.
- **Corpus construct census** (grep over all `.tex`): `equation` ×10,982, `align` ×9,853,
  `\eqref` ×5,198 (N12), `\tag{` ×5,306 (N11), `\section*` ×8,332, `\newtheorem` ×3,366,
  `\numberwithin` ×208, `\swapnumbers` ×11. (An earlier session profile claiming "0
  equation/align envs" was itself a broken count.)

**Verdict on completeness:** N1/N10 are the dominant visible defect (systemic, all
documents); N5 makes the pipeline unusable on ~19% of corpus files outright; N11/N12 are
additional real gaps touching ~10k constructs; N13+N8 account for the single crash. Every
crash mode in the corpus is now accounted for (203 × N5, 1 × N13→N8); no other exception
type occurred across all 1,056 files.
