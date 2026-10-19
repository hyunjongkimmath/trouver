# Trouver code-quality assessment (2026-10-13)

Lens: `nbs/CODING_STANDARDS.md` (as extended 2026-10-13) + the ICM walk test. Evidence: Grep over all ~101 notebooks in `nbs/` (re-runnable patterns in the footer). **Verdict up front: structure is strong, enforcement is missing.** Co-located testing and notebook discipline are exemplary where touched (`01_helper_*`, `04_latex_00.divide`); the ML layer and GUI are an under-tested frontier; two real bugs hide in plain sight (F1, F2).

## What's genuinely good
1. **Co-located testing at scale** — 2,497 assertion lines across 73 notebooks; exemplar test:export ratios ≈1:1 (`01_helper_20.latex.core` 181/155, `01_helper_25.macros_and_commands` 186/209).
2. **nbdev discipline** — clean source/generated split; `.aiexclude` keeps AI off generated code; shared `_tests/` fixtures.
3. **Documentation culture** — markdown explanation cells precede implementations in maintained notebooks; `show_doc()` usage; Examples sections.

## Findings (ranked)

### F1 · Silent no-op: warning constructed, never raised — HIGH (bug)
`05_personal_vault_20.information_notes.ipynb`, `index_note_of_note`: builds `UserWarning(f'...')` but never raises it — the guard is dead code and callers get no signal.
**Fix:** `warnings.warn(...)` (or raise); add a test asserting the warning fires.

### F2 · Duplicate definitions, last-one-wins — HIGH (bug)
`04_latex_00.divide.ipynb` defines `get_formatted_number` twice (~lines 1527 & ~4200) and `_build_number_string` twice (~3948 typed, ~4019 untyped) — the *untyped* version silently wins. nbdev exports both into one namespace; nothing errors.
**Fix:** delete the superseded defs (or merge), re-export, re-run divide tests.

### F3 · Print-based pseudo-tests — HIGH
`04_latex_20.convert.ipynb`: cells run a mock-filesystem scenario and `print` results with zero assertions — they pass no matter what the code does.
**Fix:** convert to `test_eq` assertions (fixtures already exist in `_tests/`).

### F4 · Exported-incomplete functions — MEDIUM
`reference_of_information_note` (`05_personal_vault_20.information_notes.ipynb`) is exported with an empty/TODO body. Violates existing practice 5 "Finish or Don't Export".
**Fix:** drop `#| export` until implemented, or raise `NotImplementedError`.

### F5 · Migration scars — MEDIUM
`04_latex_00.divide.ipynb`: `# --- NEW HIERARCHICAL LOGIC ---` marker; superseded `_setup_numberwithins`/`_setup_all_numberwithins` still exported next to their replacements (`get_counter_hierarchy`/`get_reset_hierarchy`).
**Fix:** grep for callers first, then delete the superseded helpers.

### F6 · Documented ideal ≠ reality — MEDIUM (meta)
`nbs/CONTEXT.md` claimed docstrings use `| param | type | description |` tables; **zero** notebooks do. Actual dominant style: `**Parameters**` bullets (64 uses / 21 files). Spec now canonicalizes bullets.
**Fix:** done 2026-10-13 — spec + CONTEXT.md aligned on the bullet form.

### F7 · Even the exemplar violates the rules — MEDIUM (meta)
`01_helper_04.regex.ipynb` (named "best" in nbs/CONTEXT.md) contains commented-out code, a stray empty `#| export` cell, and TODO rename markers. Standards are aspirational — nothing enforces them.
**Fix:** Phase 2 checker; quick win: clean this one notebook so the exemplar actually exemplifies.

### F8 · God functions — MEDIUM
`setup_reference_from_latex_parts` (`04_latex_20.convert.ipynb`): ~25 parameters, ~50-line body — the worst 20-line-limit violation in the codebase. `divide_latex_text` (~40 lines) is decomposed but still over limit.
**Fix:** staged extraction (parse → build → write) per practice 3; consider a parameter object for the 25-arg function.

### F9 · Under-tested frontier — TRACK IN PHASE 3
| Notebook | Exports | Test lines |
|---|---|---|
| `08_machine_learning_10.information_note_types` | 451 | 18 |
| `08_machine_learning_25.notation_summarization` | 383 | 50 |
| `08_machine_learning_90.semantic_search` | 426 | 67 |
| `09_app_00.gui` | 127 | **0** |

Plus 273 TODO/FIXME markers across 52 files (hotspots: `05_personal_vault_15.reference` 37, `03_obsidian_40.file` 27, `08_ml_25` 20). Return annotations appear in only 865 places / 84 files; explicit `Returns:` docstring sections in just 17 places / 13 files.

## Scorecard
| Dimension | Grade |
|---|---|
| Function length (≤20) | ⚠️ holds in maintained modules; F8 violations in convert/divide |
| Co-located tests | ✅ strong in `01_*`, `04_latex_00`; ❌ absent in `09_app_00.gui`, thin across `08_ml_*` |
| Docstrings | ⚠️ present on most exports; returns documented in only 13 files |
| Type hints | ⚠️ partial (865 return annotations / 84 files) |
| Dead code | ❌ commented-out blocks, superseded helpers, print-pseudo-tests |
| Spec enforcement | ❌ none — the spec predates this audit; nothing checks it |

**Bottom line:** the decay is not structural — the nbdev skeleton and testing culture are real strengths. It's an enforcement gap: F1/F2 are silent bugs only a careful reader (or a checker) would catch, and Phase 2's job is to make them impossible to merge unnoticed.

## Footer — re-runnable evidence
All counts via Grep over `nbs/*.ipynb` (2026-10-13):
- exports: pattern ``#\|\s*export`` → ≈10,756 total lines
- test signal: `test_eq|test_ne|test_is_not|ExceptionExpected|assert` → 2,497 / 73 files
- TODOs: `#\s*(TODO|FIXME|HACK)\b` → 273 / 52 files (excludes the domain tag `#_meta/TODO/split`)
- return hints: `->\s*\S` → 865 / 84 files
- docstring returns: `Returns:` → 17 / 13 files; table headers `\| param \| type` → 0
