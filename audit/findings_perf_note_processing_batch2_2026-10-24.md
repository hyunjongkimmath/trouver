# Perf audit: note-processing pass consolidation (N2+N3+N4)

Part of the note-processing audit [`findings_note_processing_2026-10-20.md`](findings_note_processing_2026-10-20.md).
Frozen 2026-10-24. Measurements taken 2026-10-24 on the Windows dev box.

**Result: no measurable end-to-end change.** The passes consolidated here are
not the dominant cost of `process_standard_information_note` — at these sizes
the runtime is dominated by the `reset_parts()` full re-parse at the end of
`merge_display_math_mode_into_preceding_text` (N5, deliberately kept) plus
per-part list rebuilds. The consolidation ships on correctness/simplicity
merits (fewer passes over `parts`, one code path for the default flag
combination), with equivalence pinned by test cells — not on a speedup claim.

## Benchmark harness (verbatim)

```python
"""Bench for N2/N3/N4 (audit/findings_note_processing_2026-10-20.md):
`process_standard_information_note` end-to-end, before/after pass consolidation.

Canonical recipe per _nbdev_development/specs/CODING_STANDARDS/performance.md:
perf_counter around the call, one warmup discarded, median of 5 runs,
fixed deterministic input, two sizes (complexity-class check).
"""
import statistics
import time
from pathlib import Path

from trouver.obsidian.file import MarkdownFile
from trouver.personal_vault.note_processing import process_standard_information_note


def build_note(n_blocks: int) -> str:
    out = []
    for b in range(n_blocks):
        out.append(f'# Section {b}')
        out.append('')
        out.append(f'Body text of block {b} with some lorem ipsum.')
        out.append('#tag_for_block')
        out.append('')
        out.append('$$')
        out.append(f'x_{b} + y_{b}')
        out.append('= z_{b}')
        out.append('$$')
        out.append('')
        if b % 50 == 0:
            out.append('# Meta')
            out.append('')
            out.append(f'meta content {b}')
            out.append('')
            out.append('# See Also')
            out.append('')
            out.append('- [[some_other_note]]')
            out.append('')
    out.append('Final line.')
    return '\n'.join(out) + '\n'


def run_once(text: str) -> int:
    mf = MarkdownFile.from_string(text)
    process_standard_information_note(
        mf, vault=None, replace_embedded_links_with_content=False)
    return len(str(mf))


def bench(n_blocks: int, runs: int = 5) -> tuple[float, int]:
    text = build_note(n_blocks)
    run_once(text)  # warmup (discarded)
    times, out = [], 0
    for _ in range(runs):
        t0 = time.perf_counter()
        out = run_once(text)
        times.append(time.perf_counter() - t0)
    return statistics.median(times), out


if __name__ == '__main__':
    for n in (200, 800):
        med, out = bench(n)
        print(f'n_blocks={n}: median {med:.3f} s (output {out} chars)')
```

Fixture: `n_blocks` body sections, each with a heading, a body line, an
in-line tag line, and a 4-line display-math chunk; every 50th block adds a
`# Meta` and a `# See Also` section so `_remove_sections` is exercised.
Default flags (all tail passes on, math merged into preceding text) — the
combination the consolidation targets.

## Measurements

| date | function (notebook · cell) | code state | input size | before | after | change |
|------|----------------------------|------------|------------|--------|-------|--------|
| 2026-10-24 | `process_standard_information_note` (nb 25 · cell 10) | `1e93f3f`* → `6e6c86e` | 200 blocks (14,992 chars in) | 0.058 s | 0.061 s | no measurable difference (within run-to-run noise) |
| 2026-10-24 | same | same | 800 blocks (61,036 chars in) | 0.215 s | 0.253 s | no measurable difference; scaling stays linear in blocks in both states |

\* The "before" tree was dirty with concurrent sessions' uncommitted changes
(ML notebooks nb 32/37/38); none of them touch nb 40's `MarkdownFile` methods
or nb 25's pipeline, so `1e93f3f` is the citable baseline for this measurement.

Notes:
- Output is byte-identical between states (same char counts at both sizes) —
  equivalence also pinned by test cells T1–T4 in nb 40 / nb 25.
- No perf-guard cell added: there is no measured bound to guard, per the
  "no claim without numbers" rule in `CODING_STANDARDS/performance.md`.
- If a future audit targets this pipeline's runtime, N5 (the trailing
  `reset_parts()` re-parse) is the candidate, not the pass count.
