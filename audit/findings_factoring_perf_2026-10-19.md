# Factoring & Performance Audit — `trouver\nbs`

**Purpose:** exact factor-out and performance changes across the 101 notebooks. Each item states the current excerpt, the change, and why.

**Method:** scanner `_nbdev_development/spec_checkers/check_dupes_perf.py` (full report: re-run it); every Tier A item below verified by reading both copies.

---

## 1. Factor-out candidates

### A1 — `helper.packages` is exported by TWO notebooks (nbdev module collision) ⚠️ most serious

**Current:** both `01_helper_10.packages.ipynb` and `star.ipynb` contain `#| default_exp helper.packages`, and `star.ipynb` re-defines all four functions identically, e.g.:

```python
# star.ipynb (and 01_helper_10.packages.ipynb), both "#| export"
def check_package_installed(package_name: str) -> bool:
    if importlib.util.find_spec(package_name) is not None:
        return True
    else:
        return False
# + install_package, ensure_package_installed, check_package_version_with_version_attribute
```

Consumers import the generated module: `09_app_00_gui.ipynb` → `from trouver.helper.packages import ensure_package_installed, …`.

**Change:** retire `star.ipynb`'s function cells (or the whole notebook — `nbs/CONTEXT.md` already flags it as "non-standard naming"); `01_helper_10.packages.ipynb` becomes the sole exporter of `trouver/helper/packages.py`.

**Why:** two notebooks writing one generated file is last-processed-wins nondeterminism, not just duplication — a fix in one copy silently vanishes on the next export.

### A2 — `is_number` duplicated verbatim

**Current:** identical body in `01_helper_09.numbers.ipynb:58` and `04_latex_15.formatting.ipynb:82`:

```python
def is_number(x: Union[float, int, complex, str]) -> bool:
    if isinstance(x, (float, int, complex)):
        return True
    if x is None:
        return False
    if x and x[0] == '-': x = x[1:]
    return x.replace(".", "1", 1).isdigit()
```

**Change:** delete the def in `04_latex_15.formatting`; add `from trouver.helper.numbers import is_number` to its import cell (first confirm no *other* notebook imports it from `trouver.latex.formatting`).

**Why:** one tested copy (`helper_09` has the assert suite) instead of two that can drift; the `x.replace(".", "1", 1).isdigit()` trick is subtle enough that a second copy invites divergence.

### A3 — `create_method` lambda factory ×3

**Current:** identical in `08_ml_15.tokenize…classification`, `08_ml_25.notation_summarization`, `08_ml_35.definition_and_notation_naming`:

```python
def create_method(method, p, scale):
    return lambda x: method(x, p=p*scale)
```

**Change:** define once in `01_helper_28.latex.augment` (home of `augment_text`, which these all call); the three ML notebooks import it.

**Why:** it's the closure factory for the augmentation pipeline; if the `p=p*scale` scaling rule changes, three copies must change in lockstep.

### A4 — markdown-link extractors duplicated between `note_data` and `notation_linking`

**Current:** identical in `08_ml_50.note_data.ipynb:1158` and `08_ml_70.notation_linking.ipynb`:

```python
def _linked_note_names_from_content(content: str) -> list[str]:
    linked_note_names = []
    for match in re.findall(MARKDOWNLINK_CAPTURE_PATTERN, content):
        link_name = match[1]
        if link_name.endswith('.md'):
            link_name = link_name[:-3]
        linked_note_names.append(link_name)
    return linked_note_names
# + _linked_notat_note_names_from_content (same shape)
```

**Change:** keep in `note_data`, drop the underscore (it becomes cross-module API), and in `notation_linking` replace both defs with:

```python
from trouver.machine_learning.note_data import (
    linked_note_names_from_content, linked_notat_note_names_from_content)
```

(`notation_linking` already imports from `trouver.machine_learning.*`, so this fits the existing pattern.)

**Why:** link-parsing is exactly the logic that changes when Obsidian's link syntax edge cases are discovered; two copies = two bug-fix sites.

### A5 — `make_example_vault` fixture builder ×2

**Current:** identical in `03_obsidian_40.file.ipynb` and `03_obsidian_49.file_write.ipynb:207`:

```python
def make_example_vault(temp_dir: PathLike):
    temp_dir = Path(temp_dir)
    os.mkdir(temp_dir / 'algebraic_geometry')
    os.mkdir(temp_dir / 'algebraic_geometry' / 'a1_homotopy_theory')
    # … nested tree + note files
```

**Change:** keep in `03_obsidian_40.file`; delete from `03_obsidian_49` (its import cell already has `from trouver.obsidian.file import …` — just add the name). Longer-term, per `testing.md` ("fixture data lives in `_tests/`"), move the builder next to `_test_directory` in `trouver.helper.tests`.

**Why:** test fixture that must stay in sync with what the tests assert about the tree shape.

### A6 — `MockTokenizer`/`MockPipeline` duplicated (test mocks, not production)

**Current:** identical mock classes in test cells of `08_ml_21.…_mark` and `08_ml_22.…_main_workflow`:

```python
class MockPipeline:
    """Mocks the TokenClassificationPipeline."""
    def __init__(self, preds):
        self.tokenizer = MockTokenizer()
        self._preds = preds
    def __call__(self, text):
        return self._preds
```

**Change:** move both mocks to `trouver.helper.tests` (already hosts `_test_directory`, imported by test cells across notebooks); import in ml_21/ml_22. Same treatment for `mock_note_data` (ml_60 vs ml_64, Tier B).

**Why:** (initial guess of a production-class split was wrong on verification — these are test doubles; the fix is shared test helpers, cheaper than A4.)

### Tier B — name collisions to eyeball (not verified as dupes)

| Name | Locations | Check |
|---|---|---|
| `from_note` | `03_obsidian_01.vault`, `08_ml_50.note_data` | same contract? import if so |
| `_split_text_by_html_data_parts` | `08_ml_15`, `08_ml_35` | private + same name in two ML nbs → likely copy |
| `make_tag` | `06_notation_10_management`, `06_notation_15.glossary` | compare bodies |
| `mock_note_data` | `08_ml_60.…sieve`, `08_ml_64.…augmentation` | → `helper.tests` with A6 |

Excluded false positive: `path`/`exists`/`create` in `08_ml_35` are a test mock class, not a reimplementation of `03_obsidian_08.vault_path`.

## 2. Performance opportunities

### 2.1 Fuzzy-similarity hot path (biggest runtime win)

**Current:** `01_helper_02.init.ipynb:371` — slides the shorter string over the longer, full Levenshtein DP per window:

```python
for i in range(len2 - len1 + 1):          # ~len2 windows
    substring = s2[i:i+len1]
    d = [[0] * (len1 + 1) for _ in range(2)]
    for j in range(1, len1 + 1):
        ...                                # O(len1^2) DP per window
```

Called per pair from `08_ml_67.note_linking_vault_operations.ipynb:81`:

```python
for notation_note in notation_notes:              # every notation note
    notation = notation_in_note(notation_note, include_dollar_signs=False)
    for latex_text in latex_texts_in_origin_note:  # every $…$ snippet in origin
        if latex_str_is_likely_in_latex_str(notation, latex_text, threshold=threshold):
```

and `latex_texts_in_origin_note` is re-derived (`origin_note.text()` + `latex_indices`) on **every call** — `sieve_potential_relied_notes` calls this across many origin notes.

**Change (three parts):**
1. `@lru_cache(maxsize=4096)` on `partial_ratio_with_alphabet` — pure str→float, and the same (notation, snippet) pairs recur as different origin notes share snippets.
2. Length pre-filter before the metric in `similar_notat_notes_in_note`: skip a pair when `abs(len(notation) - len(latex_text)) > max_len` (partial ratio can't exceed threshold if lengths differ too much).
3. Hoist latex extraction: build `{note.name: [latex texts]}` once per run and pass it in, instead of re-parsing each origin note's text inside the loop.

**Why:** vault-wide cost is O(#origin notes × #notation notes × #snippets × DP) with zero caching anywhere in the codebase (report §F: no `@lru_cache`/`@cache` in any of the 101 notebooks).

### 2.2 Vault files re-read multiple times per run

**Current:**
- `03_obsidian_70.vault_and_links.ipynb:158` — `all_links_in_vault` reads **every** note: `text = text_from_file(vault / path, encoding='utf8')` inside the loop.
- `05_personal_vault_10.notes.ipynb:78` — `notes_linked_in_note` does `text = list_note.text()` per call; `notes_linked_in_notes_linked_in_note` (line 86) calls it 1 + N times → 1 + N file reads.

So one note-linking run that uses both reads the same files 2–4×.

**Change:** build `link_map = all_links_in_vault(vault)` once per run and thread it as a parameter — the codebase already threads shared state this way (`note_data: dict[str, NoteData]`, `cache: dict[…])` in `sieve_potential_relied_notes`; extend the same pattern. Minimal version: give `notes_linked_in_note` an optional `links: list | None = None` param so callers with a map skip the read.

**Why:** disk + parse cost scales with vault size × number of passes; one pass is enough.

### 2.3 `VaultNote.rename` — wasted regex passes + redundant close

**Current:** `03_obsidian_10.vault_file_crud.ipynb` (cell `8830213c`) inner loop:

```python
for name, paths in self.__class__.cache[str(self.vault)].items():
    for path in paths:
        other_note = VaultNote(vault=self.vault, rel_path=path)
        if not other_note.exists():
            continue
        original_text = other_note.text()
        text = replace_links_in_text(text, old_wikilink_pattern_by_name, new_link_name=new_name)
        text = replace_links_in_text(text, old_markdownlink_pattern_by_name_1, …)
        text = replace_links_in_text(text, old_markdownlink_pattern_by_name_2, …)
        if text != original_text:
            with open(other_note.path(), 'w', encoding='utf-8') as file:
                file.write(text)
                file.close()
```

**Change:**
1. After reading, `if self.name not in original_text: continue` — the three regex passes only matter for notes that mention the old name (most don't).
2. Drop `file.close()` — the `with` block already closes.

**Why:** rename is O(vault) by nature, but 3 full-text regex scans per note are avoidable; the substring check is ~free after the read that's needed anyway.

### 2.4 `substring_generator` — dead O(n²) trap

**Current:** `01_helper_02.init.ipynb:66`:

```python
def substring_generator(input_string: str):
    length = len(input_string)
    for i in range(length):
        for j in range(i + 1, length + 1):
            yield input_string[i:j]
```

Grep evidence: only `sublist_generator` (its sibling) is imported anywhere (`01_helper_21.latex`, `01_helper_27_latex.processing`); `substring_generator` has **zero** references.

**Change:** delete it (or drop `#| export` if it's kept for the generated API).

**Why:** an exported n²-substring generator invites exactly the misuse §2.1 warns about.

### 2.5 Semantic search re-ingestion (verify)

`08_ml_90.semantic_search`: `_get_all_paths` + `ingest_files` rescan the tree on every run. Candidate: path→mtime dict so unchanged files skip embedding. *Not yet read in detail — confirm before committing.*

## 3. Action order

1. **A1** (module collision — correctness, not just tidiness).
2. **§2.1** caching + pre-filter (biggest runtime win, localized to `01_helper_02` + `08_ml_67`).
3. **A2–A5** pure import swaps (zero behavior change).
4. **§2.2/§2.3** link-map threading + rename micro-fixes.
5. **A6 + Tier B** shared test helpers; delete `substring_generator` (§2.4).

## State — COMPLETE (all Tier A verified against source)

Re-run scanner: `python _nbdev_development/spec_checkers/check_dupes_perf.py Python/trouver/nbs > _tmp/_dupes_perf_report_tmp.txt`.
