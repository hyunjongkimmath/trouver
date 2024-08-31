"""Helper functors dealing with HTML tags"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/38_helper.html.ipynb.

# %% auto 0
__all__ = ['html_tag_str', 'find_lt_symbols_without_space_in_math_mode', 'add_space_to_lt_symbols_without_space',
           'remove_html_tags_in_text', 'add_HTML_tag_data_to_raw_text']

# %% ../../nbs/38_helper.html.ipynb 2
import bs4
from bs4 import BeautifulSoup
import random
import re
from typing import Optional, Union


from .regex import latex_indices, find_regex_in_text, replace_string_by_indices


# %% ../../nbs/38_helper.html.ipynb 5
def html_tag_str(
        html_tag: bs4.element.Tag
        ) -> str:
    """
    Return the full string of `html_tag`, accounting for 
    special characters that `bs4` changes
    """
    special_chars = {'&lt;': '<', '&gt;': '>', '&amp;': '&'}
    text_to_return = str(html_tag)
    for special_char, replace_with in special_chars.items():
        text_to_return = text_to_return.replace(special_char, replace_with)
    return text_to_return

# %% ../../nbs/38_helper.html.ipynb 10
def find_lt_symbols_without_space_in_math_mode(
        text: str
        ) -> list[int]: # The index of  
    """
    Return the indices in `text` with math mode less than `<` symbols without
    a space that follows.
    """
    latex_inds = latex_indices(text)
    lt_pattern = re.compile(r'<(?! )')
    inds_of_lt_without_spaces_after = []
    for start, end in latex_inds:
        latex_str = text[start:end]
        relative_lt_inds = find_regex_in_text(latex_str, lt_pattern)
        inds_of_lt_without_spaces_after.extend([
            start + relative_lt_ind for relative_lt_ind, _ in relative_lt_inds
        ])
    return inds_of_lt_without_spaces_after 


# %% ../../nbs/38_helper.html.ipynb 14
def add_space_to_lt_symbols_without_space(
        text: str
        ) -> str:
    """Add space after less than `<` symbols if the symbol
    is not followed by a space.
    """
    lt_wo_space_inds = find_lt_symbols_without_space_in_math_mode(text)
    lt_wo_space_ranges = [(ind, ind+1) for ind in lt_wo_space_inds]
    return replace_string_by_indices(
        text, replace_ranges=lt_wo_space_ranges,
        replace_with=['< '] * len(lt_wo_space_inds))
    

# %% ../../nbs/38_helper.html.ipynb 20
def remove_html_tags_in_text(
        text: str, # The text in which to remove the HTML tags.
        replace_with_attributes: Optional[Union[str, list[str]]] = None, # Attribute(s) within the HTML tags which should be used to replace the text of the tags. If `None`, then the texts are not replaced with the attributes. If multiple attributes are specified, then only one attribute is used to replace the text for each HTML tag (independently at random of other replacements). Each attribute's text has an equal chance of being selected for replacement. Repeats are ignored.
        definitely_replace: bool = False, # If `True` and if a given HTML tag has an attribute specified in `replace_with_attributes`, then the text for that tag will definitely be replaced by the text of one of the attributes. Otherwise, the original text and each attribute's text have an equal chance of being selected.
        seed: int = None # Random seed 
        ) -> tuple[str, list[tuple[bs4.element.Tag, int, int]]]: # The text `removed` without HTML tags and a list whose elements consist of the removed HTML tags and the starting and ending indices of the text corresponding to the removed tags within `removed`.
    """Remove the HTML tags in `text`.

    HTML tags are assumed to be not nested.

    """
    random.seed(seed)
    parsed_soup = BeautifulSoup(text, 'html.parser')
    replace_with_attributes = _init_replace_with_attributes(
        replace_with_attributes)

    position = 0
    replaced_contents = []
    for content in parsed_soup.contents:
        position = _process_content(
            parsed_soup, replace_with_attributes, definitely_replace, content,
            position, replaced_contents)
    text_to_return = html_tag_str(parsed_soup)
    return text_to_return, replaced_contents


def _init_replace_with_attributes(
        replace_with_attributes: Optional[Union[str, list[str]]]
        ) -> set[str]:
    if replace_with_attributes is None:
        replace_with_attributes = []
    elif isinstance(replace_with_attributes, str):
        replace_with_attributes = [replace_with_attributes]
    return set(replace_with_attributes)


def _select_replacement_text(
        content: bs4.element.Tag,
        replace_with_attributes: set[str],
        definitely_replace: bool) -> str:
    if not replace_with_attributes:
        return content.string
    selection_pool = []    
    if not definitely_replace:
        selection_pool.append(content.string)
    for attribute, value in content.attrs.items():
        if attribute not in replace_with_attributes:
            continue
        selection_pool.append(value)
    return random.choice(selection_pool)


def _process_content(
        parsed_soup: BeautifulSoup,
        replace_with_attributes: set[str],
        definitely_replace: bool,
        content,
        position: int,
        replaced_contents: list) -> int:
    
    if not isinstance(content, bs4.element.Tag):
        return position + len(content)
    replacement_text = _select_replacement_text(
        content, replace_with_attributes, definitely_replace)
    
    try:
        replaced_content = content.replace_with(
            parsed_soup.new_string(replacement_text))
    except TypeError as e:
        raise e

    replaced_contents.append((
        replaced_content,
        position,
        position + len(replacement_text)))
    return position + len(replacement_text)
    

# %% ../../nbs/38_helper.html.ipynb 37
def add_HTML_tag_data_to_raw_text(
        text: str, # The text onto which to add HTML tags. This is assumed to contain no HTML tags.
        tags_and_locations: list[tuple[bs4.element.Tag, int, int]] # Each tuple consists of the tag object to add as well as the indices within `text` to. The ranges specified by the tuples are assumed to not overlap with one another.
        ) -> str: # The modification of `text` in which the tags are added at the specified locations; the ranges in `text` are replaced..
    """
    Add specified HTML tags to the specified locations/ranges in `text`.

    See the `add_HTML_tag_data_to_text` function for adding HTML
    tag data to text that may or may not already have HTML tags.
    """
    # sort by starting index
    tags_and_locations = sorted(
        tags_and_locations, key=lambda x: x[1])
    replace_ranges = [(start, end) for _, start, end in tags_and_locations]
    replace_with = [html_tag_str(html_tag) for html_tag, _, _ in tags_and_locations]
    return replace_string_by_indices(text, replace_ranges, replace_with)