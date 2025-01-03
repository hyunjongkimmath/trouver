"""Functions involving both the vault and links"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../../nbs/50_markdown.obsidian.vault_and_links.ipynb.

# %% auto 0
__all__ = ['all_custom_text_for_links_in_vault', 'all_links_in_vault']

# %% ../../../../nbs/50_markdown.obsidian.vault_and_links.ipynb 2
from os import PathLike
from pathlib import Path
import re
from typing import Union

from ....helper.files_and_folders import text_from_file
from ....markdown.obsidian.vault import VaultNote, all_paths_to_notes_in_vault
from ....markdown.obsidian.links import ObsidianLink, LinkType, links_from_text, LinkFormatError

# %% ../../../../nbs/50_markdown.obsidian.vault_and_links.ipynb 4
def all_custom_text_for_links_in_vault(
        note: VaultNote, # The note to find the custom text for.
        vault: PathLike, # The path to the Obsidian vault directory
        anchor: Union[str, int] = -1 # The anchor in the note to find the custom text for. If 0, then returns only the custom texts for internal links without anchors. If -1, then returns the custom texts for all of the internal links of the specified note.
        ) -> dict[Union[str, int], str]: # Each key is the custom text used and each value is a set of paths relative to `vault` to the notes where the custom text is used.  The key `0` means that no custom text is used.
    """
    Return all custom text used in the Obsidian vault for the specified
    note and anchor.
    """
    vault = Path(vault)
    name = note.name
    wiki_gen = ObsidianLink(
        is_embedded=False, file_name=name, anchor=anchor, custom_text=-1,
        link_type=LinkType.WIKILINK)
    wiki_regex = wiki_gen.to_regex()
    mark_gen = ObsidianLink(
        is_embedded=False, file_name=name, anchor=anchor, custom_text=-1,
        link_type=LinkType.MARKDOWN)
    mark_regex = mark_gen.to_regex()
    regex = f'{wiki_regex}|{mark_regex}'
    all_note_paths = all_paths_to_notes_in_vault(vault)
    # I am creating a generator as opposed to a list so that the program
    # does not store the contents of all the text files.
    texts = ((path, text_from_file(vault / path, encoding='utf8'))
             for path in all_note_paths)
    regex_object = re.compile(regex)
    custom_text_usage = {}
    for path, text in texts:
        custom_texts = _custom_text_for_links_in_text(text, regex_object)
        for custom_text in custom_texts:
            if custom_text not in custom_text_usage:
                custom_text_usage[custom_text] = set()
            custom_text_usage[custom_text].add(path)
    return custom_text_usage


def _custom_text_for_links_in_text(
        text: str, regex_object: re.Pattern) -> list[str]:
    """Helper function for finding custom text for links in a single file.
    
    **Parameters**
    - text - str
    - regex_object - re.Pattern
        - An object returned with the `re.compile` function. Matches
        wikilinks and markdown links.
        
    **Returns**
    - list[str]
    """
    link_matches = regex_object.finditer(text)
    match_ranges = [match.span() for match in link_matches]
    links = [ObsidianLink.from_text(text[start:end])
             for start, end in match_ranges]
    return [link.custom_text for link in links]

# %% ../../../../nbs/50_markdown.obsidian.vault_and_links.ipynb 6
def all_links_in_vault(
        vault: PathLike, backlinks: bool = False, 
        multiplicities: bool = False) -> dict[str, list[str]]:
    """Returns a dict keeping track of which notes contain 
    links to which notes.
    
    TODO: currently, the regex capture regex code. Change them
    so that this does not happen.
    
    **Parameters**
    - vault - PathLike
    - backlinks - bool
        - If `True`, then keeps track of the links in each note.
        If `False`, then keeps track of the backlinks in each note,
        i.e. which other notes link to each note. Defaults to `False`.
    - multiplicties - bool
        - If `True`, then keeps track of multiple links to the same note
        for each note. Otherwise, only keeps track of whether or not
        a note links to a(nother) note. Defaults to `False`.
  
    **Returns**
    - dict[str, list[str]]
        - Each key is a str, referring to the name of a note. 
        Each corresponding value is a list. The list contains 
        the names of all the notes which the key note references to if
        `backlinks` is `True`, and contains the names of all the notes which
        reference the key note if `backlinks` is `False`. The list can contain
        multiple occurrences of the same note if `multiplicities` is `True`.
    """
    vault = Path(vault)
    all_note_paths = all_paths_to_notes_in_vault(vault, as_dict=True)
    links = {}
    for name, path in all_note_paths.items():
        text = text_from_file(vault / path, encoding='utf8')
        try:
            links_in_note = links_from_text(text)
        except LinkFormatError:
            print(name)
        if not multiplicities:
            links_in_note = set(links_in_note)
        if backlinks:
            if name not in links:
                links[name] = []
            for link in links_in_note:
                if link.file_name not in links:
                    links[link.file_name] = []
                links[link.file_name].append(name)
        else:
            if name not in links:
                links[name] = []
            links[name] += [link.file_name for link in links_in_note]
    return links
