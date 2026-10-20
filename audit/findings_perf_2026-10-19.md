# Performance measurements — VaultNote cache (2026-10-19)

Effort: the three cache speedups from `findings_factoring_perf_2026-10-19.md` §2.2/§2.3
(link-map threading, delete-path rebuild, rename pre-check). Baseline measured before
any change; "after" rows added as each fix lands. File frozen when the effort is done.

## Benchmark harness

Keeper script: `bench_vault_cache.py` (repo root, committed at baseline). Verbatim at
baseline commit `7956355`; re-run with:

```bash
..\/trouver_py312_venv\Scripts\python.exe bench_vault_cache.py --size 10 100
```

Method (per `_nbdev_development/specs/CODING_STANDARDS/performance.md`): deterministic
n-note fixture vault (note_i wikilinks note_(i+1)), fresh vault per timed run, 1 warmup
discarded, median of 3 runs, `time.perf_counter`. Targets:

- `link_pass` — `all_links_in_vault` (full-vault read pass; §2.2)
- `delete` — cold-cache (`clear_cache()`) `VaultNote(name=...).delete()` (lazy rebuild + single-entry remove)
- `rename` — cold-cache `VaultNote(name=...).rename(...)` (§2.3, full-cache sweep)

## Measurements

| Date | Function (notebook · cell) | Code state | Input size | Before | After | Change |
|---|---|---|---|---|---|---|
| 2026-10-19 | `all_links_in_vault` (`03_obsidian_70.vault_and_links.ipynb`) | `7956355` | 10 / 100 notes | 1.2 / 9.5 ms | — | baseline (scaling ~8× for 10× size — linear ✓) |
| 2026-10-19 | `VaultNote.delete` (`03_obsidian_10.vault_file_crud.ipynb`) | `7956355` | 10 / 100 notes | 0.5 / 1.6 ms | — | baseline (scaling ~3×) |
| 2026-10-19 | `VaultNote.rename` (`03_obsidian_10.vault_file_crud.ipynb`, cell `8830213c`) | `7956355` | 10 / 100 notes | 1.9 / 13.8 ms | — | baseline (scaling ~7× for 10× size — linear ✓) |
| 2026-10-19 | `notes_linked_in_note`, every note, no map (`05_personal_vault_10.notes.ipynb`) | `7956355` → `9165969` | 10 / 100 notes | — | 1.2 / 8.6 ms | reference workload for link-map threading (one file read per call; linear ✓) |
| 2026-10-19 | `notes_linked_in_note`, every note, with map (`05_personal_vault_10.notes.ipynb`) | `7956355` → `9165969` | 10 / 100 notes | — | 1.3 / 8.1 ms | **no speedup** on a single-pass workload: building the map is itself a full-vault read (≈ `link_pass`), so it cancels out the per-note reads it saves |

**Finding (honest null result):** threading `link_map` pays off only when the caller
already holds the map (e.g. from an earlier `all_links_in_vault` call) or queries many
notes against one prebuilt map — then each call is a dict lookup instead of a file read.
On a from-scratch single pass it is neutral to slightly slower. The parameter stays
(opt-in, documented with this caveat); no default behavior changed.
