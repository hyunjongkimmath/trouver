# `process_standard_information_note` Review — Performance

**Purpose:** optimization review of the standard-information-note processing pipeline, for later implementation. Companion to `findings_markdown_file_2026-10-20.md` (the `MarkdownFile` methods this pipeline chains are reviewed there). Line numbers refer to generated files; **all edits go into the nbdev sources**: `nbs/05_personal_vault_25.note_processing.ipynb` and `nbs/03_obsidian_40.file.ipynb`.

**Method:** full read of `trouver/personal_vault/note_processing.py` (111 lines) plus the chained `MarkdownFile` methods in `trouver/obsidian/file.py`, and the `VaultNote` cache behavior in `trouver/obsidian/vault.py` (2026-10-20).

The pipeline is ~15 sequential passes over `parts`. Cost is heavily skewed: embedded-link expansion dominates; the rest is repeated scans and O(n·k) delete loops.

---

## N1 — Embedded-link expansion has no memoization ⚠️ dominant cost

**Current:** `replace_embedded_links_with_text` (`file.py:1308-1329`) → `_replace_embedded_links_one_line` (`file.py:1269-1304`). Every `![[...]]` *occurrence* does:

```python
link_note = VaultNote(vault, name=link_object.file_name, update_cache=False)
link_file = MarkdownFile.from_vault_note(link_note)   # full file read + full line-classification
```

The `VaultNote` class-level cache makes *path resolution* cheap after the first hit for a given name, but the **parse is never cached**: a note embedded 5 times is read from disk and fully re-classified (per-line regex chain in `_line_dict`) 5 times. The recursive branch (`_text_of_lines_of_embedded_links`, `file.py:1249-1265`) compounds this — it deepcopies the slice and re-expands nested links, again per occurrence.

**Change:** a memo dict keyed by resolved path, scoped to one top-level `replace_embedded_links_with_text` call (instance attribute initialized at entry, or threaded through `_replace_embedded_links_one_line` and the helpers).

**Safety:** nothing in the expansion path mutates `link_file` — `str(link_file)`, `text_of_lines`, and `parts_of_id` are read-only, and the recursive branch deepcopies before processing. Caching parsed files is therefore safe.

**Why:** this is the single biggest win, and it scales with batch size — processing N notes in a vault where K of them are commonly embedded goes from O(total occurrences × target size) disk+parse work to O(distinct targets).

## N2 — Three `remove_section` calls ≈ 9 passes → 1

**Current:** `note_processing.py:81-86` calls `remove_section` for `'See Also'`, `'Meta'`, `'References'`. Each call (`file.py:740-758`) does a heading lookup (full scan) + `get_headings_by_line_number` (full scan) + sort + O(n) slice-splice.

**Change:** a private `_remove_sections(titles: set[str])` helper — one scan identifying all requested section ranges, one combined deletion. Replaces 3 scans + 3 sorts + 3 splices with 1 of each. Keep the public `remove_section` for single-section use.

## N3 — Tail cleanup: six passes → two

**Current:** `note_processing.py:99-109` runs `remove_in_line_tags`, `remove_headers`, `remove_double_blank_lines` back to back. Each does an O(n) scan plus an O(n·k) per-index delete loop (the P1 pattern from `findings_markdown_file_2026-10-20.md`; also carries the index-0 wrap-around bug C5 in `remove_double_blank_lines`).

**Change:** when all three flags are on (the default), one consolidated keep/drop sweep — classify each line once (heading? in-line tag? consecutive blank?) and rebuild `parts` in a single pass. Keep the individual methods for flag-combinations where only some apply.

## N4 — `merge_display_math_mode` runs twice when both merge flags are set (minor)

**Current:** with `merge_display_math_mode=True` *and* `merge_display_math_mode_into_text` set, the merge scan runs once at `note_processing.py:103-104` and again inside `merge_display_math_mode_into_preceding_text` (`file.py:1483`).

**Why it's minor:** after the first merge no `DISPLAY_LATEX_START` lines remain, so the second run is a cheap no-op scan.

**Change (optional):** skip step 13 in the pipeline when `merge_display_math_mode_into_text is not None`.

## N5 — `reset_parts()` full re-parse at end of merge-into-text (keep, be aware)

**Current:** `file.py:1491` — `merge_display_math_mode_into_preceding_text` ends with `reset_parts()`, which re-parses the whole document (`str(self)` → `from_string` → per-line regex classification).

**Assessment:** intrinsic — merging latex into text lines breaks the one-type-per-line invariant, so a re-classification is genuinely needed. No change; just note the pipeline ends with a full pass when this option is used.

## N6 — Cheap short-circuits (regex avoidance)

| Location | Short-circuit |
|---|---|
| `_replace_embedded_links_one_line` (`file.py:1279`) | `if '![' not in text: return text` before `find_regex_in_text` — most lines have no links |
| `remove_block_identifiers` / `_remove_text_id` (`file.py:1127-1139`, `304-309`) | skip the regex when `'^' not in line` |
| `remove_double_asterisks_in_markdown_file` (`note_processing.py:31`) | `if '**' in part['line']` before `.replace('**', '')` |

## N7 — Correctness observations (not perf)

- **Case sensitivity of `'See Also'`:** docstring says the `# See also` section is removed, code passes `'See Also'` (`note_processing.py:82`), and heading matching is exact. If vault notes use a different case, removal silently no-ops. Verify against actual note conventions before relying on it.
- **Debug leftover:** the `except TypeError` around `remove_html_tags` (`note_processing.py:90-96`) prints the entire file to stdout before raising; `ProcessNoteError.__str__` already embeds the file content. Drop the `print`s (or convert to a log).

## Ordering note (no change needed)

Step ordering is otherwise sound and should be preserved in any refactor:
- `remove_footnotes_to_embedded_links` runs **before** expansion, so whole notes don't get inlined into footnote definitions.
- `remove_block_identifiers` runs **after** expansion, so block ids brought in by inlined content get cleaned.

---

## Suggested implementation order

1. **N1** — memoization; biggest win, self-contained, safe per the mutation analysis above.
2. **N6** — three one-line short-circuits.
3. **N2, N3** — pass consolidation (N3 also fixes C5 from the companion file).
4. **N7** — verify `'See Also'` casing against the vault; drop debug prints.
5. **N4** — optional micro-clean.

Each fix lands in the notebook with an assert-only test per `nbs/CONTEXT.md`. N1's test: a note embedding the same target twice must produce identical output to embedding it once, and (instrumented) read the target file only once.
