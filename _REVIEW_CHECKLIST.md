# Review checklist — .md files created (TEMPORARY)

> Working doc for assessing each file we created, one by one. Tick as you go; delete this file when done.
> Paths are relative to `Python/trouver/` unless noted. "Look for" = the main thing(s) to assess in that file.

## Workspace scaffolding (ICM)

- [ ] `CLAUDE.md` — Layer-0 map: layout table + routing table + 4 rules.
  - Look for: ≤1 screen; every rule is a pointer, not a paragraph; "continue" routes to PROGRESS.md; spec wins over habit stated.
- [ ] `PROGRESS.md` — STATE: phase machine (1 ✅ / 2 pending / 3 pending), next action, log.
  - Look for: single source of truth for position; state lives only here, never in method files.

## Spec — index

- [ ] `../../_nbdev_development/specs/CODING_STANDARDS.md` — ≤1-screen index over the 4 topics + `examples/`; hard limits box; stability rule.
  - Look for: no dated-file references; stability rule present and clear; every link resolves to a real file.

## Spec — detail files (rules)

- [x] `../../_nbdev_development/specs/CODING_STANDARDS/function_shape.md` — 20-line limit · one responsibility · extract-over-nest · trust boundaries.
  - Look for: five-section shape intact; "Why it matters here" is a self-contained pattern (no F-numbers / dated paths).
- [ ] `../../_nbdev_development/specs/CODING_STANDARDS/documentation.md` — canonical docstring form · no param tables · type hints on exports.
  - Look for: same as above; drift story explains *why bullet form*; "Returns" required-vs-omittable edge case is clear.
- [ ] `../../_nbdev_development/specs/CODING_STANDARDS/type_hints.md` — full annotations on exports · modern (3.10) generics/unions · fully-qualified containers · no lying hints.
  - Look for: five-section shape intact; "Why it matters here" is the self-contained drift pattern (partial/uneven annotations, no F-numbers / dated paths); `Any`-needs-a-reason and `_`-helper best-effort rules present.
- [ ] `../../_nbdev_development/specs/CODING_STANDARDS/testing.md` — co-located tests · assert-only rule · isolation (tempfile / mock / `_tests/`).
  - Look for: "print-only ≠ test" stated crisply; GUI edge case framed as a Phase-3 note, not an exception.
- [ ] `../../_nbdev_development/specs/CODING_STANDARDS/lifecycle.md` — delete dead code · finish-or-don't-export · one def per name.
  - Look for: pattern bullets (commented-out / TODO body / migration scars / duplicate defs); no F-numbers; "grep callers before deleting" edge case present.

## Spec — examples (synthetic)

- [ ] `../../_nbdev_development/specs/CODING_STANDARDS/examples/function_shape.md` — nested god-function → extracted helpers; naming; boundary comments.
  - Look for: fully synthetic — zero live function names / line numbers.
- [ ] `../../_nbdev_development/specs/CODING_STANDARDS/examples/documentation.md` — canonical form + bad pairs (missing `**Parameters**`, untyped export).
  - Look for: synthetic; the "good" form matches the canonical form in `documentation.md` exactly.
- [ ] `../../_nbdev_development/specs/CODING_STANDARDS/examples/type_hints.md` — partial annotation, legacy aliases → built-ins/`|`, half-qualified generic, lying return type.
  - Look for: fully synthetic; each bad pair shows failure → fix; modern syntax in every "good" version.
- [ ] `../../_nbdev_development/specs/CODING_STANDARDS/examples/testing.md` — print-pseudo-test → asserted twin; mocked LLM call; demo-print edge case.
  - Look for: synthetic; assertion keywords present in every "good" version.
- [ ] `../../_nbdev_development/specs/CODING_STANDARDS/examples/lifecycle.md` — commented-out export, empty-body export, duplicate-def last-wins.
  - Look for: synthetic; each shows the failure → the fix.

## Audit (frozen evidence)

- [ ] `audit/findings_code_quality_2026-10-13.md` — dated snapshot: verdict up front, F1–F9 with Fix lines, scorecard, re-runnable greps.
  - Look for: this is the ONLY place live names + line numbers appear; self-contained (nothing in the spec points down to it).

## Memory (meta — outside the project)

- [ ] `C:\Users\hyunj\.claude\projects\C--Users-hyunj-Documents-Development\memory\feedback-spec-stability.md` — feedback memory: specs must not depend on dated files.
  - Look for: frontmatter correct (`type: feedback`); **Why** + **How to apply** present; linked in `MEMORY.md`; `[[feedback-factoring-style]]` link resolves.

---

**Coverage:** 14 project files + 1 memory file = **15 created**.
**Pre-existing / out of scope:** `trouver/CONTEXT.md`, `trouver/README.md` (not created); `nbs/CONTEXT.md` (edited, not created).
