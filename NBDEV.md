# NBDEV — reference for this project

**Where to find it:**
- Source: [github.com/fastai/nbdev](https://github.com/fastai/nbdev) (mirror: [AnswerDotAI/nbdev](https://github.com/AnswerDotAI/nbdev))
- Docs site: [nbdev.fast.ai](https://nbdev.fast.ai/) — API reference + tutorials (start with the [walkthrough](https://nbdev.fast.ai/tutorials/tutorial.html))
- In-terminal: `nbdev-help` lists every installed command with its current name/flags — treat it as ground truth over this file

**Version note — you are on nbdev3.** The Jan 2026 major update moved config from `settings.ini` to `pyproject.toml` (`[tool.nbdev]`; your `settings.ini.old` is the migrated remnant). Command names also changed from underscore to hyphen form. Commands in `CONTEXT.md` are nbdev2-era — mapping below.

## Day-to-day commands (nbdev3 names)

| You type (v3) | Old name (v2, in CONTEXT.md) | What it does |
|---|---|---|
| `nbdev-export` | `nbdev_export` | Notebooks → `trouver/*.py` |
| `nbdev-test` | `nbdev_test_nbs` | Run notebook tests in parallel (`--n_workers 0` to avoid the BrokenProcessPool issue you hit; `--timing` for per-cell times) |
| `nbdev-docs` | `nbdev_build_docs` | Build the Quarto docs site (host: `hyunjongkimmath.github.io/trouver` per `[project.urls]`) |
| `nbdev-update` | `nbdev_update_lib` | **Reverse** sync: changes made in `trouver/*.py` → back into the notebooks |
| `nbdev-prepare` | — | export + test + clean + README in one pass (the CI one-liner) |
| `nbdev-preview` | — | Render docs locally in a browser before pushing |
| `nbdev-trust` / `nbdev-clean` | — | Trust / strip metadata from notebooks (clean = merge-conflict avoidance) |
| `nbdev-help` | — | Full command list for the installed version |

Your config (`pyproject.toml` → `[tool.nbdev]`): `lib_name = "trouver"`, `nbs_path = "nbs"`, `recursive = "True"`, `tst_flags = "tst"`.

## Cell tags (the `#|` directives)

| Tag | Effect |
|---|---|
| `#| export` / `#| exporti` | Export cell to lib / export **interactively** (skip at docs-render time) |
| `#| default_exp <mod>` | Default target module for subsequent exports (e.g. `default_exp helper.packages`) |
| `#| hide` | Keep in notebook, exclude from docs |
| `#| eval:off` | Don't run the cell when building docs |
| `#| code` / `#| markdown` | Treat cell as code/markdown for export/docs purposes |
| `#| include <file>` | Splice an external file's contents into the docs page |
| `#| flags: tst` | Cell only runs under `nbdev-test --flags tst` (your `tst_flags`) — gate slow tests this way |
| `#| comments:strip` | Drop comments from the exported code |
| `#| self:module` / `#| self:class` | Export as module-level / class-body code (for `@patch` methods) |
| `#| path <dir>` | Override output location for this notebook's exports |

## Features you probably don't know about

1. **Two-way sync is real.** `nbdev-update` propagates edits made directly in `trouver/*.py` back into the source notebooks, matched by cell ID — so a quick IDE fix in the generated lib doesn't get clobbered on the next export. (This is why you must never *keep* hand-edits in `trouver/` without updating.)
2. **Git integration suite.** `nbdev-install-hooks` installs Jupyter+git hooks that auto-clean/trust notebooks and turn merge conflicts into human-readable form; `nbdev-diff` gives cell-level diffs between git refs; `nbdev-fix <nb>` rebuilds a working notebook from a conflicted one; `nbdev-merge`/`nbdev-diff-driver` are the git drivers behind it.
3. **Test flags gate slow cells.** With `tst_flags = "tst"` in your config, mark heavy cells `#| flags: tst` and run them only via `nbdev-test --flags tst` — daily test runs stay fast without deleting coverage.
4. **`watch-export`.** Re-exports changed notebooks live as you save — useful when iterating on export structure (e.g. moving a function between modules).
5. **Docs are Quarto-based now (v3).** `nbdev-docs`/`nbdev-preview` render via Quarto: native LaTeX math in docs, full-text search, and auto-hyperlinking across packages via `nbdev-index`. `nbdev-filter` is the Quarto notebook filter if you ever wire notebooks into a standalone Quarto project.
6. **`nbdev-readme`** regenerates `README.md` from `index.ipynb`; `nbdev-sidebar` (your `sidebar.yml`) and `nbdev-contributing` do the same for their files.
7. **The imports/computations rule.** Docs rendering runs import cells + exported cells + `show_doc` to keep signatures fresh — a non-exported cell mixing `import x` with other top-level code triggers the "mix of imports and computations" warning and can break/slow docs builds. Keep imports in their own cells.
8. **You already depend on `nbdev_ignore`** (in `[project] dependencies`) — third-party package for marking cells to skip; check its README for the tag syntax it uses, since it layers on top of nbdev's own directives.
9. **Release tooling exists** (out of day-to-day scope): `nbdev-bump-version`, `nbdev-pypi`, `nbdev-conda`, `nbdev-release-gh` — the last generates a changelog from closed GitHub issues and opens the release.

## Caveats for this machine

- README states nbdev "works on Windows under WSL, **not** under cmd or PowerShell" — if a command misbehaves here, that's the first thing to check (your shell is Git Bash; run nbdev commands from the environment where it's installed).
- `nbdev` isn't visible from the default `python` on this machine — invoke via whatever env your notebooks use.
