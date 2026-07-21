# CONTEXT.md — Trouver

## Overview

Python library that parses LaTeX documents (e.g. from arXiv), divides them into Obsidian-compatible `.md` notes, and uses ML models to classify note types, identify definitions/notations, name them, and generate summaries. Used alongside Obsidian for mathematical note-taking.

Built with [nbdev](https://nbdev.fast.ai/) — **Jupyter notebooks are the source of truth**. The `trouver/` Python package is auto-generated and should **not be edited directly**.

## Nbdev Workflow

Run all commands from `Python/trouver/`:

| Command | What it does |
|---------|-------------|
| `nbdev_export` | Export notebooks → `trouver/*.py` |
| `nbdev_update_lib` | Sync exported lib with notebook changes |
| `nbdev_build_docs` | Build documentation site |
| `nbdev_test_nbs` | Run all notebook tests |
| `python -m nbdev.test --timing --n_workers 0` | Run tests (avoids BrokenProcessPool) |
| `python -m nbdev.doclinks` | Check export synchronization |

The `.aiexclude` file instructs AI tools to ignore `trouver/` and only read notebooks.

## Notebook Structure

Detailed notebook structure, naming conventions, cell flags, testing patterns, and maintenance quality: see [`nbs/CONTEXT.md`](nbs/CONTEXT.md).

### Module Overview

| Notebook prefix | Module | Responsibility |
|----------------|--------|---------------|
| `01_helper_*` | `helper` | LaTeX parsing helpers, regex, dates, file I/O, constants |
| `02_markdown_*` | `markdown` | Markdown heading parsing |
| `03_obsidian_*` | `obsidian` | Vault operations (notes, links, tags, footnotes, cache, CRUD) |
| `04_latex_*` | `latex` | LaTeX document division and conversion to Obsidian notes |
| `05_personal_vault_*` | `personal_vault` | Authors, index notes, references, information notes, note types |
| `06_notation_*` | `notation` | Notation parsing, management, glossary generation |
| `07_llm_core_*` | `llm_core` | LLM API calls (OpenAI, LM Studio) |
| `08_machine_learning_*` | `machine_learning` | Note type classification, def/notation identification, naming, summarization |

## Environment & Dependencies

- **Python >= 3.12** (pyproject.toml)
- Install: `pip install -e ".[dev]"` from `Python/trouver/`
- Key deps: fastai, sentence-transformers, transformers, PyQt6, weaviate-client, instructor, openai, lmstudio, numpy<2.0

## ML Models

All hosted on Hugging Face under [`hyunjongkimmath`](https://huggingface.co/hyunjongkimmath):
- `information_note_type` — excerpt type classification
- `def_and_notat_token_classification_model` — definition/notation token marking
- `definition_naming_model`, `notation_naming_model` — naming extracted definitions/notations
- `notation_summarizations_model` — notation summary generation

## GUI

Prototype PyQt6 GUI wrapping select functionalities. Build via `.github/workflows/build_gui.yaml`. Entry point: `app.py`.
