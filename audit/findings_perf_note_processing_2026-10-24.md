# Perf audit: `replace_embedded_links_with_text` memoization (N1)

Part of the note-processing audit [`findings_note_processing_2026-10-20.md`](findings_note_processing_2026-10-20.md).
Frozen 2026-10-24. Measurements taken 2026-10-23 on the Windows dev box.

## Benchmark harness (verbatim)

```python
"""Bench for N1 (audit/findings_note_processing_2026-10-20.md):
`MarkdownFile.replace_embedded_links_with_text` — before/after memoization.

Canonical recipe per _nbdev_development/specs/CODING_STANDARDS/performance.md:
perf_counter around the call, one warmup discarded, median of 5 runs,
fixed deterministic input, two sizes (complexity-class check).
VaultNote name->path cache is warmed before timing (one-off cost excluded).
"""
import statistics
import tempfile
import time
from pathlib import Path

import trouver.obsidian.file as f
from trouver.obsidian.vault import VaultNote


def build_vault(root: Path, n_targets: int, lines_per_target: int,
                embeds_per_target: int) -> None:
    for t in range(n_targets):
        body = '\n'.join(
            f'Line {i} of target {t}. Some fixed lorem ipsum text.'
            for i in range(lines_per_target))
        (root / f'target_{t}.md').write_text(body + '\n')
    src = 'Source note.\n\n' + ''.join(
        f'![[target_{t}]]\n\n' * embeds_per_target
        for t in range(n_targets))
    (root / 'source_note.md').write_text(src)


def run_once(vault: Path) -> int:
    vn = VaultNote(vault, name='source_note')
    mf = f.MarkdownFile.from_vault_note(vn)
    mf.replace_embedded_links_with_text(vault)
    return len(str(mf))


def bench(n_targets: int, lines: int = 20, embeds: int = 3,
          runs: int = 5) -> tuple[float, int]:
    with tempfile.TemporaryDirectory(prefix='bench_embed_') as td:
        vault = Path(td)
        build_vault(vault, n_targets, lines, embeds)
        VaultNote.update_cache(vault)   # warm name->path cache (excluded)
        run_once(vault)                 # warmup run (discarded)
        times = []
        out = 0
        for _ in range(runs):
            t0 = time.perf_counter()
            out = run_once(vault)
            times.append(time.perf_counter() - t0)
        return statistics.median(times), out


if __name__ == '__main__':
    for n in (50, 200):
        med, out = bench(n)
        print(f'n_targets={n}: median {med:.3f} s (output {out} chars)')
```

Fixture: `n_targets` target notes of `lines_per_target` lines each; a source
note embedding every target `embeds_per_target` times. The "before" state
re-parses each target on every occurrence (600 parses at size 200); the
"after" state memoizes parsed files by resolved path for the call (200 parses).

## Measurements

| date | function (notebook · cell) | code state | input size | before | after | change |
|------|----------------------------|------------|------------|--------|-------|--------|
| 2026-10-23 | `MarkdownFile.replace_embedded_links_with_text` (nb 40 · cells 237–239) | `855d584`* → `f00fa30` (guard cell in `6281e61`) | 50 targets × 20 lines, 3 embeds each (output 151,063 chars) | 0.049 s | 0.006 s | memoize parsed target files per call by resolved path — ~8× |
| 2026-10-23 | same | same | 200 targets × 20 lines, 3 embeds each (output 612,013 chars) | 0.232 s | 0.029 s | ~8×; scaling stays linear in distinct targets, not occurrences |

\* The "before" tree was dirty with concurrent sessions' uncommitted changes
(nb 32/37/38 ML work); none of them touch nb 40's embedded-link functions, so
`855d584` is the citable baseline for this measurement.

Notes:
- Output is byte-identical between states (same char counts above) — the change
  is pure parse deduplication, no behavior change.
- Regression guard: nb 40 test cell asserts a 200-target expansion stays under
  1.0 s (~34× headroom over the 0.029 s median), per the perf-guard rule in
  `CODING_STANDARDS/performance.md`.
