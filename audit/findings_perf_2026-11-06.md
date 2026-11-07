# Perf findings 2026-11-06 — ripgrep-backed candidate discovery for `VaultNote.rename`

## Harness (verbatim, reproducible from this file)

Fixture: the live Math vault (`MATH_VAULT_LOCATION`, 159,184 `.md` files,
379 MB), needle `'Homotopy'` (appears in 471 notes — typical for a note name).
Machine: Windows 11 home desktop, Defender real-time protection active.

Variant ladder (`_tmp/bench_rename_tiers_tmp.py`, faithful loop-body
simulation of `rename`'s scan; each variant run twice, all variants agree on
the 471 hits):

- **A current** — `exists()` + `text()` (stats twice per file), text-mode
  read (full UTF-8 decode of every file), substring skip test after decoding.
- **B** — A minus the redundant second stat (`open` + tolerate `FileNotFoundError`).
- **C** — B plus bytes-level prefilter (decode only when raw bytes contain the needle).
- **D** — C with `ThreadPoolExecutor(max_workers=8)`.

Ripgrep route: `_note_paths_containing_literal('Homotopy', vault)` after
export; ripgrep 15.2.0 (`winget install BurntSushi.ripgrep.MSVC`), invoked as
`rg --hidden --no-ignore --no-messages -0 -l --fixed-strings -g *.md -- <needle> .`
with `cwd=vault`.

## Results (date · function · state · size · before → after · change)

| date | function (nb · cell) | state | size | before | after | change |
|---|---|---|---|---|---|---|
| 2026-11-06 | rename scan loop (03_obsidian_10 · 8830213c) | HEAD → working tree | 159,184 notes | A: 63.9 s / 84.1 s (r1/r2) | ripgrep candidates r1/r2/r3: 22.2/17.0/**15.8 s** + patch pass over the ≤471 candidates only | full-vault scan → `rg -l` literal files-with-matches superset, regexes unchanged |
| 2026-11-06 | rename scan loop variants | working tree | same | A: ~64–84 s | B: 75.8/39.5 · C: 35.5/37.4 · D: 32.9/34.0 s | micro-variants measured to isolate each fix (see below) |
| 2026-11-06 | raw-I/O floor reference | n/a | same | — | 75.1 s cold bytes-read+search, single thread | minimal possible full scan, no Python overhead |

## Verdicts

- **ripgrep ≈ 4–5×** over the current loop on this vault, and it is the
  practical floor: its own search CPU is ~0.03 s (`user` time) — the remaining
  ~16 s is 159K file opens through NTFS + Defender, which no scan-based
  approach escapes (raw `rg` from git-bash measured identically: 17–19 s).
- **Micro-variants were honest null-to-modest results in isolation** on warm
  cache: B (no double stat) ≈ 2× at best with noisy runs, C (bytes prefilter)
  small, D (threading) surprisingly weak here (~33 s — Defender appears to
  serialize opens). They are NOT shipped; the rg route supersedes them and
  beats D by ~2×. The fallback path is deliberately left byte-identical to
  the old loop (zero risk when rg is absent).
- **Equivalence**: every link style contains `old_name` literally, so rg's
  output is a sound superset of the referencing notes; the regex passes make
  all replacement decisions. All runs returned the same 471 hits; the pre-existing
  rename test net (bystander/near-miss/all-link-styles cells) plus new
  gitignored-dir + hidden-dir integration cells pin both routes to identical
  behavior. `--hidden --no-ignore` is load-bearing: `md_files_in_dir`'s cache
  walk has no exclusions, so a default rg run (which skips hidden/gitignored
  files) would have been unsound.

## Deferred follow-ups

- Sub-17-s renames need an index, not a faster scan (persistent backlink
  index, or Obsidian's own `metadataCache` when invoked from trouver-obs).
- A Windows Defender exclusion for the vault folder would lower every row
  above (owner action, unmeasured).
