# Trouver — map (Layer 0)

LaTeX → Obsidian math-note pipeline, built with nbdev. **Notebooks in `nbs/` are the source of truth**; `trouver/` is auto-generated — never edit it.

## Layout
| Path | Role |
|---|---|
| `PROGRESS.md` | STATE: phase, next action. Read first on any "continue". |
| `CONTEXT.md` | METHOD: nbdev workflow, module map, environment. Never records progress. |
| `nbs/` | SOURCE: notebooks (truth), `_tests/` fixtures, tutorials. |
| `../../_nbdev_development/specs/CODING_STANDARDS.md` + `CODING_STANDARDS/` | SPEC (workspace-level, shared across nbdev projects): index + per-topic detail files (shape, docs, testing, lifecycle) + synthetic examples. Wins over habit when they conflict. |
| `nbs/CONTEXT.md` | Notebook conventions: naming, cell flags, structure, quality spectrum. |
| `audit/` | OUTPUT: dated code-quality assessments; latest file = current state of the codebase. |
| `trouver/` | GENERATED — off-limits (see `.aiexclude`). |

## Routing
| Job | Read | Save to |
|---|---|---|
| "continue" / status | `PROGRESS.md` → next action | tick `PROGRESS.md` |
| write/refactor code in `nbs/` | spec index (`../../_nbdev_development/specs/CODING_STANDARDS.md`) → relevant `CODING_STANDARDS/<topic>.md` + `nbs/CONTEXT.md` (cell flags, naming) | the notebook itself — never `trouver/` |
| assess / audit quality | latest `audit/findings_*.md` | new dated file in `audit/` |
| run tests / export | `CONTEXT.md` §Nbdev Workflow | — |

## Rules
1. Edit notebooks, then `nbdev_export`. Never edit files under `trouver/`.
2. `../../_nbdev_development/specs/CODING_STANDARDS.md` is the spec: 20-line limit, docstrings, type hints, assert-only tests. When in doubt, the spec wins over local habit.
3. State lives only in `PROGRESS.md`; method only in `CONTEXT.md`. Never record progress in a method file.
4. Keep this map ≤1 screen. If a rule needs paragraphs, it belongs in `CONTEXT.md`.