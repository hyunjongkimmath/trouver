# ML Notebook Audit — inefficiencies, factoring, cleanup

**Date:** 2026-10-20 · **Scope:** all ML-related `.ipynb` files under `Python/trouver_personal_playground/` (training notebooks, playgrounds, front_use_utility) + the already-factored `trouver` `08_machine_learning_*` nbs for reference.
**Assumption:** the auto classifier model is **likely not available** — any code path that hard-depends on it is flagged as a fragility.

Legend: 🔁 duplication · 📦 factoring opportunity (belongs in trouver/trouver_plus) · 🐢 inefficiency · 🧹 cleanup · ⚠️ auto-classifier dependency

> **Update 2026-10-21** — promoted from `_tmp/ml_notebooks_audit.md`. The ml_11
> items flagged here are now resolved: the `'ww'` example was a verbatim copy of
> the `'w'` one and, once written honestly, exposed that `LABEL_TAGS`' `'#'`
> prefixes made every `_auto/` comparison in `automatically_add_note_type_tags`
> miss (so `'ww'` removed nothing and `overwrite=None` never warned); fixed with
> `_BARE_LABEL_TAGS` plus tests for `'w'`/`'ww'`/`None` and the consolidation
> rule, and `predict_note_types`' empty docstring was filled (commits `b5334a8`,
> `a720d39`). Remaining items below are still open.

## Status

| Group | Notebooks | Status |
|---|---|---|
| `ml_training_notebooks/` | 15 | ✅ complete |
| `playgrounds/` | 11 | ✅ complete |
| front_use_utility ML (ml_data_update/*, modification playgrounds, pred_correction) | 21 | ✅ complete |
| `trouver` `08_machine_learning_*` + fastai how-to | 29 | ✅ complete |

---

## Findings

### Group 1: `ml_training_notebooks/`

**Group-level pattern:** every training notebook consumes a pre-generated CSV (`notation_summarizations.csv`, `definition_and_notation_naming.csv`, `note_division.csv`, `information_note_type_labels.csv`, `notations.csv`, `notation_identification.csv`, `notation_linking.csv`) that does **not exist in the repo** — it is produced at runtime by the front_use_utility data-gathering notebooks. The CSV columns are an **implicit contract** between two notebook groups with no shared schema definition. 📦 Define the schemas once (dataclass or documented spec in trouver) so producers and consumers can't drift.

#### `fine_tune_t5_unsupervised.ipynb`
- 📦 Vendored upstream code sits next to the notebook: `run_t5_mlm_flax.py` (a copy of HF's T5 MLM Flax example, ~880 lines) and `t5_tokenizer_model.py` (sentencepiece wrapper). Pin as dependencies or move to a `tools/` dir; as-is they rot silently against upstream.
- 📦 Corpus-prep logic is ad-hoc and local: `split_text` (chunk to 510 tokens), shuffle + `train_test_split`, JSONL export via `to_json(orient='records', lines=True)`. This "prepare corpus for CLI training" step is a candidate for a shared helper — check duplication against `mlm_training*.ipynb`.
- 🧹 Kernel-crash cells and dead explorations left in place (cells 24–26: crash output, `ValueError` traceback); commented-out alternative tokenizer approaches inline.
- 🐢 cwd-relative paths (`./math_text_corpus/...`, `./t5_small_math_base`) — notebook only runs from one directory; no path constants shared with the other notebooks.

#### `mlm_training.ipynb` (and near-identical `mlm_training_BART.ipynb`)
- 🐢 **Hardcoded foreign absolute path**: `Path('/home/hyunjong/Documents/Development/ml_data/latex_image_data')` — a Linux home path; this notebook cannot run as-is on the current Windows machine. No shared path constant.
- 🐢 **Manual resumable-batching by hand**: "I have to gather data a little at a time to prevent the kernel from crashing" — re-running cells with hand-edited `range(450, ...)`, saving `part_1..part_4`, then `concatenate_datasets`. This is exactly what `datasets.map(checkpoint_strategy=...)` / Arrow streaming does. Fragile: counts drift when the source corpus changes.
- 📦 **Corpus-building logic inline**: glob book subdirs → natsort → read page `.txt`s, merge pages <100k chars; separately glob `**/main.tex`, swallow `UnicodeDecodeError` with a print. A "build math-text corpus from books directory" helper belongs in trouver (or at least one shared module) — duplicated verbatim in `mlm_training_BART.ipynb`.
- 🔁 **Tokenizer setup repeated 3× in the same notebook** (cells 2, 33, …): load `latex_command_tokens.txt` → `add_tokens` → `resize_token_embeddings`. One function `load_math_tokenizer(checkpoint)` would do.
- 🧹 Leftover scaffolding: exploratory chunking cells that duplicate `group_texts`, kernel-crash + `FileNotFoundError` cells kept in place, commented-out GPU-memory cleanup block.

#### `upload_fastai_models_to_huggingface.ipynb`
- 🧹 One-off publishing script kept as a notebook: OS-branched paths (`C:\Users\hyunj\...` vs `/home/hyunjong/...`) + the `pathlib.PosixPath = pathlib.WindowsPath` monkeypatch hack (fastai `load_learner` quirk). Should be a 30-line CLI script, and the monkeypatch should be wrapped in one helper if fastai loading stays.
- ⚠️ **This is where the "auto classifier" lives**: fastai `.pkl` learners (`information_note_type_classification_model*.pkl`, `notation_identification_classification_model.pkl`) under `C:\Users\hyunj\Documents\Development\ml_data\`. Consumers that `load_learner` these: `note_tag_classification_pred_correction.ipynb` (3×) and the trouver `08_machine_learning` inference nbs (checked in Group 4). If the `.pkl`s are gone, all of those paths die — see ⚠️ section below.

#### `ml_training.ipynb`
- 🧹 **Kitchen-sink notebook** (~28k lines of JSON): trains *four+* different tasks in one file — note division (`note_division.csv`), information-note-type classification (labels + augmented data, fastai), notation identification, notation linking. Each task also has (or should have) its own notebook; this one is the pre-refactor monolith. Split per task, or archive it now that the task-specific notebooks exist.
- 🔁 Its `row_to_single_formatted_str`, `df_splitter`, `_merge_meta_tag` etc. are one-offs for the augmentation step — if the notebook is archived they vanish; if kept, they belong in trouver's data-prep code.

#### Remaining Group-1 notebooks (pattern-level, not cell-by-cell)
- `def_and_notat_token_training.ipynb` / `modernbert_def_and_notat_token_training.ipynb`: read raw files straight from `ml_data` (5+ path references each), define the same 4 dataset helpers twice, and end with model-eval cells that load dated local checkpoints (`models/def_notat_token_model_2025_02_04_3`, `..._modernbert_base_2025_12_27_3`). The modernbert notebook is a full re-implementation of the first on a different backbone — the *pipeline* (load → filter nontrivial labels → build attention masks/labels → train → eval) should be one parameterized function, not two 3000-line notebooks.
- `modernbert_note_linking_training.ipynb` / `modernbert_notation_linking_rag_training.ipynb`: binary pair-classification from `notation_linking.csv`; `tokenize_and_encode` defined twice in the same notebook (two variants); eval cells load dated local checkpoints.
- `notation_note_naming_training.ipynb` / `def_and_notation_naming_training.ipynb`: seq2seq naming trainers on `definition_and_notation_naming.csv`; both carry the stale `single_input` import and old Linux model paths in comments.
- `BART_training_for_unconditional_generation.ipynb`: two near-identical dataset classes (`__init__/__len__/__getitem__/apply_noise` twice, lines 43–113) — one class with a flag.
- `notation_summarization_with_context_training.ipynb`: LongT5 seq2seq trainer reading from `MATH_VAULT / '_ml_data' / 'notation_summarization_with_context'`; three competing load paths in eval cells (dated `models/..._2024_04_15`, fresh `checkpoint-6678`, commented-out old) — same comment-uncomment model-versioning pattern as `notation_summarization_training.ipynb`.
- **Count confirmed by grep:** `compute_metrics` defined in **9** notebooks, `preprocess_function` in **5** — the two strongest candidates for a single shared module (`trouver.machine_learning.training_helpers`).

### Group 2: `playgrounds/` (11 notebooks, incl. `ml_model_training_playground/`)

#### `minimal_huggingface_training_playground.ipynb`
- 🧹 Single-cell distilbert/imdb smoke test — fine as a reference, but it's the only notebook that trains on a *public* dataset; nothing to factor. Keep as the "does the HF stack work" canary.

#### `llm_playground.ipynb`
- 🔴 **Secret in source**: cell 30 contains a commented-out `login('hf_REDACTED_REVOKED')` — an HF API token committed in the notebook. Revoke/rotate it and move credentials to env vars (same pattern as `groq_api_key.txt`).
- 🔁 **Prompt text duplicated within the notebook**: the 5-rule notation-summarization instruction block appears verbatim in both the few-shot (`create_few_shot_prompt`) and zero-shot (`create_zero_shot_prompt`) cells. This prompt is the *actual system prompt* of the summarization model — it should live once, in trouver (next to `single_input_for_notation_summarization`), so training data generation and inference use identical wording.
- 🔁 `example_from_notation_note` rebuilds per-note `(text, summary)` pairs inline from vault notes — the same construction that produced `notation_summarizations.csv`. This is the third place (training nb, this playground, CSV producers) the "one notation note → training row" logic exists. 📦 One trouver function: `notation_note_to_training_row(note, vault)`.
- 🧹 Four different LLM backends explored in one notebook (LM Studio, Intel NPU + transformers pipeline, smolagents/TransformersModel, llama_index+Ollama), with kernel-crash cells and `NameError` cells kept in place. Split per backend or archive; the NPU section is machine-specific.
- 🐢 `time.sleep(1)` between streamed turns in the "model talking to itself" cell — arbitrary pacing, no justification.

#### `token_classification_playground.ipynb`
- 🧹 Canonical HF wnut_17 NER example; the *first* copy of `tokenize_and_align_labels` (word_ids → -100) and the seqeval-based `compute_metrics`. Fine as the reference NER template — but see the duplication count in `fine_tune_modern_bert_playground.ipynb`: this logic now exists in 4 notebooks.

#### `summarization_training_playground.ipynb`
- 🧹 HF billsum/T5-small example — the origin of Group 1's seq2seq `preprocess_function` variants (the "summarize: " prefix pattern). KeyboardInterrupt cell kept in place; otherwise a clean reference. Keep, and point the production summarization notebooks at it as the canonical template.

#### `huggingface_playground.ipynb`
- 🧹 **Dead exploratory code — recommend archive/delete.** Misuses `BertForSequenceClassification` as a seq2seq summarizer (custom `TextDataset` built on `encode_plus`, labels = summary token ids), and the cells show the resulting `ValueError` + CUDA OOM. It cannot work as written; nothing downstream imports from it.

#### `mlm_training_playgroup.ipynb`
- 🧹 **Filename typo**: "playgroup" — rename to `mlm_training_playground.ipynb` (check for references first).
- 🔁 Copy of HF NLP course ch7 on imdb; contains `whole_word_masking_data_collator` — the second copy (first is Group 1's `mlm_training.ipynb`). The collator + `group_texts` chunking are exactly the shared-module candidates.
- 🧹 Saves to `./models/imdb_mlm_model_2`; commented-out `push_to_hub` block left in place.

#### `ml_model_training_playground/fine_tune_t5_unsupervised_playground.ipynb`
- 🔁 HF Flax T5 tokenizer-training example on oscar (Norwegian) data; imports the vendored `t5_tokenizer_model.SentencePieceUnigramTokenizer` **from Group 1's `ml_training_notebooks/` folder** — a cross-folder import that silently breaks if either notebook moves. Same vendoring problem as Group 1's `fine_tune_t5_unsupervised.ipynb`.
- 🧹 ValueError cell (missing `decoder_input_ids`) kept; saves to `./norwegian-t5-base`.

#### `ml_model_training_playground/fine_tune_modern_bert_playground.ipynb`
- 🧹 **Unrelated C-extension experiment cells at the top** (cells 0–20: `test_module.c`, `gcc -shared`, `python3-config --includes` confusion between system py3.10 and venv py3.12, anaconda `CFLAGS` env hack) — these belong in a CPython-extension playground, not an NER notebook; they were the source of the `python3-config` path debugging and should be excised or moved.
- 🔁 **Third copy of the NER helper set**: `tokenize_and_align_labels` (word_ids → -100) + seqeval-based `compute_metrics` — same logic as `token_classification_playground.ipynb` and the two `def_and_notat_token` training notebooks. This is the strongest case for a shared `trouver.machine_learning.token_classification` module: `align_labels_to_tokens`, `seqeval_compute_metrics(label_list)`.
- 🧹 Cell 52 is a ~100-line fully commented-out duplicate of the entire pipeline above it (old batch-size variant); cell 42 keeps the `TypeError` crash from `use_iterable_datasets=True` (not a valid `TrainingArguments` kwarg).
- 🔁 The `LOCAL_MODELS`/`ONLINE_MODELS` dicts map backbone → HF repo for five backbones — useful reference data, but it's inline; if this notebook is kept as the NER template, these dicts should move to a constants module next to the shared helpers.

#### `ml_model_training_playground/` — remaining four
- `fine_tune_t5_v1_1_small_playground.ipynb`: single-cell T5-v1.1-small/cnn_dailymail seq2seq trainer — the origin of the `preprocess_function` ("summarize: " prefix + `as_target_tokenizer`) template that Group 1's summarization notebooks copy. **Bug:** `compute_metrics` calls `metric.compute(...)` but `metric = evaluate.load("rouge")` was never written — the NameError cell at the end is this crash, not a kernel issue. Fix: add the load line (or use the shared metric helper). Also uses deprecated `as_target_tokenizer()` and `evaluation_strategy=`.
- `modernbert_query_document_training_playground.ipynb`: MRPC pair-classification on ModernBERT-base — the public-dataset twin of Group 1's `notation_linking` pipeline (`preprocess_function` over sentence pairs + binary `compute_metrics`). Same deprecation warnings (`tokenizer=` kwarg, `evaluation_strategy=`); KeyboardInterrupt cell kept; **cell 9's source is truncated mid-line** (`save_pretrained("./fine_tuned_modernber`) — the save block never finished being typed.
- `sentence_transformers_fine_tuning_playground.ipynb`: four "Trial" sections (CosineSimilarityLoss/stsb on ModernBERT-base-msmarco and MiniLM → new `SentenceTransformerTrainer` API with mpnet triplets). Trial 1 and Trial 2 differ only in the added evaluator — merge into one notebook with an evaluator flag. Keep as the reference for the embedding-model side of the RAG pipeline (same backbone family as `modernbert_notation_linking_rag_training.ipynb`).
- **Group-2 summary:** these are upstream HF-course examples adapted to ModernBERT/T5. Their value is as *templates*; the pattern is that Group 1's production notebooks were copied from them and then diverged (adding vault data paths, CSV contracts, dated checkpoints) with no shared layer in between. The factoring target is therefore a `trouver.machine_learning.training_helpers` module (preprocess builders, metric functions, tokenizer-loading for the math vocabulary) that both playgrounds and production notebooks import — killing the 9× `compute_metrics` / 5× `preprocess_function` drift at the root.

### Group 3: front_use_utility ML notebooks

#### `note_tag_classification_pred_correction.ipynb`
- ⚠️ **Primary auto-classifier consumer.** Loads the fastai learner via `load_learner` with the `pathlib.PosixPath = pathlib.WindowsPath` monkeypatch, OS-branched: Windows → `information_note_type_classification_model_2024_05_29_5.pkl`, Linux → `information_note_type_classification_model.pkl` (note the *different filenames* per OS — two artifacts that must be kept in sync by hand). If the `.pkl` is absent, cell 4 crashes and nothing below runs. This is exactly the path the ⚠️ centralization recommendation covers: one trouver function returning `None`/clear error + a manual-fallback mode for this notebook (its whole purpose is cross-checking model predictions against human tags).
- 🔁 **Three near-identical disagreement functions** (`model_disagrees_with_note_marking_for_tag`, `..._note_markings`, `..._auto_note_markings`) — the only differences are tag prefix (`''` vs `_auto/`) and return shape. One function with a `tag_prefix: str` parameter replaces all three.
- 🐢 Cells 11–12 and 14–15 repeat the "all info notes" block verbatim (`all_paths_to_notes_in_vault` → `VaultNote` list → `note_is_of_type` filter) — extract to one cell/helper.
- 🔁 `label_tags` (the 10 `_meta/*` tags) hardcoded here; the same tag vocabulary lives in trouver's `information_note_types` — single source of truth needed, or a model trained on one list is checked against notes tagged with another.
- 🧹 `import winsound` (Windows-only, unused-looking); `platform`-branched vault path block duplicated from the upload notebook — candidate for a shared `get_math_vault()` helper.

#### `front_use_utility_notebooks/ml_data_update.ipynb`
- 📦 **The producer half of the Group-1 CSV contract.** Confirms the concrete schema of the notation-summarization dataset: `['notation_note_name', 'notation', 'latex_in_original', 'summary', 'main_note_name', 'processed_main_note_content', 'single_input']`, saved via `save_to_disk` to a **dated** path (`_ml_data/notation_summarization_2025_03_10`) — the consumer side (Group 1) must be pointed at the right date by hand. This is the strongest case for a shared, versioned schema + path convention in trouver.
- 🔁 **Identical "collect all notation notes" block twice** (cells 4 and 10: `all_paths_to_notes_in_vault` → filter `NOTATION_NOTE` minus the 3-name blacklist). The blacklist itself (`ml_data_definition_and_notation_in_sentence`, `_template_notation_index`, …) is a magic list that also appears in sibling notebooks.
- 🐢 **LaTeX-token vocabulary generation inline** (cells 30–34): globs `C:\Users\hyunj\Documents\Math\latex_image_data\latex` (hardcoded path *outside* the vault), regex `\\[a-zA-Z]+`, prints every file's matches. This is what produces the math-vocabulary token list Group 1's `mlm_training*.ipynb` load via `add_tokens` — a hidden producer→consumer dependency with no shared artifact name. Belongs in trouver as `gather_latex_command_tokens(tex_dir)`.
- 🧹 Kitchen-sink: three jobs in one notebook (notations.csv update [marked *deprecated*], summarization dataset build, token vocabulary), plus commented-out reference-note logic (cells 5–7) and a debug block for one specific note (`demarco_aws…`, cells 24–29).
- ⚠️ Cell 17 calls `single_input_for_notation_summarization(..., formatter=format_training_tokens)` but `format_training_tokens` is never imported/defined in the visible cells — stale reference; this cell can't run as-is.
- 🔁 The OS-branched vault-path block appears twice in this notebook alone (cells 1, 24) and once each in at least three other Group-3 notebooks — a `get_math_vault()` helper is overdue.

#### `front_use_utility_notebooks/ml_data_update/` (7 sub-notebooks; all read)

**Group-level pattern — two producer generations coexist:** the old path is *vault → CSV* (`notations.csv`, `notation_summarizations.csv`; consumed by Group 1's pandas-reading notebooks); the new path is *vault → `save_to_disk` Arrow datasets* under `_ml_data/` (consumed directly by `load_from_disk`). Both are live, with dated directory names as the only versioning. 📦 Pick one contract: a trouver module that owns (a) the schemas, (b) the `_ml_data` path convention, and (c) the producer functions — so training notebooks never hardcode dataset column names.

- **Cross-notebook kernel dependency:** `ml_data_update_notation_note_naming.ipynb` uses `MATH_VAULT`, `VaultNote`, `MarkdownFile` without importing them — it only runs if the parent `ml_data_update.ipynb` was executed first in the same kernel. Every sub-notebook should be self-contained (import its own paths); the sibling `notation_note_linking.ipynb` already does this via `trouver_plus.markdown.obsidian.personal.MATH_VAULT_LOCATION`.
- 🔁 **`reference_blacklist`** (`baum_fulton_quart`, `broberg_2004`, …) hardcoded in 3+ notebooks; the "collect `_reference*` notes → their `_index_*` notes minus blacklist" block is near-verbatim in `notation_note_linking` and `note_linking`. One trouver function: `reference_index_notes(vault, blacklist=DEFAULT_BLACKLIST)`.
- ⚠️ **Reproducibility bug — "consistent" splits are not consistent:** `split_list_consistently` uses Python's built-in `hash(note.name[7:])`, which is salted per-process (`PYTHONHASHSEED`) for strings. The train/valid split therefore *changes on every kernel restart*, defeating the stated purpose ("a reference will always be part of either the test or valid set"). Use a stable digest (`hashlib.md5(name).digest()` → int) instead. Related drift: four variants of "split list" now exist — `trouver.helper.split_list_into_chunks`, this hash-based one (multiplier `39` here, `35` in the parent's commented-out copy), and a seeded `random.sample`-based one in `notation_note_linking`.
- 🐢 **Broken error handling in the two-pass collection** (`note_linking.ipynb`): `except Exception as e: raise(e); continue` — the `continue` is unreachable, so one bad reference kills the whole gather; the kept `KeyError: '_index_achter_dcgff'` cell shows a second pass over `train_note_data` crashing on an entry the first pass silently dropped. The two-pass design (gather note data once, build both `note_linking` and `notation_summarization_with_context` datasets from it) is the right shape — fix the per-reference skip logic (`continue` without `raise`, collect failures into a list to print at the end).
- 🧹 `note_linking.ipynb` final cell references `dataset_dict` (not defined in this notebook; the variable is `ds`) — stale copy from the parent. Large fully-commented duplicate cells kept in place throughout the folder.
- ✅ What's already factored: `note_data_from_reference`, `find_reverse_links`, `get_main_note_content_of_notat_note_data`, `dataset_from_note_data(format='bert')`, `summarization_dataset_from_note_data(format='t5')` all live in `trouver.machine_learning.note_linking` — the new-generation notebooks are thin orchestrators. The remaining inline logic (reference collection, splitting, augmentation loops, save paths) is what should finish moving into trouver.

- **`ml_data_update_note_division.ipynb`:**
  - 🐢 **Latent NameError in `group_notes_linked_in_index_notes_by_references`:** the loop does `try: index_note_of_index_note = ... except: print(...)` — if `index_note_of_note(index_note)` raises, execution falls through and the next statement uses `index_note_of_index_note`, which is either unbound (first iteration) or *stale from the previous reference* (later iterations — silently wrong grouping, worse than a crash). The `except` must `continue`. Marked with a live `# TODO Check this` comment.
  - 🔁 Fourth+ copy of the format-check assertion block (`assert '# See Also' in headings`, `'# Meta'`, `'## References'`, `'## Citations and Footnotes'`) — identical to `note_type.ipynb` cell 5 and the parent's copy; belongs in a trouver `assert_information_note_format(mf)` helper.
  - 🔁 OS-branched vault-path block inline again (cell 3).
  - ✅ Uses the already-factored `append_note_split_data_to_database(file, notes, VAULT, lines_in_point=5, split_at=2)` from `trouver_plus.markdown.obsidian.personal.machine_learning.note_splitting` — a good example of the target shape for the rest of this folder.

- **`ml_data_update_note_type.ipynb`:**
  - ⚠️ **This is the producer of the auto-classifier's training data** (`_ml_data/information_note_type_labels`, via `information_note_types_as_dataset`) — so "auto classifier unavailable" means *this notebook is the only way to regenerate its weights*, and it has problems:
  - 🐢 **Broken augmentation cell (cell 14):** references `augmented_dataset` which was defined in cell 12 as `merge_augmented_dataset`/`augmented_dataset` — the saved kernel state shows a `NameError` + full kernel crash. The notebook's last successful run predates the augmentation edits; the saved `_ml_data/information_note_type_labels` (82,731 train rows) was built from whatever state existed then — provenance is unclear.
  - 🐢 **Unseeded "chunk" split (cell 9):** `random.randint(0, num_chunks - chunks_20_percent)` picks the 20% window at random on every run with no seed — a third variant of the non-reproducible-split problem (see `split_list_consistently` above).
  - 🐢 **O(n²) augmentation loop:** `for datapoint in augmented_dataset:` iterates the whole Dataset row-by-row in Python, then rebuilds it via `Dataset.from_dict` — for ~17k→82k rows this is minutes of pure overhead; a single `ds.map(augment_dataset)` replaces both the loop and the manual dict assembly.
  - 🔁 `label_tags` list hardcoded again (also in `note_tag_classification_pred_correction.ipynb`) — should come from `PersonalNoteTypeEnum` itself, which it already imports.
  - 🧹 Commented-out CSV-era cells (cell 8) kept alongside the live dataset path; `winsound.Beep` imported at top and only used in commented code; a large commented `<S`-check block (cell 7).
  - ✅ Good: uses factored `append_to_information_note_type_database` / `information_note_types_as_dataset` from `trouver.machine_learning.information_note_types`, and the augmentation primitives (`random_char_modification`, `dollar_sign_manipulation`, …) already live in `trouver.helper.latex`.

- **`ml_data_update_def_and_notat_token_classification.ipynb`** (largest producer; ~72k train rows → `_ml_data/def_and_notat_data_modernbert_base_4096_2025_12_27`):
  - ✅ **Contains the *fixed* split:** `get_stable_hash_modulo` (hashlib.md5) + `split_list_consistently` with an explicit comment "Do NOT use Python's built-in hash(), it is randomized per-session" — this is the version every other notebook should copy; the old salted-hash version is kept commented right below.
  - 🐢 **Copy-paste bug (cell 11):** the `valid_notes` loop's `except` prints `train_note.name` — failures in valid gathering are attributed to a train note.
  - 🐢 **Operator-precedence bug (cell 23):** `if type_of_note(...) in [A or B]:` — Python's `or` collapses the list to `[STANDARD_INFORMATION_NOTE]`, so `NOTATION_NOTE`-indexed index notes are silently never admitted. Should be `in (A, B)`.
  - 📦 **Large inline policy block (cell 27):** `admit_main_note_by_verified_notations/definitions` + ratio thresholds (`<= 0.3`, count `>= 1`) — data-admission *policy* living in a notebook; belongs in trouver next to `html_data_from_note`.
  - 🔁 The augmentation loop (raw + `extend(augment_html_data(...))`) appears 3× with **different ratios** (cell 13: ratio 3.00, cell 35: 4.00, cell 49: 4×) — the train set's clean/augmented composition is a moving target across runs; one `augment_html_data_list(data, ratio)` helper.
  - 🐢 **Pickle round-trips through cwd** (`temp_train_html_data`, `temp_valid_html_data`) to survive kernel restarts, with sizes tracked in comments (`#previous: 53308`) — no versioning, easy to mix generations; a `save_to_disk` checkpoint would be atomic and inspectable.
  - 🐢 **Compendium .tex pipeline (cells 45–49):** hardcoded path to a *second* vault (`C:\Users\hyunj\Documents\Obsidian\Chores\math\_writing`), a from-scratch regex environment extractor with `regex`-library fallback, and inline `\hl*/\TODO/\CrefIfExists` LaTeX cleaning — all of it producer logic that should be a trouver module (`gather_tex_environment_data(root, exclude)`).
  - 🐢 **In-place schema migration (cell 56):** renames `'tag_data'` → `'tags'` on gathered data because the producers emit both shapes — `html_data_from_note` vs. the tex pipeline disagree on the field name; fix at the source.
  - 🔁 `reference_blacklist` hardcoded again (cell 4); format-check assertion block ×2 more (cells 8, 33).
  - 🧹 `label2id` for the NER labels (`O/B-definition/I-definition/B-notation/I-notation`) is inlined here *and* in Group 1's token-classification training notebooks — one shared constant.

- **`ml_data_update_def_and_notat_naming.ipynb`:**
  - ✅ Best-behaved producer: imports the vault path from `trouver_plus`, uses factored `def_notat_naming_data_from_information_note` + `augment_def_and_notat_naming_data` (`trouver.machine_learning.definition_and_notation_naming`).
  - 🐢 **Same unbound-variable anti-pattern as `note_division`:** cell 12's `try: data_from_note = ... except: print(note.name)` leaves `data_from_note` unbound/stale on failure — first failing note raises NameError, later ones silently append *previous* note's rows.
  - 📦 **~150-line "consolidate new dataset based on old splitting" section (cells 18–33) exists *only because the split was random** (`split_list_into_chunks` in cell 11): to fine-tune an old model on regenerated data, it re-derives train/valid membership by difflib text-similarity against the old dataset, then sanitizes leakage (2,256 rows moved), then runs **two near-duplicate integrity checkers** (cells 29 and 31 — same idea, different min-length guards 10 vs 20) plus a commented-out third (cell 32). With the hashlib-based `split_list_consistently` (from its sibling notebook above), this entire section is deleted. Strongest concrete payoff for the stable-split fix.
  - 🐢 `get_source_indices` assumes "every 4th row is the source" — the augmentation ratio is hardcoded into the analysis code; breaks silently if augmentation count changes.
  - 🔁 Two different `normalize_text` definitions in one notebook (`re.sub(r'\s+','',...)` vs `" ".join(text.split())`) with different semantics feeding "equivalent" checks.
  - 🧹 Crashed cells kept in place (cells 16–17: `NameError: name 'data' is not defined`); `exclude_paths_containing` list hardcoded again (identical to `note_type.ipynb`).

#### `front_use_utility_notebooks/ml_modification_playground/` (9 notebooks — all read)

Notebooks that *apply* ML/LLM output back into the vault (the "modification" layer).

- **`typo_checking_playground.ipynb`:**
  - 🔴 API key loaded from plaintext `groq_api_key.txt` sitting next to the notebook (no env var); a LAN LLM endpoint is hardcoded (`http://192.168.127.189:1234/v1`, `api_key="not-needed"`).
  - 🧹 Three LLM backends tried inline (lmstudio → groq → raw OpenAI client) with the crashed LMStudio traceback saved in outputs; model selection is a comment-swap (`# model_obj=model, # model_obj=groq_client, model_obj=client`). One `get_llm_client(backend)` helper.
  - ✅ Core logic is factored: `run_vault_audit`, `audit_text_for_typos`, `typo_audit_log_message`, `FIND_LATEX_TYPOS_SYSTEM_PROPT` from `trouver.machine_learning.llm_typo_finding`.
  - 🧹 Debug cell (`import os; os.path.exists`); audit targets hardcoded as a checklist string for one reference (`fulton_it`); external path `C:\Users\hyunj\Documents\Math\latex_image_data\latex\_archive` inline again (same tree as the LaTeX-token vocabulary producer).

- **`divide_note_playground.ipynb`:** ⚠️ auto-classifier consumer.
  - ⚠️ **The saved output shows the fastai `.pkl` is no longer loadable at all:** `load_learner` on `ml_data/note_splitting/note_splitting_classification_model.pkl` fails under current fastai — "attempted to import from `fastcore.dispatch`/`fastcore.transform` which are deprecated in fastai>=2.8.0 … Downgrade to fastai<2.8.0". So the "auto classifier unavailable" assumption is understated: the pickles are *actively broken* against the installed fastai, and the fix (downgrade vs re-export) is a decision this notebook forces on every user.
  - 🔁 OS-branched vault path block again (now 3-way incl. Darwin) — the `get_math_vault()` helper is needed in at least 6 notebooks.
  - 🧹 Two competing targeting modes inlined, first assignment overwritten by the second (`index_notes = notes_linked_in_note(...)` then immediately `notes_from_links_in_text(...)`); `winsound.Beep` completion signal; live `# TODO: fix citations and footnotes being added wrong`.
  - ✅ Uses factored `automatically_split_notes(index_note, VAULT, model, template_note)` from `trouver_plus.…note_splitting` — the model is passed in as a parameter, which is exactly the seam a central "load or None" helper should plug into.

- **`link_notes_modification_playground.ipynb`:** (HF-hosted model `hyunjongkimmath/note_linking_classifier_modernbert` — *not* affected by the fastai-pickle breakage)
  - 📦 **~100-line `RemoteModernBERT` proxy class defined inline** (and a near-identical earlier version kept fully commented above it): a `torch.nn.Module` wrapping an HTTP endpoint that fakes HF's `ModelOutput`/`.config`/`.framework` so `MultiLabelPipeline` accepts it. This is production-grade code living in a playground notebook — promote to `trouver.machine_learning.remote_model`.
  - 🔴 LAN endpoint hardcoded (`http://192.168.127.189:8000`); the same machine appears in `typo_checking` on port 1234 — one `llm_endpoints` config, not literals.
  - 🐢 **Per-link-type threshold dict hardcoded inline** (`INFO_TO_INFO_IN_CONTENT: 0.5`, … 7 entries) — model-tuning policy that should sit next to the pipeline/model load, and be comparable across runs.
  - 🧹 `origin_notes` assigned twice (first assignment dead); debug cells (`origin_note.name`, `origin_notes[2:]`); a large commented-out block implementing an *older* linking algorithm that calls functions no longer imported in this notebook (`consolidate_note_linking_predictions_into_cache`, `similar_notat_notes_in_note`); `winsound.Beep` per-note and at end.
  - ✅ Core loop is factored: `note_data_from_reference`, `sieve_potential_relied_notes`, `predict_on_relied_notes_and_related_notat_notes`, cache parse/write/remove functions all from `trouver.machine_learning.note_linking`.

- **`def_and_notat_identification_playground.ipynb`:** (HF-hosted `hyunjongkimmath/def_and_notat_token_classification_model_modernbert_base` — *not* affected by the fastai-pickle breakage)
  - 📦 **~150-line `NEW_DEF_NOTAT_VERIFY_SYSTEM_PROMPT` inlined in a cell**, under active iteration: the notebook runs LLM audits on flagged notes, collects failures into a manifest, then builds a mega-prompt ("re-write the system prompt to identify FUNDAMENTAL problems") and copies it to the clipboard for manual prompt engineering. This is a live prompt-tuning workflow whose artifact (the prompt) belongs in a module constant next to `FIND_LATEX_TYPOS_SYSTEM_PROPT` (e.g. `trouver.machine_learning.def_notat_audit_prompts`) so the version history lives somewhere diffable, not in notebook cells.
  - 📦 The "assess the system prompt" loop itself (manifest → tally → mega-prompt → clipboard) is a reusable LLM-eval harness existing only inline; `AuditLogger` (trivial callable class) defined per-notebook.
  - 🔁 The same index-note → subvault-relative-notes boilerplate (with its "speed-up on re-run" comment) is copy-pasted **3× within this one notebook** (cells 10/15/27), each with a pile of commented-out targeting variants; the subvault trick deserves a `notes_for_reference(reference, VAULT)` helper.
  - 🔴 LAN LLM endpoint hardcoded again (`http://127.0.0.1:1234/v1`, LM Studio via raw OpenAI client).
  - 🧹 `winsound.Beep` per-note and at end; saved `NameError` output (`canndidate_notes`); `pyperclip.copy` used as the **data bus between cells** (three separate clipboard hand-offs: `total_log`, `total_copy`, sampled texts) — fragile and invisible to any downstream consumer; `'typo' in str(mf)` as a skip heuristic (raw substring match on file content).
  - ✅ Core logic is well factored: `auto_mark_def_and_notats`, `convert_double_asterisks_to_html_tags`, `predict_and_mark_def_and_notats`, `latex_highlight_formatter`, `run_audit_voting_maker`/`AuditVoteResult` all from `trouver.machine_learning.tokenize.def_and_notat_token_classification`.

- **`name_def_and_notat_create_notat_notes_glossary_playground.ipynb`:** the pipeline *orchestrator* (naming → create notation notes → glossary); mostly thin calls over factored functions.
  - ✅ Best-factored of the modification layer: `add_names_to_html_tags_in_info_note`, `get_all_linked_info_notes`, `get_accumulated_context_for_notes`, `fix_notation_name_syntax_in_HTML_tags`/`fix_notation_syntax_in_notation_note`, `make_notation_notes_from_HTML_tags`, `remove_bad_notation_notes`, `reorder_notation_note_links_in_see_also_section`, `create_glossary_for_index_note` — all from trouver. The glossary section is a single clean call.
  - 📦 **Two HF Seq2Seq naming models loaded inline in duplicate** (`definition_naming_model`, `notation_naming_model`), with a commented-out local-`ml_data` variant that needs the `pathlib.PosixPath = pathlib.WindowsPath` monkeypatch — a third copy of OS-branched model loading. One `load_naming_models(backend)` helper would cover all three copies (HF, local HF-format folder, fastai pickle).
  - 📦 LLM backend for definition naming selected inline again: `import lmstudio as lms; model = lms.llm("mistralai/mistral-small-3.2")` with `lms.set_sync_api_timeout(3600)`, plus a commented raw-OpenAI variant — the 4th distinct backend-selection pattern across these playgrounds (LMStudio lib, LMStudio via OpenAI client, Groq, LAN IP).
  - 🔁 The index-note → subvault boilerplate is copy-pasted **4× within this one notebook** (naming / syntax-fix / create-notation-notes / glossary sections), each with its own `reference` checkpoint cell and pile of commented targeting variants.
  - 🧹 `if False: continue` guard left live; `winsound.Beep` per-note + at end; the syntax-fix section still prints "Naming defs and notations" (copy-paste residue); `replace_bad_notes` flag gates a full-subvault `all_links_in_vault(backlinks=True)` recompute — incremental re-runs must choose between full recompute and skipping cleanup.

- **`name_notat_notes_playground.ipynb`:** (small, single-purpose: name notation notes via Seq2Seq pipeline)
  - 📦 Local `ml_data` model load with OS branch + `pathlib.PosixPath = pathlib.WindowsPath` monkeypatch — the **4th copy** of this pattern (`notation_note_naming_model_2024_09_04_8`).
  - 🐢 Saved warnings show silent input-length problems: "Token indices sequence length … longer than the specified maximum (917 > 512). Running this sequence through the model will result in indexing errors" plus repeated `max_length=200` summarizer warnings — long notation notes get truncated naming with no guard; a pre-check on token length (skip/flag) is missing.
  - ✅ Core is factored: `predict_name_and_add_to_notation_note`, and the fallback trio `autogen_name_from_notation_note` / `sanitize_autogen_name` / `add_autogen_name_to_notation_note` is imported — a model-less path already exists in trouver, which matters if the HF/local models go unavailable.
  - 🔁/🧹 Same import block (≈40 lines) and index-note → subvault boilerplate as every sibling notebook; `winsound.Beep`; commented targeting variants.

- **`summarize_notation_playground.ipynb`:** two summarizer generations coexist in one notebook — (a) HF Seq2Seq `notation_summarizations_model` pipeline → `append_summary_to_notation_note`; (b) LLM via LM Studio (`lms.llm("qwen3.5-122b-a10b")`, comment-swap model selection, plus raw OpenAI client at LAN `http://192.168.127.189:1234/v1`) → `generate_notation_summary` + `_write_summary_to_notation_note`.
  - 🐢 **Saved output shows the LLM wrote corrupted LaTeX into vault notes**: the `summary` field contains `\operatornamen{Gal}`, `\langles\eigma`, broken escapes (`K^^\times n`). No post-hoc validation that a generated summary is parseable LaTeX before `_write_summary_to_notation_note` — this is data corruption of the highest-value derived notes.
  - 🧹 `config` dict with **duplicated snake/camelCase keys** (`repeat_penalty`/`repeatPenalty`, `presence_penalty`/`presencePenalty`) defined but never passed to `generate_notation_summary` (dead code); `max_context = 8192` with a commented reference to an undefined `SYSTEM_PROMPT`; saved `NameError` from a pasted-in `if __name__ == "__main__"` usage-example cell.
  - 📦 Notebook reaches into trouver **private** functions (`_summary_should_be_generated`, `_get_summary`, `_write_summary_to_notation_note`, `format_training_tokens`) — they're de facto public API; promote or expose deliberately.
  - 📦/🧹 Final cell is a misplaced data-collection utility: `sample_and_combine` walks an *external* tree (`C:\Users\hyunj\Documents\Math\latex_image_data\latex\SGA` — the third notebook to hardcode this path), unseeded `random.random()` sampling at 1%, writes `combined_sample.txt` to cwd. Prompt-engineering material gathering that doesn't belong in a summarization notebook; belongs with the other data-collection cells (cf. typo_checking, def_and_notat producer).
  - ✅ Core is factored: `append_summary_to_notation_note`, `notation_note_should_be_summarized`, `generate_notation_summary`, `example_from_notation_note` all from trouver.

- **`tag_note_type_modification_playground.ipynb`:** ⚠️ primary auto-classifier consumer — and the notebook where the fastai breakage is being fought.
  - 📦 **Inline `sys.modules` shim for the fastai≥2.8.0 breakage**: cell 1 redirects `fastcore.transform`/`fastcore.dispatch` to the new `fasttransform` package (fallback: `fastcore.basics`), with a "Run this in your terminal: pip install fasttransform" comment. This is *the* fix for the divide_note pickle failures — it should be one `load_fastai_learner(path)` helper in trouver_plus, not ad-hoc sys.modules surgery per notebook (and the fallback-to-`fastcore.basics` branch silently loads the wrong module if `fasttransform` isn't installed).
  - 📦 **Five learners loaded on every run** (Windows branch): `information_note_type_classification_model.pkl`, `_2024_10_22_3.pkl`, `focused_information_note_type_classification_model_2024_12_12.pkl`, HF-hosted `from_pretrained_fastai('hyunjongkimmath/information_note_type')`, and a 5th `context_model` from `_2024_05_29_5.pkl` (Linux branch loads only one). Multiple generations of the same classifier coexist with no record of which is canonical; only one list is actually used per run.
  - 🧹 The `overwrite=` semantics are documented in a ~6-line notebook comment instead of the function docstring; `compare_predictions` flag gates an inline model-disagreement diff with **hardcoded tag-subtraction sets** (`#_meta/TODO/merge`, `#_meta/hint`, …) — the same "models disagree" pattern as `note_tag_classification_pred_correction.ipynb`'s three near-identical functions; `pyperclip.copy` as the message bus again.
  - ✅ Core is factored: `automatically_add_note_type_tags`, `predict_note_types` from `trouver.machine_learning.information_note_types`.

- **`context_extraction_playground.ipynb`:** cleanest notebook in the folder — one factored call, `create_context_extraction_for_index_note(index_note, model, max_context=8192, verbose=True)` (model passed as a parameter: same seam as divide_note for a central client helper), plus `process_multiple_notes` for multi-note text assembly.
  - 📦 LLM backend selected inline again — the **5th distinct pattern** across these playgrounds: `lms.llm("qwen3.5-122b-a10b")` + `lms.set_sync_api_timeout(3600)`, with a commented-out Groq client (the only notebook here that reads `GROQ_API_KEY` from an env var) and a commented groq config (`openai/gpt-oss-120b`).
  - 🧹 Debug cell (`inspect.signature(...)` dump); two consecutive runs (ellenberg, bredon) each with their own copy-pasted try/finally `winsound.Beep` block; the shared ≈40-line import boilerplate again.

#### `Python/trouver/nbs/` — `08_machine_learning_*` (28 nbs) + `how_to.train_ml_model.fastai.ipynb`

- **`08_11.information_note_types_predict`** (read in full):
  - ⚠️ **Hard fastai import in the export chain**: an exported cell does `from fastai.text.learner import TextLearner`. If fastai is broken/removed, the *entire* `trouver.machine_learning.information_note_types` module becomes unimportable — not just learner loading. This taints every consumer that imports trouver's ML package at all.
  - ✅ Best seam in the set: library functions take learners as parameters (`predict_text_types_with_one_learner`, `consolidate_single_text_predictions_by_sum_of_confidence` — sums p−(1−p) across learners, `predict_note_types` with consolidation callback, `automatically_add_note_type_tags`, `convert_auto_tags_to_regular_tags_in_notes`). The canonical OS-branch + PosixPath-monkeypatch model-load cell (`#| notest #| hide`) lives here — it is the source every playground copy-pasted.
  - 🧹 Doc bug: the 'ww' example cell carries `# TODO: change example` and actually passes `overwrite='w'`, so the docs demonstrate single-char overwrite mode; `predict_note_types` has an empty docstring.

- **`how_to.train_ml_model.fastai.ipynb`** (read in full) — the canonical training recipe for the auto classifier:
  - ⚠️ ULMFiT recipe (`language_model_learner(dls_lm, AWD_LSTM, drop_mult=0.3)` → freeze loop → `text_classifier_learner(..., drop_mult=0.5)`, both `.to_fp16()`) exists only as notebook cells, not factored into any function — every future retrain re-derives it by hand.
  - 🐢 **Seedless split in the canonical recipe**: `TrainTestSplitter(test_size=0.2, random_state=None)` + `dataloaders(df, bs=32, seed=None)` — non-reproducible train/valid; same disease as the PYTHONHASHSEED problem in the HF pipeline (the fixed stable-hash split exists only in one playground notebook).
  - 🐢 Fragile positional label extraction: `label_cols = list(df.columns[5:-1])` with "Change the indices here if the labels change".
  - 🧹 Most actual training cells commented out; untested weight-resume paths (`# TODO: test the below code`, `# TODO: think about how to set up vocab`); blanket `warnings.filterwarnings("ignore")`.
  - ⚠️ Forward risk: the recipe depends on `AWD_LSTM`/`language_model_learner` from `fastai.text.all`, whose availability under fastai≥2.8.0 is unverified — the same version jump that broke pickle loading will likely break retraining too.

- **`08_24.tokenize.def_and_notat_token_classification_llm_verification`** (read in full):
  - ✅ Best-tested notebook of the set (mock-based tests for salvage/voting/MAKER); `client` passed as a parameter — good seam.
  - 📦 Exports the canonical ~150-line `DEF_NOTAT_VERIFY_SYSTEM_PROMPT` into `machine_learning.tokenize.def_and_notat_token_classification` — yet the def_and_notat_identification playground carries its own inline copy of an equivalent prompt with a live prompt-tuning workflow attached. The playground should import the canonical prompt, not re-inline it (the two are now diverging).
  - 🐢 Bug: `run_strict_audit(..., max_tokens=1024)` accepts the parameter but hardcodes `max_tokens=1024` in the client call — the parameter is dead.
  - 🔴 LAN endpoint `http://127.0.0.1:1234/v1`, `api_key="lm-studio"` in a `#| notest` cell + one plain commented cell.

- **Grep map across the remaining 08 nbs** (fastai / LLM-backend patterns):
  - Only `08_11` imports `load_learner`; **no fastcore.transform shim anywhere in trouver's nbs** — the fix for the ≥2.8.0 breakage exists only inline in one playground notebook.
  - `08_35.definition_and_notation_naming`: the only place a backend abstraction exists — duck-typed strategy factory (`is_lmstudio = hasattr(model, 'respond')` / `is_openai`). This is the pattern to generalize into the central client helper.
  - `08_26`/`08_80` import lmstudio; `08_25` mocks `sys.modules['transformers']` (test-only).

### ⚠️ Auto-classifier availability (cross-group)

The fastai text classifiers in `ml_data/` (`information_note_type`, `notation_identification`) are the "auto classifier". Hard dependencies found so far:
- `note_tag_classification_pred_correction.ipynb` — loads them via `load_learner` (3×); its entire purpose is correcting their predictions.
- **Confirmed in Group 4:** the dependency is in trouver's *import chain*, not just in consumers — `08_11.information_note_types_predict` has an exported cell doing `from fastai.text.learner import TextLearner`, so a broken/missing fastai makes the whole `trouver.machine_learning` package unimportable.
- ⚠️ **The pickles are actively unloadable under current fastai (≥2.8.0)**: saved outputs in `divide_note_playground.ipynb` show `load_learner` failing with "attempted to import from `fastcore.dispatch` and/or `fastcore.transform` which are deprecated in fastai>=2.8.0 … Downgrade to fastai<2.8.0" (modules moved to the `fasttransform` package). The fix already exists inline in `tag_note_type_modification_playground.ipynb` cell 1 (`sys.modules['fastcore.transform'] = fasttransform`, fallback `fastcore.basics`) — it should be promoted into a single guarded helper, not kept as ad-hoc `sys.modules` surgery.
- **Recommendation:** centralize classifier loading in one trouver function that (a) applies the fasttransform shim, (b) returns `None`/raises a clear error when the `.pkl` is absent or fastai is unavailable — so every consumer gets a uniform "classifier unavailable" path instead of an opaque `load_learner` crash; downstream workflows (tagging, vault modification) need an explicit manual/no-op fallback.

---

## Cross-group synthesis

### Duplication inventory (cross-notebook)
- 🔁 `def_and_notat_token_training.ipynb` ↔ `modernbert_def_and_notat_token_training.ipynb`: identical helper set (`pick_out_datapoints_with_nontrivial_labels`, `attention_mask_list_for_dataset`, `label_list_for_dataset`, `input_id_list_for_dataset`) — the modernbert one is a re-skin of the same token-classification pipeline on a different model.
- 🔁 `mlm_training.ipynb` ↔ `mlm_training_BART.ipynb`: identical `tokenized_dict`, `group_texts`, `whole_word_masking_data_collator`.
- 🔁 `compute_metrics` redefined in ≥7 notebooks (each a slight variant); `preprocess_function` in ≥6.
- ⚠️ **Broken/stale imports** — `single_input` is imported from *both* `trouver.machine_learning.notation_summarization` and `trouver.markdown.obsidian.personal.machine_learning.notation_summarization`. Verified: only the former exists, and it defines `single_input_for_notation_summarization`, **not** `single_input`. So `from ... import single_input` (in `BART_training_for_unconditional_generation.ipynb` and `notation_note_naming_training.ipynb`) is dead — those cells can't have run since the rename. A module move + function rename were done without updating consumers.
- 🔁 ~40-line import boilerplate + OS-branched VAULT block copy-pasted across all modification playgrounds; the PosixPath-monkeypatch model-load cell (canonical in `08_11`) re-inlined in ≥4 places.
- 🔁 Canonical `DEF_NOTAT_VERIFY_SYSTEM_PROMPT` exported by `08_24`, re-inlined (diverged) in the def_and_notat_identification playground.
- 🔁 Model-disagreement diff with hardcoded tag-subtraction sets: `note_tag_classification_pred_correction.ipynb` (3 near-identical functions) + `tag_note_type_modification`'s `compare_predictions`.

### Top factoring targets (recommended order)
1. **`load_fastai_learner(path)`** — fasttransform shim + OS branch + PosixPath monkeypatch + clear "unavailable" error, and remove the exported `from fastai.text.learner import TextLearner` from `08_11`'s import chain. Highest leverage given the auto-classifier assumption: kills 5× inline loads, the divide_note failures, and the package-wide import hazard in one move.
2. **`get_llm_client()`** (trouver_plus) — one env-var-driven place for LM Studio vs LAN-OpenAI vs Groq selection, generalizing the duck-typed strategy factory in `08_35`. Replaces 5 inline backend patterns and the scattered LAN endpoints/keys.
3. **`trouver.machine_learning.training_helpers`** — per-task `compute_metrics`/`preprocess_function`/label helpers shared by the training notebooks; pin the CSV schemas as dataclasses so producers (front_use_utility) and consumers (training nbs) can't drift.
4. **Stable-hash split** — promote `get_stable_hash_modulo` (already in the def_and_notat_token_classification playground, proven necessary by the ~150-line consolidation section in def_and_notat_naming) into trouver; use it in the canonical fastai recipe and all HF pipelines; seed the how_to.train_ml_model.fastai splitter (`random_state=None`, `seed=None` today).
5. **`RemoteModernBERT` proxy** → `trouver.machine_learning.remote_model` — production-grade class (fakes HF ModelOutput/.config/.framework for MultiLabelPipeline) currently living in a notebook with a near-identical commented duplicate.
6. **Vault boilerplate helper** — VAULT resolution + winsound/pyperclip conveniences, so playgrounds stop re-pasting the OS-branched block.

### Cleanup priorities
- 🔴 **Secrets**: HF token saved in `llm_playground` outputs; `groq_api_key.txt` plaintext next to typo_checking — move to env vars and scrub the saved outputs.
- 🐢 **Silent data corruption**: LLM summaries with corrupted LaTeX (`\operatornamen{Gal}`, `\langles\eigma`) written into vault notes by summarize_notation — add validation before `_write_summary_to_notation_note`; token-length guard for the naming model (saved warnings show 917 > 512 truncation).
- 🧹 **Dead cells**: `single_input` imports, `if False: continue`, kernel-crash cells, commented-out training runs (`how_to.train_ml_model.fastai`), the 'ww' doc example bug in `08_11`; find-and-remove the dead config dict (duplicated snake/camelCase keys) in summarize_notation.
- 🧹 **Dead parameter**: `run_strict_audit(max_tokens=...)` in `08_24` — accepted but ignored (hardcoded 1024).
