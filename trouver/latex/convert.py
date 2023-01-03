# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/16_latex.convert.ipynb.

# %% auto 0
__all__ = ['DEFAULT_NUMBERED_ENVIRONMENTS', 'NoDocumentNodeError', 'find_document_node']

# %% ../../nbs/16_latex.convert.ipynb 3
from collections import OrderedDict
import os
from os import PathLike
from pathlib import Path
from pylatexenc import latexwalker, latex2text
from pylatexenc.latexwalker import (
    LatexWalker, LatexEnvironmentNode, get_default_latex_context_db,
    LatexNode, LatexSpecialsNode, LatexMathNode, LatexMacroNode, LatexCharsNode,
    LatexGroupNode, LatexCommentNode
)
from pylatexenc.latex2text import (
    MacroTextSpec, EnvironmentTextSpec)
from pylatexenc.macrospec import (
    MacroSpec, LatexContextDb, EnvironmentSpec
)
import re
from typing import Union
from trouver.helper import (
    find_regex_in_text, dict_with_keys_topologically_sorted,
    containing_string_priority, replace_string_by_indices, text_from_file
)
from trouver.markdown.markdown.file import (
    MarkdownFile, MarkdownLineEnum
)

from ..markdown.obsidian.vault import VaultNote
from trouver.markdown.obsidian.personal.index_notes import (
    correspond_headings_with_folder, convert_title_to_folder_name
)
from ..markdown.obsidian.personal.reference import setup_folder_for_new_reference
from ..markdown.obsidian.vault import VaultNote
import warnings

# %% ../../nbs/16_latex.convert.ipynb 4
DEFAULT_NUMBERED_ENVIRONMENTS = ['theorem', 'corollary', 'lemma', 'proposition',
                                 'definition', 'conjecture', 'remark', 'example',
                                 'question']

# %% ../../nbs/16_latex.convert.ipynb 19
class NoDocumentNodeError(Exception):
    """Exception raised when a LatexEnvironmentNode corresponding to the document 
    environment is expected in a LaTeX string, but no such node exists.
    
    **Attributes**
    - text - str
        - The text in which the document environment is not found.
    """
    
    def __init__(self, text):
        self.text = text
        super().__init__(
            f"The following text does not contain a document environment:\n{text}")



# %% ../../nbs/16_latex.convert.ipynb 20
def find_document_node(
        text: str, # LaTeX str
        document_environment_name: str = "document" # The name of the document environment.
        ) -> LatexEnvironmentNode:
    """Finds the `LatexNode` object for the main document in `text`.
    
    **Raises**
    - NoDocumentNodeError
        - If document environment node is not detected.
    """
    w = LatexWalker(text)
    nodelist, _, _ = w.get_latex_nodes(pos=0)
    for node in nodelist:
        if node.isNodeType(LatexEnvironmentNode)\
                and node.environmentname == document_environment_name:
            return node
    raise NoDocumentNodeError(text)
