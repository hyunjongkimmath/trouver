# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../../nbs/13_markdown.obsidian.personal.notes.ipynb.

# %% auto 0
__all__ = ['notes_linked_in_note', 'notes_linked_in_notes_linked_in_note']

# %% ../../../../nbs/13_markdown.obsidian.personal.notes.ipynb 2
from typing import Union

from trouver.markdown.markdown.file import (
    MarkdownFile
)
from trouver.markdown.obsidian.links import (
    links_from_text
)
from trouver.markdown.obsidian.vault import (
    VaultNote
)


# %% ../../../../nbs/13_markdown.obsidian.personal.notes.ipynb 5
def notes_linked_in_note(
        list_note: VaultNote, # The `VaultNote` in which to find the links.
        as_dict: bool = True # If `True`, returns a dict. Returns a list otherwise.
        ) -> Union[dict[str, VaultNote], list[VaultNote]]: # If dict, the keys are the names of the vault notes and the values are the `VaultNote` objects. If list, then the entries are the `VaultNote` objects.
    """Returns a list or dict of VaultNotes of notes linked by 
    a specified note.
    """
    text = list_note.text()
    links = links_from_text(text)
    if as_dict:
        return {link.file_name: VaultNote(list_note.vault, name=link.file_name) for link in links}
    else:
        return [VaultNote(list_note.vault, name=link.file_name) for link in links]


def notes_linked_in_notes_linked_in_note(
    list_note: VaultNote, # The `VaultNote` with links to notes containing the links to obtain.
    as_dict: bool = True # If `True`, returns a dict. Returns a list otherwise. 
    ) -> Union[dict[str, VaultNote], list[VaultNote]]: # If dict, the keys are the names of the vault notes and the values are the `VaultNote` objects. If list, then the entries are the `VaultNote` objects.
    """Returns a list or dict of VaultNotes of notes 
    linked by notes which are linked by a specified note.
    """
    linked_in_list_note = notes_linked_in_note(list_note, as_dict=False)
    notes_for_each_note = [notes_linked_in_note(note, as_dict=True) 
                           for note in linked_in_list_note]
    all_notes = {}
    for notes_for_note in notes_for_each_note:
        for name, note in notes_for_note.items():
            all_notes[name] = note
    if as_dict:
        return all_notes
    else:
        return [note for _, note in all_notes.items()]     