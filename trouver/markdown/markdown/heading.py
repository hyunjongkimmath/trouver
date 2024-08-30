"""Functions about Markdown headings"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/05_markdown.markdown.heading.ipynb.

# %% auto 0
__all__ = ['heading_level', 'heading_title']

# %% ../../../nbs/05_markdown.markdown.heading.ipynb 3
def heading_level(
        heading_str: str # A str representing a markdown heading. Starts with 1 to 6 sharps `'#'`.
        ) -> int: # Between 1 and 6, inclusive.
    """Return the level of the heading string."""
    without_sharps = heading_str.lstrip('#')
    return len(heading_str) - len(without_sharps)

# %% ../../../nbs/05_markdown.markdown.heading.ipynb 5
def heading_title(
        heading_str: str # A str representing a markdown heading. Starts with 1 to 6 sharps `'#'`.
        ) -> str:
    """Return the heading title, without the starting sharps.
    """
    return heading_str.lstrip('#').strip()
