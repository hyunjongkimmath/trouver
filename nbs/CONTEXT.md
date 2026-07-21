# CONTEXT.md — Trouver Notebooks

This directory contains the nbdev source notebooks for the trouver library. These are the **source of truth** — running `nbdev_export` generates the `trouver/` Python package.

## Naming Convention

Notebooks follow the pattern `XX_module_YY.name.ipynb`:

- `XX` — Module group number (determines export path prefix)
- `YY` — Sequential order within the module
- `name` — Descriptive name of the submodule

| Prefix | Export Path | Examples |
|--------|-------------|----------|
| `01_helper_` | `trouver.helper.*` | constants, regex, files_and_folders, latex.core, date_and_time |
| `02_markdown_` | `trouver.markdown.*` | heading, obsidian.__init__ |
| `03_obsidian_` | `trouver.obsidian.*` | vault, vault_note, tags, links, footnotes |
| `04_latex_` | `trouver.latex.*` | divide, preamble, convert, formatting |
| `05_personal_vault_` | `trouver.personal_vault.*` | authors, index_notes, information_notes, trouver_vault |
| `06_notation_` | `trouver.notation.*` | parse, management, glossary |
| `07_llm_core_` | `trouver.llm_core.*` | call_llm |
| `08_machine_learning_` | `trouver.machine_learning.*` | information_note_types, notation_summarization, semantic_search |
| `09_app_` | `trouver.app.*` | gui |
| `10_shortcuts_` | `trouver.shortcuts.*` | multiple_notes |

Notebooks with double-digit prefixes that don't match the `XX_module_YY.name.ipynb` pattern (e.g., `24_markdown.obsidian.personal...`, `26_markdown.obsidian.personal...`) are experimental or migrated to `trouver_plus`.

### Special Files

| File | Purpose |
|------|---------|
| `index.ipynb` | Documentation site index page |
| `sidebar.yml`, `nbdev.yml`, `_quarto.yml` | nbdev/Quarto configuration |
| `release_notes.ipynb` | Version changelog for docs |
| `styles.css` | Custom documentation styling |
| `how_to.*.ipynb` | Tutorial/installation guides, not library code |
| `tutorial.*.ipynb` | Walkthroughs and coding-style references |
| `using_regex.ipynb` | Reference guide for regex patterns used in the library |
| `star.ipynb` | `helper.packages` — non-standard naming, minimal testing |
| `unused.ipynb` | Tutorial content marked `#| notest`; not exported to package |
| `TODO.ipynb` | Scratch pad and TODO list; exports to `todo.html`, not Python |
| `_tests/` | Shared test fixtures (sample LaTeX files, mock vault structures) |
| `images/` | Assets for documentation |

## The Ideal Notebook Structure

Well-maintained notebooks follow a consistent 5-part pattern:

1. **Raw frontmatter cell** — Markdown metadata at the very top: `title`, `description`, `output-file`. Controls documentation output and tells nbdev which module the notebook exports to.

2. **`#| default_exp` cell** — Sets the default export module for all subsequent cells (e.g., `#| default_exp helper.regex`). One per notebook, right after frontmatter.

3. **Exported imports + setup** — A `#| export` cell with public dependencies, followed by a non-exported cell for test utilities (`fastcore.test` assertions like `test_eq`, `ExceptionExpected`; `unittest.mock`; `tempfile.TemporaryDirectory`).

4. **Alternating documentation → implementation → test blocks** — The heart of each notebook:
   - A markdown cell explaining the concept or problem being solved
   - One or more `#| export` cells containing functions/classes with docstrings (parameter tables using `| param | type | description |` format)
   - Test cells that exercise the exported code, often with `#| hide` to suppress output in docs
   - `show_doc()` calls to display function signatures and docstrings for reference

5. **Examples section** — A markdown heading "## Examples" near the end, followed by realistic usage demonstrating the module's public API.

**Best examples**: `01_helper_04.regex.ipynb` (near-perfect adherence, rich per-function documentation), `03_obsidian_01.vault.ipynb` (comprehensive temp-directory tests, thorough error class coverage).

## Spectrum of Maintenance Quality

The notebooks range from fully adhering to the ideal down to bare-bones code dumps. Common deviations:

| Deviation | Description | Examples |
|-----------|-------------|----------|
| **Missing tests** | Functions marked `# TODO: test` or `# TODO: examples` — implemented but not verified | `01_helper_03.files_and_folders.ipynb`, `05_personal_vault_20.information_notes.ipynb` |
| **Sparse documentation** | Export cells with no preceding markdown explanation; docstrings missing parameter tables | `04_latex_20.convert.ipynb` (many helpers documented only by variable names) |
| **Commented-out code** | Alternative implementations or deprecated code left as comments instead of removed | `01_helper_03.files_and_folders.ipynb` (`uncompress_file`), `04_latex_20.convert.ipynb` |
| **Incomplete functions** | Export cells containing bare `return` statements or partial function signatures | `05_personal_vault_20.information_notes.ipynb` (`reference_of_information_note`) |
| **Misused cell types** | Raw markdown cells used as code cells (e.g., `#| export` in a raw cell followed by incomplete code) | `04_latex_20.convert.ipynb` (cell-18), `star.ipynb` (cell-8) |
| **Missing frontmatter** | Notebooks that use plain markdown headers instead of raw metadata cells | Several notebooks across modules |

## Nbdev Cell Flags

| Flag | Effect |
|------|--------|
| `#| export` | Includes the cell in the generated Python module |
| `#| default_exp module.name` | Sets the target module for all following exported cells |
| `#| hide` | Suppresses cell output in generated docs; code is still exported |
| `#| notest` | Skips the cell during `nbdev_test_nbs` |
| `#| eval_false` | Prevents execution entirely; useful for placeholders or environment-specific code |

Cells **without** `#| export` are executed in the notebook session but not included in the package — use for imports, fixtures, one-off examples.

## Testing Patterns

When tests are present, they follow these conventions:

- **Unit assertions**: `fastcore.test` functions (`test_eq`, `test_ne`, `test_is_not`)
- **Filesystem operations**: Wrapped in `tempfile.TemporaryDirectory()` for clean teardown
- **External dependencies**: Heavy use of `unittest.mock.patch` to isolate LLM calls and API requests
- **Fixtures**: Shared test data lives in `_tests/` — sample LaTeX files, mock vault structures

## Docstring Format

Docstrings use a custom format with parameter tables rather than standard Google/NumPy/Sphinx style:

```
| param | type | description |
|-------|------|-------------|
| x     | str  | The input   |
```

This is what `show_doc()` renders in the generated documentation.

## Coding Standards

See [`CODING_STANDARDS.md`](CODING_STANDARDS.md) — function length limits, naming conventions, testing expectations, and practices distilled from the well-maintained vs. degraded notebooks in this codebase.