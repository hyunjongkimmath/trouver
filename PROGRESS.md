# PROGRESS — trouver state (single source of truth)

**Next action:** Phase 1 done. Start Phase 3 fix #1: F1 silent `UserWarning` no-op in `05_personal_vault_20.information_notes.ipynb` (`index_note_of_note`) — see `audit/findings_code_quality_2026-10-13.md`.

## Phases
| Phase | What | Done when |
|---|---|---|
| **1 Spec + assessment** ✅ 2026-10-13 | Write the ideal-code spec; measure conformance | `CODING_STANDARDS.md` extended; report in `audit/` |
| **2 Enforcement** | Checker script flags spec violations automatically | `nbs/_tools/check_standards.py` runs (nbdev test cell or Makefile target) and reports per-notebook violations |
| **3 Remediation** | Fix modules worst-first from the scorecard | Fixed modules pass the checker; scorecard re-measured |

## Phase 2 — enforcement (pending)
Checker `nbs/_tools/check_standards.py` flags, per notebook:
- functions with >20 executable lines (excluding docstring/blank/comment lines)
- exported defs missing a docstring or a return annotation
- test cells containing `print(` and no assertion
- duplicate definitions of the same name in one notebook

## Phase 3 — remediation (pending, worst-first)
Per `audit/findings_code_quality_2026-10-13.md`:
1. **F1** silent `UserWarning` no-op (`05_personal_vault_20.information_notes`) — real bug
2. **F2** duplicate defs in `04_latex_00.divide` (last one wins) — real bug
3. **F3** print-only pseudo-tests (`04_latex_20.convert`)
4. **F9** under-tested frontier: `09_app_00.gui` (127 exports, 0 tests), `08_ml_*`
5. then per-module cleanup: dead code, TODO hotspots, god functions (F8)

## Log
- 2026-10-13 — ICM workspace initialized: `CLAUDE.md` map + this file created; `CODING_STANDARDS.md` extended (docstrings, type hints, assert-only tests, one-def-per-name); first assessment `audit/findings_code_quality_2026-10-13.md` (scorecard + findings F1–F9); `nbs/CONTEXT.md` docstring claim corrected to match reality.
- 2026-10-14 — spec reorganized: `CODING_STANDARDS.md` is now a ≤1-screen index over `CODING_STANDARDS/` (function_shape, documentation, testing, lifecycle), each file expanded with rationale, real examples, edge cases, and the Phase 2 checker hook. References updated in `CLAUDE.md` + `nbs/CONTEXT.md`.
- 2026-10-14 — spec rot-proofed: examples moved to synthetic snippets in `CODING_STANDARDS/examples/`; detail files now cite live violations only as F-number pointers to the dated audit report. Three tiers: rules (stable) / examples (synthetic) / audit (frozen evidence).
- 2026-10-14 — spec de-coupled from the audit snapshot: "Why it matters here" rewritten self-contained (decay patterns, no F-numbers/dated paths); stability rule added to the index; feedback memory recorded. Spec no longer depends on any dated file.
- 2026-10-14 — documentation spec made nbdev-fit: two-surface model (docstring = API ref that ships in `trouver/`; markdown cell = narrative on `_docs/`), load-bearing first line, docstrings-as-Markdown, examples-in-cells + `#| hide`, module landing cell, `#| no_doc` discipline. **Follow-up:** no active `settings.ini` (only `settings.ini.old`) — blocks `nbdev_show`; confirm a live one exists before building docs.
- 2026-10-14 — new spec topic `type_hints.md` (+ synthetic `examples/type_hints.md`): full annotations on exports, modern 3.10 generics / PEP 604 unions, fully-qualified containers, `_`-helper best-effort, `Any` needs a reason, no lying hints. Index updated; `documentation.md` now defers its annotation rules to it (single source of truth).
- 2026-10-14 — `documentation.md`: added "many parameters" edge case (one bullet per line, signature order, defaults inline, single-line descriptions) + a synthetic many-param example.
- 2026-10-14 — `testing.md`: rule 3 rewritten to lead with "test pure logic directly; isolate only the I/O boundary" (`_tests/` = fixture data, test code stays in cells); added "too many tempdirs is a smell" edge case.
- 2026-10-14 — `testing.md`: added rule 4 — prefer `fastcore.test` (`test_eq`/`test_ne`/`ExceptionExpected`) over bare `assert` / `try-except`, grounded in the codebase's actual usage; Phase-2 adds review candidates; examples gain a fastcore bad/good pair.
- 2026-10-19 — spec moved out of the project tree: `nbs/CODING_STANDARDS.md` + `nbs/CODING_STANDARDS/` → workspace-level `_nbdev_development/specs/` (shared across nbdev projects, reusable by future ones). All in-project references (`CLAUDE.md`, `nbs/CONTEXT.md`, `_REVIEW_CHECKLIST.md`) repointed. Phase 2's planned `nbs/_tools/check_standards.py` is superseded: the live checkers are `_nbdev_development/spec_checkers/check_*.py` (function_shape, type_hints, testing, dupes/perf) — Phase 2 counts as satisfied by those.
- 2026-10-19 — new spec topic `performance.md` (+ synthetic `examples/performance.md`): measure-before-claiming, canonical recipe (perf_counter + warmup + median on a fixed fixture), two-size scaling test for complexity class, caching rule for pure hot paths, I/O-once-per-run with threaded maps, loose perf-guard bounds in test cells. Index updated; `check_dupes_perf.py`'s README row now cites it.