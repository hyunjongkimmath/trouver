# Coding Standards — Trouver Notebooks

These standards are distilled from comparing the well-maintained notebooks (`01_helper_04.regex.ipynb`, `03_obsidian_01.vault.ipynb`) against the degraded ones (`04_latex_20.convert.ipynb`, `05_personal_vault_20.information_notes.ipynb`) in this codebase. They're not generic best practices — they address the specific decay patterns observed here.

## Function Length: Maximum 20 Lines

Functions should be **no more than 20 lines of executable code** (excluding docstrings, blank lines, and inline comments). This is a hard limit, not a suggestion. When a function exceeds this, extract logical sub-parts into named helper functions.

Long functions are the root cause of most decay patterns in this codebase — they accumulate edge cases over time, become difficult to test, and are where commented-out code tends to hide.

## Six Practices

### 1. One Function, One Responsibility

A function should do a single thing that its name describes. If the name contains "and" (e.g., `parse_and_format_and_save`), it's doing too much.

**Good**: `extract_latemacros_from_preamble`, `validate_vault_path` — specific, single-action verbs.
**Bad**: A function that parses, transforms, validates, and writes in one pass.

### 2. Tests Co-located with Code

Every exported function should have test cells immediately below it in the same notebook. This ensures tests and implementation degrade together if someone modifies the function. A function without tests is technical debt that will compound — marked `# TODO: test` it becomes a reminder, unmarked it becomes a blind spot.

### 3. Extract Helpers Instead of Nesting

When logic requires multiple levels of conditionals or loops, extract each level into its own named function rather than indenting deeper. Several 15-line functions that call each other clearly is the goal; four levels of nesting in an 80-line function is the antipattern.

### 4. Delete Dead Code, Don't Comment It Out

If an implementation is superseded, remove it entirely. Git history preserves the old version if it's ever needed. Commented-out blocks inline are noise that confuses future readers and AI assistants alike.

### 5. Finish or Don't Export

Bare `return` statements with no body should not be exported. If an implementation is planned but incomplete, either skip the `#| export` flag or raise `NotImplementedError` so failures are explicit rather than silent.

### 6. Trust Function Boundaries

When a function is ≤20 lines and has tests, you don't need defensive comments explaining what it does. The name + body should be self-evident. If you feel the urge to write a paragraph comment above a function, make the function smaller or give it a better name instead.