# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../../../nbs/24_markdown.obsidian.personal.machine_learning.notation_identification.ipynb.

# %% auto 0
__all__ = ['add_one_double_asts_to_line', 'notation_data_from_text', 'notation_data_from_note',
           'append_notation_data_to_database', 'automatically_mark_notations']

# %% ../../../../../nbs/24_markdown.obsidian.personal.machine_learning.notation_identification.ipynb 2
import os
from os import PathLike
from pathlib import Path
import pandas as pd
import re
from typing import Optional, Union
import warnings

from fastai.text.learner import TextLearner

from trouver.helper import (
    find_regex_in_text, latex_indices, notation_asterisk_indices,
    defs_and_notats_separations, replace_string_by_indices,
    current_time_formatted_to_minutes
)
from ....markdown.file import MarkdownFile, MarkdownLineEnum
from ..note_processing import process_standard_information_note
from .database_update import append_to_database
from trouver.markdown.obsidian.vault import(
    # all_note_paths_by_name, note_path_by_name,
    VaultNote, NoteDoesNotExistError
)


# %% ../../../../../nbs/24_markdown.obsidian.personal.machine_learning.notation_identification.ipynb 6
def add_one_double_asts_to_line(
        line: str, # The text to which to add the double asterisks `**`
        start: int, # The first double asterisks are added in between `line[start-1]` and `line[start]`.
        end: int # The second double asterisks are added in between `line[end-1]` and `line[end]`.
        ) -> str: # The str obtained from `line` by surrounding the substring `line[start:end]` with double asterisks.
    # TODO: rename to add_one_double_asts_to_line. Better yet, also
    # implement a function which adds multiple double asts.
    """
    Return `line` with only one double asterisks `**` surrounded text.
    
    Used in `_definition_data_from_line`
    """
    return f'{line[:start]}**{line[start:end]}**{line[end:]}'

# %% ../../../../../nbs/24_markdown.obsidian.personal.machine_learning.notation_identification.ipynb 8
def notation_data_from_text(
        with_double_asts: str # May or may not have double asterisks to signify definitions and notations
        ) -> tuple[str, list[tuple[int, int, bool]]]:
    """Extracts data on the locations of notations in a text with
    double asterisks.
    
    Used in `notation_data_from_note`

    **Returns**

    - tuple[str, list[tuple[int, int, bool]]]
        - The str is the str `no_double_asts`, which is the same as
        `with_double_asts`, except with the double asterisks removed.
        - Each list represents a data point for a LaTeX math-mode
          string in `no_double_asts`and consists of

            1. The indices `start, end` where the data point considers
               whether or not the LaTeX math-mode substring
               `line_no_double_asts[start:end]` is surrounded by
               double-asterisks (and hene is supposed to introduce a notation).

            2. A bool which is `True`, if the data-point represents a
               str with double-asterisks surrounding a notation and `False`
               otherwise.
    """
    defs_and_notats = defs_and_notats_separations(with_double_asts)
    only_indices = [(start, end) for start, end, _ in defs_and_notats]
    replace_with = [with_double_asts[start+2:end-2]
                    for start, end in only_indices]
    no_double_asts = replace_string_by_indices(
        with_double_asts, only_indices, replace_with)

    bold_indices_in_no_double_asts = [
        (start - 4*i, end - 4*i - 4, is_notat)
        for i, (start, end, is_notat) in enumerate(defs_and_notats)]

    notation_indices = [(start, end, True) for start, end, is_notat 
                        in bold_indices_in_no_double_asts if is_notat]

    notat_indices_in_no_double_asts = [
        (start, end) for start, end, _ in bold_indices_in_no_double_asts]
    all_latex_indices = latex_indices(no_double_asts)
    non_notat_indices = [tuppy for tuppy in all_latex_indices
                         if tuppy not in notat_indices_in_no_double_asts]
    non_notat_indices = [(start, end, False)
                         for start, end in non_notat_indices]
    
    return no_double_asts, notation_indices + non_notat_indices


# %% ../../../../../nbs/24_markdown.obsidian.personal.machine_learning.notation_identification.ipynb 10
def _notation_data_with_indices(
        note: VaultNote, vault: PathLike) -> tuple[
            MarkdownFile, list[tuple[int, int, bool]]]:
    r"""Obtain notation data from a note including the indices.
    
    Used in `notation_data_from_note`

    **Parameters**
    - note - VaultNote
    - vault - PathLike

    **Returns**
    - str, list[list[str, int, bool]]
        - The str is the str of the processed MarkdownFile except
        without double asterisks.
        - Each list consists of

            1. The indices `start, end` where the data point considers
            whether or not the substring `no_double_asts[start:end]`
            contains a notation.
            2. A bool that is `True` if the LaTeX text contains
            notation.
    """
    # TODO: test
    mf = process_standard_information_note(
        MarkdownFile.from_vault_note(note), vault,
        remove_double_asterisks = False)
    with_double_asts = str(mf)
    no_double_asts, data = notation_data_from_text(with_double_asts)
    return no_double_asts, data

# %% ../../../../../nbs/24_markdown.obsidian.personal.machine_learning.notation_identification.ipynb 11
def notation_data_from_note(
        note: VaultNote, vault: PathLike
        ) -> list[tuple[str, str, bool]]:
    # TODO: Implement the option to include multiple-lines in the data.
    """Obtain notation data from a note.

    Note that the lists of str might not be in any particular order.
    
    **Returns**

    - list[tuple[str, str, bool]]
        - Each list consists of 
            1. The name of `note`,
            2. The processed str of `note` with only a single double
            asterisk surrounded LaTeX text. Note that the processed str
            merges display math mode text into single lines, cf.
            `process_standard_information_note`.
            3. A bool that is `True` if the LaTeX text contains
            notation.
    """
    # TODO: treat '`$`` separately.
    no_double_asts, data = _notation_data_with_indices(note, vault)
    return [
        (note.name,
         add_one_double_asts_to_line(no_double_asts, start, end),
         is_notat) for start, end, is_notat in data]


# %% ../../../../../nbs/24_markdown.obsidian.personal.machine_learning.notation_identification.ipynb 17
def append_notation_data_to_database(
        vault: PathLike, # The vault from which the data is drawn
        file: PathLike,  # The path to a CSV file
        notes: list[VaultNote], # The notes to add to the database
        backup: bool = True # If `True`, makes a copy of `file` in the same directoy and with the same name, except with an added extension of `.bak`.
        ) -> None:
    to_turn_into_a_df = []
    current_time = current_time_formatted_to_minutes()
    for note in notes:
        notation_data_for_note = notation_data_from_note(note,  vault)
        for _, with_one_double_asts, is_notat in notation_data_for_note:
            row_dict = {
                'Time added': current_time,
                'Time modified': current_time,
                'Note name': note.name,
                'LaTeX in text': with_one_double_asts,
                'Is notation': is_notat
            }
            to_turn_into_a_df.append(row_dict)
    df = pd.DataFrame(to_turn_into_a_df)
    append_to_database(
        file, df,
        cols=['Time added', 'Time modified', 'Note name',
              'LaTeX in text', 'Is notation'],
        pivot_column='LaTeX in text',
        columns_to_update=['Time modified', 'Note name', 'Is notation'],
        backup=backup)
    
    

# %% ../../../../../nbs/24_markdown.obsidian.personal.machine_learning.notation_identification.ipynb 21
def automatically_mark_notations(
        vn: VaultNote, # The information note to which to mark notations.
        learn: TextLearner, # The ML model which predicts where notation notes should occur.  This is a classifier which takes as input a str with double asterisks surrounding LaTeX text. The model outputs whether or not the single double asterisk pair surrounds a LaTeX text with notation.
        create_notation_notes: bool = False, # If `True`, creates the notations notes for the predicted notations and links them to the 'See Also' sections of the information notes.
        reference_name: str = '' # The name of the reference that `vn` belongs to; this is only relevant when `create_notation_notes=True` so that the created notation notes have file names starting with the reference name.
        ) -> None:
    # TODO: before running this, make sure to warn or check that this
    # will change contents of files drasticall.
    # TODO: implement `overwrite` parameter
    """Predict and mark where notations occur in a note, and optionally
    create a notation note, and add the notation note to the `See Also`
    section of the note.

    Assumes that no double asterisks are already in the contents of `vn`.

    This function Removes links, headings, footnotes, etc.
    from the original note and merges multi-line display math mode LaTeX
    text into single lines. Use with caution.
    """
    no_double_asts, index_data = _notation_data_with_indices(vn, vn.vault)
    notations_to_add = _get_notation_indices_to_add(
        no_double_asts, index_data, learn)
    with_double_asts = no_double_asts
    for start, end in reversed(notations_to_add):
        with_double_asts = add_one_double_asts_to_line(
            with_double_asts, start, end)

    original_mf = MarkdownFile.from_vault_note(vn)
    _, end_metadata = original_mf.metadata_lines()
    see_also_line = original_mf.get_line_number_of_heading('See Also')
    original_mf.remove_lines(end_metadata + 1, see_also_line)
    original_mf.insert_line(end_metadata + 1, {
        'type': MarkdownLineEnum.HEADING, 'line': '# Topic[^1]'})
    original_mf.add_line_in_section('Topic[^1]', {
        'type': MarkdownLineEnum.DEFAULT, 'line': with_double_asts})
    original_mf.write(vn)

    # if create_notation_notes:
    #     make_notation_notes_from_double_asts(vn, vn.vault, reference_name)


def _get_notation_indices_to_add(
        no_double_asts: str, index_data: list[list[int, bool]],
        learn: TextLearner)\
            -> list[tuple[int]]:
    """Used in `automatically_add_notations`"""
    to_test = [add_one_double_asts_to_line(no_double_asts, start, end)
                       for start, end, is_notat in index_data if not is_notat]
    predictions = [learn.predict(one_double_ast) for one_double_ast in to_test]
    notations_to_add = [
        (start, end) for (start, end, is_notat), prediction
        in zip(index_data, predictions) if is_notat or prediction[0] == 'True']
    notations_to_add.extend([
        (start, end) for (start, end, is_notat) in index_data if is_notat])
    notations_to_add.sort()
    return notations_to_add

