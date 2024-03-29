# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../../../nbs/26_markdown.obsidian.personal.machine_learning.definition_identification.ipynb.

# %% auto 0
__all__ = ['definitions_in_text', 'definition_identification_data_from_note', 'gather_definition_identification_data']

# %% ../../../../../nbs/26_markdown.obsidian.personal.machine_learning.definition_identification.ipynb 2
import os 
from os import PathLike
from pathlib import Path
from typing import Union

import pandas as pd

from .....helper import current_time_formatted_to_minutes, definition_asterisk_indices
from ....markdown.file import MarkdownFile
from ..note_processing import process_standard_information_note
from ...vault import VaultNote

# %% ../../../../../nbs/26_markdown.obsidian.personal.machine_learning.definition_identification.ipynb 5
def definitions_in_text(
        text: str
        ) -> list[str]:
    """
    Return the list of str with the definitions in the text.
    """
    indices = definition_asterisk_indices(text)
    return [text[start+2:end-2] for start, end in indices]

# %% ../../../../../nbs/26_markdown.obsidian.personal.machine_learning.definition_identification.ipynb 7
# TODO: implement a measure to not get the definition identification data, e.g. by 
# detecting a `_auto/definition_identification` tag.
def definition_identification_data_from_note(
        note: VaultNote,
        vault: PathLike
        ) -> Union[dict[str, str], None]: # The keys to the dict are "Note name", "Raw text", "Definitions". However, `None` is returned if `note` does not exist.
    """Obtain definition identification data from the information note.

    """
    if not note.exists():
        return None
    mf = MarkdownFile.from_vault_note(note)
    mf = process_standard_information_note(
        mf, vault, remove_double_asterisks=False)
    mf_text = str(mf)
    definitions = definitions_in_text(mf_text)
    raw_text = mf_text.replace('**', '') 
    return {
        "Note name": note.name,
        "Raw text": raw_text,
        "Definitions": definitions}

# %% ../../../../../nbs/26_markdown.obsidian.personal.machine_learning.definition_identification.ipynb 9
def gather_definition_identification_data(
        vault: PathLike,
        notes: list[VaultNote]
        ) -> pd.DataFrame: # 
    """
    Return a `pandas.DataFrame` encapsulating the data of definition
    identifications.
    
    cf. `definition_identification_data_from_note`, which is the function
    with which the definition identification data is drawn.
    
    This function is mainly used in
    `append_to_definition_identification_database`.
    """
    definition_identification_data = [
        definition_identification_data_from_note(note, vault) for note in notes]
    definition_identification_data = [
        row for row in definition_identification_data
        if row is not None]
    current_time = current_time_formatted_to_minutes()
    for row in definition_identification_data:
        row['Time added'] = current_time
        row['Time modified'] = current_time
    return pd.DataFrame(definition_identification_data)

# %% ../../../../../nbs/26_markdown.obsidian.personal.machine_learning.definition_identification.ipynb 11
#| export
