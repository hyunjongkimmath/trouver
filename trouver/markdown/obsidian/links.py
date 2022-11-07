# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/06_markdown.obsidian.links.ipynb.

# %% ../../../nbs/06_markdown.obsidian.links.ipynb 2
from __future__ import annotations
from deprecated import deprecated
from enum import Enum
from pathlib import Path
import re
from trouver.helper import (
    find_regex_in_text, text_from_file
)
from trouver.markdown.obsidian.vault import (
    all_paths_to_notes_in_vault, VaultNote, NoteDoesNotExistError
)
from typing import Union


# %% auto 0
__all__ = ['INTERNAL_LINK_PATTERN', 'WIKILINK_PATTERN', 'EMBEDDED_WIKILINK_PATTERN', 'MARKDOWNLINK_PATTERN',
           'EMBEDDED_MARKDOWNLINK_PATERN', 'EMBEDDED_PATTERN', 'find_links_in_markdown_text']

# %% ../../../nbs/06_markdown.obsidian.links.ipynb 3
# TODO Make it so that these patterns don't capture latex code
INTERNAL_LINK_PATTERN = r'!?\[\[.*?\]\]' 
WIKILINK_PATTERN = r'!?\[\[[^\]]+\]\]'
EMBEDDED_WIKILINK_PATTERN = r'!\[\[[^\]]+\]\]'
# WIKILINK_CAPTURE = r'!?\[\[([^#\]\|]+)(#[^\]\|]+)?(\|[^\]]+)?\]\]'
# Note that MARKDOWNLINK_PATTERN captures whitespace characters in its link, even though Obsidian
# does not. This is implmeneted to find if any misformats in the Obsidian Markdown files.
MARKDOWNLINK_PATTERN = r'!?\[[^\]]+\]\([^)]+\)'  
EMBEDDED_MARKDOWNLINK_PATERN = r'!\[[^\]]+\]\([^)]+\)'
EMBEDDED_PATTERN = f'{EMBEDDED_WIKILINK_PATTERN}|{EMBEDDED_MARKDOWNLINK_PATERN}'
# MARKDOWNLINK_CAPTURE = r'!?\[([^\]]+)\]\(([^)#])+(#[^)]+)?\)'

# %% ../../../nbs/06_markdown.obsidian.links.ipynb 6
def find_links_in_markdown_text(
        text: str
        ) -> list[tuple]: # Each tuple is of the form `(a,b)` where `text[a:b]` is an obsidian internal link.
    """Returns ranges in the markdown text string
    where internal links occur.

    # TODO: rename this function, say to link_ranges_in_text, 
    # because it is confusing when there is a links_from_text function below.

    **See Also**

    - `links_from_text`
    """
    regex = f'{WIKILINK_PATTERN}|{MARKDOWNLINK_PATTERN}'
    return find_regex_in_text(text, pattern=regex)

