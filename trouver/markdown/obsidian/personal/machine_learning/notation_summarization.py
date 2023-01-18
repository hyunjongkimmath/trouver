# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb.

# %% auto 0
__all__ = ['get_latex_in_original_from_parsed_notation_note_data', 'notation_summarization_data_from_note',
           'gather_notation_note_summaries', 'append_to_notation_note_summarization_database', 'single_input',
           'append_column_for_single_text', 'summarize_notation', 'fix_summary_formatting',
           'append_summary_to_notation_note']

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 3
import os
from os import PathLike
from typing import Union

import pandas as pd
from transformers import pipeline

from .....helper import current_time_formatted_to_minutes
from ....markdown.file import MarkdownFile
from .database_update import append_to_database
from ..note_processing import process_standard_information_note
from ..notation import parse_notation_note
from ..note_type import note_is_of_type
from ...vault import VaultNote

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 8
def get_latex_in_original_from_parsed_notation_note_data(
        metadata: dict[str],
        notation_str: str) -> str:
    """Return the string that should be considered the `latex_in_original`
    given part of the output of `parse_notation_note`

    `latex_in_original` is intended to either be 
    1. a substring of the main note in which the notation is introduced, 
       if available, or 
    2. the notation itself.

    If the notation note has a `latex_in_original` field in its YAML
    frontmatter metadata, then the (first) str there is the
    `latex_in_original`. 
    """
    if metadata is not None and 'latex_in_original' in metadata:
        latex_in_original = metadata['latex_in_original']
        if isinstance(latex_in_original, list):
            latex_in_original = latex_in_original[0]
    else:
        # latex_in_original = None 
        latex_in_original = notation_str
    return latex_in_original

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 10
def _notation_note_has_auto_summary_tag(
        metadata: Union[dict[str], None]
        ) -> bool:
    """
    Return `True` if the metadata parsed from the notation note
    has an auto tag in its YAML frontmatter meta.

    This is a helper function of `notation_summarization_data_from_note`.
    """
    return metadata and 'tags' in metadata and '_auto/notation_summary' in metadata['tags']

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 12
def notation_summarization_data_from_note(
        notation_note: VaultNote,
        vault: PathLike
        ) -> Union[dict[str, str], None]: # The keys to the dict are "Notation note name", "Notation", "Latex in oiriginal", "Summary", and "Main note name". However, `None` is returned instead of a `dict` if the notation note is determined to have not been summarized, if the main note of the notation note does not exist, or the notation note is marked with the `_auto/notation_summary` tag.
    """Obtain notation summzarization data from the notation note.

    `None` is returned instead of a `dict if

    1. the notation is determined to have not been (fully) summarized,
       - Currently, this is implemented as follows: a notation note
         is not fully summarized if it does not have any content
         beyond `<notation> denotes ` or if the notation note has
         `#_meta/TODO` marked in its content
         (except in the trailing bulleted list of notations used
          in the notation note)
    2. the main note of the notation not does not exist or
       is essentially empty
       - Essentially empty means that the
         `process_standard_information_note` function applied to the
         a `MarkdownFile` object of the main note yields a
         `MarkdownFile` object whose `__str__` method returns a
         string of only blank characters.
    3. the notation note is marked with an `_auto/notation_summary` tag
       in its YAML frontmatter meta.
       - If a notation note is marked with an `_auto/notation_summary`
         tag, then that means that its summary has been auto-generated
         by an ML model using the `append_summary_to_notation_note`
         function

    The notion of whether the notation "has been summarized" is not
    exactly implemented, but should be sufficient for gathering
    data.

    This function is mainly used in `gather_notation_note_summaries`.

    TODO: there are some notation notes drawing information from
    multiple notes; separate text in notation notes corresponding
    to each note.

    **Returns**

    - Union[dict[str, str], None]

        - If the notation note is determined to have been summarized
          (i.e. contains text beyond `<notation> denotes ` and does not
          have the `#_meta/TODO` tag) then the output is a `dict` whose
          key-value pairs are
            - `"Notation note name"` - The name of the notation note
            - `"Notation"` - The notation of the note
            - `"Latex in original"' - The entry of the `latex_in_original`
              field of the note if available, cf. `make_a_notation_note`
            - `"Summary"` - The summary of the notation.
            - `"Main note name"` - The name of the main note of the
              notation note
            - `"Processed main note contents"` - The processed contents of the
              main note
        - Otherwise, the output is `None.
    """
    metadata, notation_str, main_of_notation, main_mf, _ = parse_notation_note(notation_note, vault)
    if not _notation_has_been_summarized(main_mf):
        return None
    if _notation_note_has_auto_summary_tag(metadata):
        return None

    latex_in_original = get_latex_in_original_from_parsed_notation_note_data(
        metadata, notation_str)

    process_standard_information_note(main_mf, vault)
    processed_summary = str(main_mf)
    if len(processed_summary.strip()) == 0:
        return None

    if main_of_notation is None:
        return None
    main_note = VaultNote(vault, name=main_of_notation)
    if not main_note.exists():
        return None
    main_note_mf = MarkdownFile.from_vault_note(main_note)
    process_standard_information_note(main_note_mf, vault)

    return {"Notation note name": notation_note.name,
            "Notation": notation_str,
            "Latex in original": latex_in_original,
            "Summary": processed_summary,
            "Main note name": main_of_notation,
            "Processed main note contents": str(main_note_mf)}


def _notation_has_been_summarized(
        main_mf: VaultNote
        ) -> bool:
    text = str(main_mf).strip()
    return len(text) > 0 and '#_meta/TODO' not in text



# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 20
def gather_notation_note_summaries(
        vault: PathLike,
        notes: list[VaultNote]
        ) -> pd.DataFrame: # Has columns `Time added`, `Time modified`, `Notation note name`, `Notation`, `Latex in original`, 'Summary', 'Main note name', and 'Processed main note contents'. 
    """
    Return a `pandas.DataFrame` encapsulating the data of notation note
    summaries.

    cf. `notation_summarization_data_from_note`, which is the function
    from which the notation note summaries are drawn.

    This function is mainly used in
    `append_to_notation_note_summarization_database`.
    """
    summary_data = [
        notation_summarization_data_from_note(note, vault) for note in notes]
    summary_data = [row for row in summary_data if row is not None]
    current_time = current_time_formatted_to_minutes()
    for row in summary_data:
        row['Time added'] = current_time
        row['Time modified'] = current_time
    return pd.DataFrame(summary_data)
    

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 23
def append_to_notation_note_summarization_database(
        vault: PathLike, # The vault freom which the data is drawn
        file: PathLike, # The path to a CSV file
        notes: list[VaultNote], # the notation notes to consider adding to the database. 
        backup: bool = True # If `True`, makes a copy of `file` in the same directory and with the same name, except with an added extension of `.bak`.
        ) -> None:
    """
    Either create a `csv` file containing data for information note type
    labels or append to an existing `csv` file.

    The columns of the database file are as follows:

    - `Time added` - The time when the row was added.
    - `Time modified` - The time when the labels of the row 
    - `Notation note name` - The name of the note from which the data for the row
      was derived.
    - 'Notation' - The notation which is being summarized
    - 'Latex in original' - The entry of the `latex_in_original` field of the
      note if available, cf. `make_a_notation_note`
    - `"Summary"` - The summary of the notation.
    - `"Main note name"` - The name of the main note of the
      notation note
    - `"Processed main note contents"` - The processed contents of the
      main note

    All timestamps are in UTC time and specify time to minutes
    (i.e. no seconds/microseconds).
    
    TODO: implement updating rows and rewrite the next paragraph to
    accurately reflect the implementation. I would like the 'Notation', 'Latex in original',
    'Summary', 'processed main note contents' to be the "pivot_cols"

    If a "new" note has the same processed content as a pre-existing
    note and anything is different about the "new" note, then update
    the row of the existing note. In particular, the following are updated:
    - Time modified (set to current time)
    - Notation (overwritten)
    - Latex in original (overwritten)
    - Summary (overwritten)
    - Main note name (overwritten)
    - Processed main note contents (overwritten)
    
    This method assumes that all the processed content in the
    CSV file are all distinct if the CSV file exists.
    """
    if not notes:
        return
        file = Path(file)
    df = pd.read_csv(file) if os.path.exists(file) else None
    # start_ID_from = max_ID(df) + 1 if not df is None else 1
    new_df = gather_notation_note_summaries(vault, notes)
    if new_df.empty:
        return
    cols = [
        'Time added', 'Time modified', 'Notation note name',
        'Notation', 'Latex in original', 'Summary', 'Main note name',
        'Processed main note contents']
    cols_to_update = [
      'Time modified', 'Notation note name', 'Notation', 'Latex in original', 'Summary', 'Main note name']
    append_to_database(
        file, new_df, cols, 'Processed main note contents', cols_to_update, backup)

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 24
def append_to_notation_note_summarization_database(
        vault: PathLike, # The vault freom which the data is drawn
        file: PathLike, # The path to a CSV file
        notes: list[VaultNote], # the notation notes to consider adding to the database. 
        backup: bool = True # If `True`, makes a copy of `file` in the same directory and with the same name, except with an added extension of `.bak`.
        ) -> None:
    """
    Either create a `csv` file containing data for information note type
    labels or append to an existing `csv` file.

    The columns of the database file are as follows:

    - `Time added` - The time when the row was added.
    - `Time modified` - The time when the labels of the row 
    - `Notation note name` - The name of the note from which the data for the row
      was derived.
    - 'Notation' - The notation which is being summarized
    - 'Latex in original' - The entry of the `latex_in_original` field of the
      note if available, cf. `make_a_notation_note`
    - `"Summary"` - The summary of the notation.
    - `"Main note name"` - The name of the main note of the
      notation note
    - `"Processed main note contents"` - The processed contents of the
      main note

    All timestamps are in UTC time and specify time to minutes
    (i.e. no seconds/microseconds).
    
    TODO: implement updating rows and rewrite the next paragraph to
    accurately reflect the implementation. I would like the 'Notation', 'Latex in original',
    'Summary', 'processed main note contents' to be the "pivot_cols"

    If a "new" note has the same processed content as a pre-existing
    note and anything is different about the "new" note, then update
    the row of the existing note. In particular, the following are updated:
    - Time modified (set to current time)
    - Notation (overwritten)
    - Latex in original (overwritten)
    - Summary (overwritten)
    - Main note name (overwritten)
    - Processed main note contents (overwritten)
    
    This method assumes that all the processed content in the
    CSV file are all distinct if the CSV file exists.
    """
    if not notes:
        return
        file = Path(file)
    df = pd.read_csv(file) if os.path.exists(file) else None
    # start_ID_from = max_ID(df) + 1 if not df is None else 1
    new_df = gather_notation_note_summaries(vault, notes)
    if new_df.empty:
        return
    cols = [
        'Time added', 'Time modified', 'Notation note name',
        'Notation', 'Latex in original', 'Summary', 'Main note name',
        'Processed main note contents']
    cols_to_update = [
      'Time modified', 'Notation note name', 'Notation', 'Latex in original', 'Summary', 'Main note name']
    append_to_database(
        file, new_df, cols, 'Processed main note contents', cols_to_update, backup)

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 33
def single_input(
        main_note_content: str, # The text from which to summarize a notation
        latex_in_original: str, # A substring in main_note_content which is a latex string in which the notation is introduced.
        ) -> str: 

    return f"{main_note_content}\n\nlatex_in_original: {latex_in_original}"

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 36
# TODO: I wonder if I should also keep text that doesn't take 
# Latex in original but rather the notation itself.
def append_column_for_single_text(
        df: pd.DataFrame # Assumed to be structured just as a dataframe of a CSV file created/modified by append_to_notation_note_summarization_database``
        ) -> None:
    """Append a column `"Single text"` to the notation note summarization
    DataFrame to represent the input into an ML model as a single text
    """
    single_text_column = df.apply(
        lambda row: single_input(row["Processed main note contents"], row["Latex in original"]), axis=1)
    df["Single text"] = single_text_column

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 42
def summarize_notation(
        main_content: str,
        latex_in_original: str,
        summarizer,
        ) -> str:
    """Summarize a notation introduced in a mathematical text using
    a huggingface pipeline.

    Assumes that `main_content` is a mathematical text introducing
    a notation and that `latex_in_original` is a substring of
    `main_content` in which a notation is introduced.
    """
    summarizer_output = summarizer(
        single_input(main_content, latex_in_original))
    return summarizer_output[0]['summary_text']


# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 44
def fix_summary_formatting(
        summary: str
        ) -> str:
    """Fix some latex formatting issues in a summarized text
    """
    summary = summary.replace(r'\ ', '\\')
    summary = summary.replace(r'{ ', r'{')
    # TODO: do $ <latex_string> $ into $<latex_stinrg>$
    # TODO: if the replacement of r'\ ' by '\\' happesn to
    # make `\` stick to the previous chunk of things
    # (e.g. r'd\in\mathbb{Z}_{\geq 0}`, then give it some
    # space, e.g. r'd \in \mathbb{Z}_{\geq 0}'.
    return summary



# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 47
def append_summary_to_notation_note(
        main_note: VaultNote,
        notation_note: VaultNote,
        vault: PathLike,
        summarizer
    ) -> None:
    """Summarize a notation introduced in a mathematical text
    using a huggingface pipeline and append said summarization to
    `notation_note`.

    If `notation_note` does not have a YAML frontmatter meta or
    does not have a `latex_in_original` field in its YAML frontmatter
    meta, then the actual notation is used as the `latex_in_original`.

    If `notation_note` already has some content,
    then it is ignored.

    If an auto-generated summary is appended, then this function
    adds an `_auto/notation_summary` tag to the notation note's
    YAML frontmatter. This tag is intended to be used as follows:

    - The presence of this tag tells the reader that the summary
      has been autogenerated by this function.
    - The `notation_summarization_data_from_note` function (and
      by extension, the `gather_notation_note_summaries` and
      `append_to_notation_note_summarization_database` functions)
      avoids gathering notation summarization data from notation
      notes marked with this tag
    - The owner of the `Obsidian.md` vault can manually make
      modifications to the notation note if necessary and remove this
      tag to indicate that the summary is appropriate to be added
      to the note summarization database.
    """
    metadata, notation_str, main_of_notation, main_mf, _ = parse_notation_note(notation_note, vault)

    latex_in_original = get_latex_in_original_from_parsed_notation_note_data(
        metadata, notation_str)
    
    main_mf = MarkdownFile.from_vaultNote(main_note)
    process_standard_information_note(main_mf, vault)
    main_content = str(main_mf)
    if len(main_content.strip()) != 0:
        # TODO: warn that the notation note already had
        # contents, so no new ones were added.
        return
    summarization = summarize_notation(
        main_content, latex_in_original, summarizer)
    summarization = fix_summary_formatting(summarization)
    # TODO Append to notation note
    # TODO add _auto/notation_summary tag
    


