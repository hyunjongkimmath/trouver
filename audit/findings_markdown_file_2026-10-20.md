# `MarkdownFile` Review — Correctness & Performance

**Purpose:** detailed review of the `MarkdownFile` class and its module-level helpers, for later implementation. Line numbers refer to the generated `trouver/obsidian/file.py`; **all edits go into `nbs/03_obsidian_40.file.ipynb`** (nbdev source of truth — never edit `trouver/`).

**Method:** full read of `file.py` (1618 lines, 2026-10-20). Each item states the current behavior, the change, and why.

**Companion:** `findings_note_processing_2026-10-20.md` reviews the `process_standard_information_note` pipeline that chains many of these methods (its N3 subsumes C5/P1 for the tail-cleanup trio).

---

## Part 1 — Correctness issues

### C1 — `metadata_lines` crashes when there is no frontmatter ⚠️ crash-prone

**Current:** `file.py:862-891`. `start` is only assigned inside a `for i, part in enumerate(self.parts)` loop that breaks on the first META part; `end` is only assigned inside a second loop that breaks on the first non-META part. If the file has no metadata at all, `start` is never bound → `UnboundLocalError`. Likewise, if every part from the first META onward is META (no break in the second loop), `end` is never bound.

**Why it matters:** `replace_metadata` (`file.py:915`) calls `self.metadata_lines()` unconditionally, so calling `replace_metadata` on a file without frontmatter raises `UnboundLocalError` instead of inserting the metadata block at the top. Same for `add_tags`/`remove_tags` paths that reach `replace_metadata`.

**Change:** initialize `start = end = None` (or return a sentinel like `(None, None)` / `-1`) and make `replace_metadata` treat "no existing metadata" as "insert at index 0". Update the docstring, which currently says "Assumes that `self.parts` is nonempty" — the real assumption needed is "has metadata", or drop the assumption.

### C2 — Code fences classified as `COMMENT` / unclassified

**Current:** `file.py:258-263`, in `_line_dict`:

```python
if parts and parts[-1]['type'] is MarkdownLineEnum.CODE_BLOCK:
    if parts[-1]['line'].strip() != '```':
        line_dict['type'] = MarkdownLineEnum.CODE_BLOCK
        return line_dict
elif line.strip().startswith('```'):
    line_dict['type'] = MarkdownLineEnum.COMMENT   # ← should be CODE_BLOCK
```

Two defects: (a) the opening-fence branch sets `COMMENT` instead of `CODE_BLOCK`; (b) when the previous line *is* a closing fence (previous type `CODE_BLOCK`, previous line ```` ``` ````), the outer `if` body does not return, the `elif` is skipped (outer `if` was true), and the closing fence falls through the whole chain to `DEFAULT`/`UNKNOWN`.

**Why it matters:** any method that special-cases or skips a line type misbehaves on fenced code: e.g. `replace_links_with_display_text` only skips `META`, so wiki-links inside code fences get rewritten; `clear_all_sections` keeps `COMMENT` lines, so fence-openers survive as stray `%%`-less "comments".

**Change:** set `CODE_BLOCK` in the `elif`; when inside a code block and the previous line was a closing fence, classify the current line by the normal chain (i.e. treat the fence pair as closed). Track fence state explicitly (open/close) rather than inferring it from the previous line's text.

### C3 — `_text_of_embedded_link_of_id` defined twice, identically

**Current:** `file.py:1195-1209` and `file.py:1211-1226` — two `@patch`ed methods with the same name and byte-identical bodies. The second silently shadows the first.

**Change:** delete one copy (in the notebook, remove the duplicate cell).

### C4 — `parts_of_id` never returns `None` on missing id ⚠️ contract violation

**Current:** `file.py:1368-1395`. Docstring: "If the specified id does not exist for the note, then `None` is returned." In practice, if the loop over `reversed(self.parts)` finds no match, `i` retains its last enumerated value (`len(parts)-1`), and the method returns `(0, 1)` — silently embedding the first line of the note. On an *empty* parts list, `i` is never bound → `NameError`.

**Why it matters:** `_text_of_embedded_link_of_id` (`file.py:1203`) calls `parts_of_id` and unpacks the result without a `None` check, so a link to a non-existent block id embeds garbage (the note's first line) instead of nothing.

**Change:** track whether a match was found (e.g. initialize `i = None` before the loop, `return None` if still `None`); make `_text_of_embedded_link_of_id` return `''` on `None`.

### C5 — `remove_double_blank_lines` wraps around at index 0

**Current:** `file.py:1182-1191`:

```python
for i, part in enumerate(self.parts):
    last_blank = self.parts[i-1]['type'] == MarkdownLineEnum.BLANK_LINE
```

At `i=0`, `self.parts[-1]` is the *last* part. If both the first and last lines are blank, line 0 is wrongly removed.

**Change:** guard with `i > 0 and ...`, or (better, see P1) rebuild in one pass where the wrap-around cannot happen.

### C6 — `add_metadata_section` writes `'---\n'` lines

**Current:** `file.py:936-937` inserts `{'line': '---\n'}` twice, violating the class invariant (documented in the class docstring) that `'line'` values carry no newline characters. `__str__`/`text_of_lines` then joins with `'\n'`, producing `---\n\n---` — a blank line *inside* the frontmatter block.

**Why it matters:** inconsistent with `replace_metadata`, which uses bare `'---'`; downstream re-parsing (`reset_parts`, `write(check_validity=True)`) sees a different document than intended, and `yaml.safe_load('')` → `None` masks the difference in `metadata()`.

**Change:** use `'---'` (no trailing newline), matching `replace_metadata`.

### C7 — `has_metadata` disagrees with `metadata_parts` when blank lines precede frontmatter

**Current:** `_look_at_start_of_file` (`file.py:357-360`) legally emits `BLANK_LINE` parts before `META` parts (blank lines may precede frontmatter). But `has_metadata` (`file.py:857-859`) checks `self.parts[0]['type'] == META`, so a file with one leading blank line then frontmatter has nonempty `metadata_parts()` yet `has_metadata() == False`.

**Change:** make `has_metadata` scan for the first META part (or, if the intended invariant is "frontmatter must be at byte 0", enforce that in `_look_at_start_of_file` and document it). Pick one semantics and align both methods.

### C8 — `from_file` vs `from_string` line-splitting inconsistency

**Current:** `from_file` (`file.py:465`) uses `text.split('\n')`; `from_string` (`file.py:488`) and `parts_from_text` (`file.py:409`) use `splitlines(keepends=False)`. Consequences: a trailing newline yields an extra `''` part in `from_file` only; on non-Windows, CRLF files read via `from_file` keep `'\r'` at line ends (text-mode open translates only per-platform).

**Change:** have `from_file` delegate to `from_string` (read text, then one shared splitting path).

### C9 — Minor / acknowledged TODOs

- `get_headings_and_text` (`file.py:533-560`) keys its result dict on heading *text*, so two sections with identical titles overwrite each other. The existing TODO comment at `file.py:538-539` also notes a levels-filtering bug (all-level-1 headings + `levels=2` + `include_start=True` dumps everything under the start key).
- `get_line_numbers_under_heading` (`file.py:618-646`) accepts `from_line` and `levels` but ignores them (TODO at `file.py:628`). Dead parameters — implement or remove.
- Module-level function `replace_embedded_links_with_text` (`file.py:133-158`) and the same-named method (`file.py:1308`) are distinct functions with subtly different behavior (the module one does not support anchors/recursive); the name collision is a footgun. Consider renaming one (e.g. `expand_embedded_links_in_text`).

---

## Part 2 — Performance opportunities

### P1 — O(n²) remove/insert loops → single-pass rebuilds

**Current:** these methods collect indices, then do one `list.insert` / `del` per hit — each O(n), total O(n·k):

| Method | Location |
|---|---|
| `remove_double_blank_lines` | `file.py:1182-1191` |
| `_separate_consecutive_default_lines` | `file.py:1536-1549` (inserts) |
| `clear_all_sections` | `file.py:789-804` |
| `remove_headers` | `file.py:1171-1178` |
| `remove_in_line_tags` | `file.py:1089-1098` |
| `remove_footnotes_to_embedded_links` | `file.py:1143-1167` (first removal loop) |

**Change:** rebuild in one pass, e.g. `self.parts = [p for i, p in enumerate(self.parts) if i not in to_remove]` (or a streaming keep/drop generator for the insert cases). O(n), shorter code, and fixes C5 for free.

### P2 — Repeated full scans of headings across method chains

**Current:** `get_headings_by_line_number` (`file.py:492-514`) re-scans all parts on every call, and chains stack up:

- `remove_section`: heading lookup + full scan + sort = 2 scans
- `clear_section`: 2 heading lookups = 2 scans
- `_text_of_embedded_link_of_section` → `get_line_numbers_under_heading`: heading lookup + `get_headings_by_line_number` + sort = 3 scans

**Change:** a lazily-computed heading index (list of `(line_number, level, title)`), invalidated on any mutation of `parts`, collapses each chain to one scan. Implement by overriding mutation points (`insert_line`, `remove_line(s)`, `pop_line`, direct `self.parts = ...` reassignments — the latter several, so a private `_set_parts` helper would centralize invalidation).

Note: for typical Obsidian note sizes (hundreds of lines) this is mostly theoretical; do it only if profiling shows heading lookups in a hot path (e.g. batch `replace_embedded_links_with_text` over many notes).

### P3 — `write(check_validity=True)` re-parses the entire file on every write

**Current:** `file.py:1601-1604`: `str(self)` → `MarkdownFile.from_string` (full per-line classification of the whole document) → `metadata()` (yaml parse). Two full passes over the document, on every write.

**Change options:**
1. If validity is already checked upstream in the pipeline, default `check_validity=False` at the call sites that don't need it.
2. Cheaper check: validate only the yaml block — `parse_metadata_string('\n'.join(self.metadata_parts()[1:-1]))` — which skips the full re-classification and catches the actual failure mode (unparseable frontmatter) that the error message describes.

### P4 — Small constants

- `string.whitespace + '*'` is concatenated on every call to `_line_start_in_line_latex`, `_line_end_in_line_latex`, `_line_start_and_end_in_line_latex` (`file.py:318, 322, 327`). Hoist to a module constant `_LATEX_STRIP_CHARS = string.whitespace + '*'`.
- Precompiling the per-line `re.match` literals in `_line_dict` buys little (the `re` module caches up to 512 compiled patterns) — skip unless a profiler says otherwise.

---

## Suggested implementation order

1. **C1, C4** — crash/contract bugs reachable from normal use (`replace_metadata`, block-id links).
2. **C3** — trivial dead-code deletion.
3. **P1 (+ C5)** — single-pass rebuilds; strictly simpler and faster.
4. **C2, C6, C7, C8** — classification/consistency fixes (C2 touches parser state; give it a dedicated test cell).
5. **P3** — if write throughput matters in batch pipelines.
6. **P2, P4, C9** — only under profiling pressure / opportunistic cleanup.

Each fix should land with an assert-only test in the notebook's `_tests` fixture per `nbs/CONTEXT.md`.
