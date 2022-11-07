# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/04_markdown.markdown.file.ipynb.

# %% ../../../nbs/04_markdown.markdown.file.ipynb 2
from __future__ import annotations
import copy
from enum import Enum
from itertools import product
import re
import string
from typing import Iterator, Union, Optional
import yaml

from trouver.helper import (
    find_regex_in_text 
)
# from trouver.markdown.markdown.heading import (
#     heading_level, heading_title
# )
# from trouver.markdown.obsidian.links import (
#     ObsidianLink, 
#     remove_links_from_text, EMBEDDED_PATTERN, replace_embedded_links_with_text
# )
from ..obsidian.vault import VaultNote, NoteDoesNotExistError
# from trouver.markdown.obsidian.tags import (
#     strip_auto_from_tag, tag_is_auto_tag
# )

# %% auto 0
__all__ = []
