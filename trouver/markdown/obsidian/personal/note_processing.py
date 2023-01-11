# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../../nbs/19_markdown.obsidian.personal.note_processing.ipynb.

# %% auto 0
__all__ = ['remove_double_asterisks_in_markdown_file', 'standard_information_note_processor']

# %% ../../../../nbs/19_markdown.obsidian.personal.note_processing.ipynb 1
from deprecated import deprecated
from os import PathLike
from pathlib import Path, PureWindowsPath, WindowsPath
import re
from typing import Optional, Union

from ...markdown.file import MarkdownFile, MarkdownLineEnum, replace_embedded_links_with_text
from ..footnotes import remove_footnote_mentions_in_markdown_text
from ..links import EMBEDDED_PATTERN, remove_links_from_text
from ..vault import VaultNote

# %% ../../../../nbs/19_markdown.obsidian.personal.note_processing.ipynb 7
def remove_double_asterisks_in_markdown_file(
        markdown_file: MarkdownFile 
        ) -> None: 
    # TODO Don't remove asterisks in math mode.
    """Remove double asterisks in MarkdownFile object.
    
    The author of `trouver` chose to implement this function outside of the 
    `MarkdownFile` class because its use seems specific - this function
    is mostly intended to remove double asterisks marking definitions and
    notations introduced in LaTeX text.
    """
    for part in markdown_file.parts:
        part['line'] = part['line'].replace('**', '')

# %% ../../../../nbs/19_markdown.obsidian.personal.note_processing.ipynb 9
def standard_information_note_processor(
        markdown_file: Union[MarkdownFile, str],
        vault: PathLike,
        remove_frontmatter_meta: bool = True, # If `True`, removes the frontmatter meta. Defaults to `True`
        remove_see_also_section: bool = True, # If `True`, removes the `# See also` section. Defaults to `True`.
        remove_meta_section: bool = True, # If `True`, remove the `# Meta` section. Defaults to `True`.
        remove_references_section: bool = True, # If `True`, removes the `## References` section. Defaults to `True`.
        remove_double_asterisks: bool = True, # If `True`, removes double asterisks. Defaults to `True`.
        remove_links: bool = True, # If `True`, removes nonembedded links and replaces them with their display text. Defaults to `True`.
        remove_in_line_tags: bool = True, # If `True`, removes in-line tags (the lines that start with a tag).  Defaults to `True`.
        remove_footnotes_to_embedded: bool = True, # If `True`, removes footnotes to embedded notes. Defaults to `True`.
        remove_headers: bool = True, # If `True`, removes headers. Defaults to `True`.
        remove_citation_footnotes: bool = True, # If `True`, removes the citation footnote. Defaults to `True`.
        replace_embedded_links_with_content: bool = True, # If `True`, replaces embedded links with their content.  Defaults to `True`.
        merge_in_line_latex: bool = True, # If `True`, merge each group of in-line latex lines into single lines.  Defaults to `True`.
        merge_in_line_latex_into_text: Optional[str] = None, # If not `None`, merge each group of in-line latex lines into single lines and merge those groups into the text that precedes them with the specified str. Defaults to `None`.  The blank character ` ` and the new-line character `\n` are recommended as arguments.
        no_double_blank_lines: bool = True # If `True`, removes escape characters `'\n'` to make it so that there are no double blank lines. Defaults to `True`.
        ) -> MarkdownFile: # If `markdown_file` is a `MarkdownFile` object, then the output is `markdown_file` itself (not a copy) with modifications. If `markdown_file` is a `str`, then the output is a `MarkdownFile` object with the modifications.
    """Process/modify a str/MarkdownFile of a standard information note.
        
    TODO: implement remove_citation_footnote properly.
    
    """
    if isinstance(markdown_file, str):
        markdown_file = MarkdownFile.from_string(markdown_file)
    if remove_frontmatter_meta:
        markdown_file.remove_metadata()
    # if not remove_citation_footnote:
    #     return
    if remove_footnotes_to_embedded:
        markdown_file.remove_footnotes_to_embedded_links()
    if replace_embedded_links_with_content:
        markdown_file.replace_embedded_links_with_text(vault)
    if remove_see_also_section:
        markdown_file.remove_section('See Also')
    if remove_meta_section:
        markdown_file.remove_section('Meta')
    if remove_references_section:
        markdown_file.remove_section('References')
    if remove_double_asterisks:
        remove_double_asterisks_in_markdown_file(markdown_file)
    if remove_links: 
        markdown_file.replace_links_with_display_text()
    if remove_in_line_tags:
        markdown_file.remove_in_line_tags()
    if remove_headers:
        markdown_file.remove_headers()
    if merge_in_line_latex:
        markdown_file.merge_in_line_latex()
    if merge_in_line_latex_into_text:
        markdown_file.merge_in_line_latex_into_preceding_text(
            separator=merge_in_line_latex_into_text)
    if no_double_blank_lines:
        markdown_file.remove_double_blank_lines()
    # print(markdown_file)
    return markdown_file

