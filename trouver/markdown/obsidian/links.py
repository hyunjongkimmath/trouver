# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/06_markdown.obsidian.links.ipynb.

# %% ../../../nbs/06_markdown.obsidian.links.ipynb 3
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
           'EMBEDDED_MARKDOWNLINK_PATERN', 'EMBEDDED_PATTERN', 'find_links_in_markdown_text', 'LinkFormatError',
           'LinkType', 'ObsidianLink']

# %% ../../../nbs/06_markdown.obsidian.links.ipynb 4
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

# %% ../../../nbs/06_markdown.obsidian.links.ipynb 7
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


# %% ../../../nbs/06_markdown.obsidian.links.ipynb 16
class LinkFormatError(Exception):
    """Error that is raised when a string cannot be parsed as an
    `ObsidianLink` object.
    
    **Attribute**

    - `text` - `str`
    """
    def __init__(self, text):
        self.text = text
        super().__init__(f'Obsidian Markdown link is not formatted properly: {text}')

# %% ../../../nbs/06_markdown.obsidian.links.ipynb 18
class LinkType(Enum):
    """An Enumeration indicating whether an `ObsidianLink` object is a
    Wikilink or a Markdown-style link.

    Enumerates `LinkType.WIKILINK` and `LinkType.MARKDOWN`.
    """
    # See https://www.markdownguide.org/basic-syntax/
    WIKILINK = 0
    MARKDOWN = 1  
    # For Markdown links, use %20 to encode spaces in the link, e.g.
    # [asdf](localization_of_a_module#Localization%20of%20a%20module%201)
    # Links to the header `"Localization of a module 1"` in the file
    # localization_of_a_module



# %% ../../../nbs/06_markdown.obsidian.links.ipynb 19
# TODO: implment equality, copy
class ObsidianLink:
    """Object representing an obsidian link
    
    **Attributes**

    - `is_embedded` - `bool`
        - Whether or not the link is embedded.
    - `file_name` - `str`, or `-1`
        - The destination of the link. It is either 
        
          1. The Obsidian-vault-recognized name of the file that the link
          points to. It can be a path relative to the Obsidian vault path 
          without the file extension (.md), 
          2. an external link, such as a URL, or
          3. -1, in which case the object represents a generic link pointing
          to any file (this is for generating regex).
          
          Note that if `file_name` is the empty string, then the link is a
          link to the same file

    - `anchor` - `str`, `0`, or `-1`
        - The title of the header of the anchor in the destination that the
        link points to or the ID to the markdown block link (preceded by a
        carat `^`). If 0, then the `ObsidianLink` object represents a link
        without an anchor. If -1, then the object represents a generic link
        with or without an anchor (this is for generating regex).
    - `custom_text` - `str`, `0`, or `-1`
        - The custom text of the link. Is `None` if no such text is specified.
        If 0, then the `ObsidianLink` object represents an internal link
        without custom text. If -1, then the object represents a generic
        internal link of any custom text (this is for generating regex).
    - `link_type` - `LinkType`
        - If `LinkType.WIKILINK`, then the str should be of the format
        `'[[<Obsidian-vault-recognized-name>(#anchor)?(|custom_text)]]'` 
        (The question marks here indicate optional components). Otherwise,
        the str should be a more standard Markdown link. Defaults to
        `LinkType.WIKILINK`.
    
    **Parameters**

    - is_embedded - bool
    - file_name - str or `None`
        - If `None`, set `self.file_name` to `-1`.
    - anchor - str or `None`
    - custom_text - str or `None`
    - link_type - `LinkType`
    """
    
    def __init__(
            self, is_embedded: bool, file_name: Union[str, int],
            anchor: Union[str, int], custom_text: Union[str, int],
            link_type: LinkType = LinkType.WIKILINK):
        self.is_embedded = is_embedded
        self.file_name = file_name
        self.anchor = anchor
        self.custom_text = custom_text
        self.link_type = link_type


    @staticmethod
    def from_text(text: str) -> ObsidianLink:
        """Returns an ObsidianLink object from text.
                
        **Parameters**
        - `text` - str
        
        **Raises**
        - InteralLinkFormatError
            - If the text is not properly formatted as an Obsidian internal link.
        """
        is_embedded = text.startswith("!")
        regex_object = re.compile(r"!?\[\[([^#\|]*?)(#(.*?))?(\|(.*?))?\]\]")
        matches = regex_object.match(text)
        if matches:
            file_name = matches.group(1)
            anchor = matches.group(3)
            custom_text = matches.group(5)
            link_type = LinkType.WIKILINK
        else:
            regex_object = re.compile(r'!?\[([^\]]*)\]\(([^)#]+)(#([^)]+))?\)')
            matches = regex_object.match(text)
            if not matches:
                raise LinkFormatError(text)
            file_name = matches.group(2).replace('%20', ' ')
            anchor = matches.group(4)
            if anchor:
                anchor = anchor.replace('%20', ' ')
            custom_text = matches.group(1)
            link_type = LinkType.MARKDOWN
        if anchor is None:
            anchor = 0
        if custom_text is None:
            custom_text = 0
        return ObsidianLink(is_embedded, file_name, anchor, custom_text, link_type)


    def to_regex(self) -> str:
        """Returns the regex for that this `Link` object represents

        Assumes that `self.file_name`, `self.anchor`, and `self.custom_text` are
        regex-formatted strings, e.g. if self.custom_text is `denotes?`, then the
        outputted regex-pattern matches links whose custom text is either `denote`
        or `denotes`.

        If neither `self.file_name`, `self.anchor` nor `self.custom_text` is `-1`,
        then the regex will in fact be a concrete string.

        **Returns**
        - str
            - Representing a regex.
        """
        embedding = '!' if self.is_embedded else ''

        if type(self.file_name) == str:
            filing = self.file_name
        else:  # self.file_name == -1
            filing = r'([^#\|]*)?'
        
        if type(self.anchor) == str:
            anchoring = f'#{self.anchor}'
        elif self.anchor == 0:
            anchoring = ''
        else:  # self.anchor == -1
            anchoring = '(#(.*?))?'
          
        if type(self.custom_text) == str and self.link_type == LinkType.WIKILINK:
            customing = fr'\|{self.custom_text}'
        elif type(self.custom_text) == str and self.link_type == LinkType.MARKDOWN:
            customing = self.custom_text
        elif self.custom_text == 0:
            customing = ''
        else:  # self.custom == -1
            if self.link_type == LinkType.MARKDOWN:
                customing = fr'(.*?)?'
            else:
                customing = fr'(\|(.*?))?'

        if self.link_type == LinkType.WIKILINK:
            return fr'{embedding}\[\[{filing}{anchoring}{customing}\]\]'
        else:
            # Markdown links format whitespace with '%20'
            filing = filing.replace(' ' , '%20')  
            anchoring = anchoring.replace(' ', '%20')
            return fr'{embedding}\[{customing}\]\({filing}{anchoring}\)'
    
    def __str__(self) -> str:
        # TODO: Choose what to do about | vs. \|.
        return self.to_string()

    def to_string(self) -> str:
        """Returns the string for the link if it is concrete.
        
        **Returns**
        - str
        
        **Raises**
        - ValueError
            - If `self.file_name`, `self.anchor` or `self.custom_text`
            is -1, i.e.  ambiguously represents an anchor or custom text.
        """
        if self.is_abstract():
            raise ValueError(
                f'The ObsidianLink object is abstract.'
            )
        assert (self.anchor != -1 and self.custom_text != -1
                and self.file_name != -1)
        embedding = '!' if self.is_embedded else ''

        if type(self.anchor) == str:
            anchoring = f'#{self.anchor}'
        else:  # self.anchor == 0
            anchoring = ''
          
        if type(self.custom_text) == str:
            if self.link_type == LinkType.WIKILINK:
                customing = fr'|{self.custom_text}'
            else:
                customing = self.custom_text
        else:  # self.custom_text == 0:
            customing = ''
        
        if self.link_type == LinkType.WIKILINK:
            return f'{embedding}[[{self.file_name}{anchoring}{customing}]]'
        else:
            # Markdown links format whitespace with '%20'
            file_name = self.file_name.replace(' ' , '%20')  
            anchoring = anchoring.replace(' ', '%20')
            return fr'{embedding}[{customing}]({file_name}{anchoring})'
    
    def convert_link_type(self, link_type: LinkType) -> ObsidianLink:
        """Returns an equivalent Link object which has the specified
        ``LinkType``.
        
        **Parameters**
        - link_type - ``LinkType``
        """
        # TODO
        return
    
    def displayed_text(self) -> str:
        """Returns the displayed str of this link.
        
        `self.file_name`, `self.custom_text` and `self.anchor` are
        assumed to be not `-1`.
        """
        if self.custom_text:
            return self.custom_text
        else:
            if not self.anchor:
                return self.file_name
            else:
                return f'{self.file_name} > {self.anchor}'

    def is_abstract(self) -> bool:
        """
        Returns `True` if self is abstract, i.e. file_name, anchor,
        or custom_text is `-1`.
        """
        return self.anchor == -1 or self.file_name == -1 or self.anchor == -1
    
