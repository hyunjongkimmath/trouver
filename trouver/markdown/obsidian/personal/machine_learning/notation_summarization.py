"""Functions for summarizing notations"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb.

# %% auto 0
__all__ = ['get_latex_in_original_from_parsed_notation_note_data', 'notation_summarization_data_from_note',
           'gather_notation_note_summaries', 'append_to_notation_note_summarization_database',
           'single_input_for_notation_summarization', 'append_column_for_single_text', 'summarize_notation',
           'append_summary_to_notation_note']

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 3
import os
from os import PathLike
from pathlib import Path
import re
from typing import Optional, Union

import pandas as pd
from transformers import pipeline, pipelines

from .....helper.date_and_time import current_time_formatted_to_minutes
from .....helper.latex import reduce_unnecessary_spaces, _list_of_candidates_from_math_mode_strings, correct_latex_syntax_error, fix_autogen_formatting
from ....markdown.file import MarkdownFile, MarkdownLineEnum
from ...links import ObsidianLink
from .database_update import append_to_database
from ..note_processing import process_standard_information_note
from ..notation import _notation_string_no_metadata, _raw_notation
from ..notation.parse import main_of_notation, parse_notation_note
from ..note_type import note_is_of_type
from ...vault import VaultNote

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 7
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

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 9
def _notation_note_has_auto_summary_tag(
        metadata: Union[dict[str], None]
        ) -> bool:
    """
    Return `True` if the metadata parsed from the notation note
    has an auto tag in its YAML frontmatter meta.

    This is a helper function of `notation_summarization_data_from_note`.
    """
    return metadata and 'tags' in metadata and '_auto/notation_summary' in metadata['tags']

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 11
def notation_summarization_data_from_note(
        notation_note: VaultNote,
        vault: PathLike,
        # gather_data_for_blank_content_notation_notes: bool = False,
        check_for_actual_summarization: bool = True # If `True`, then return `None` if `notation_note` is determined to not have a summary or if the summary is autogenerated.
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

        - If `check_for_actual_summarization` is `False` or
          the notation note is determined to have been summarized
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
    if check_for_actual_summarization and not _notation_has_been_summarized(main_mf):
        return None
    if check_for_actual_summarization and _notation_note_has_auto_summary_tag(metadata):
        return None

    latex_in_original = get_latex_in_original_from_parsed_notation_note_data(
        metadata, notation_str)

    process_standard_information_note(main_mf, vault)
    processed_summary = str(main_mf)
    if check_for_actual_summarization and len(processed_summary.strip()) == 0:
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


# TODO: Test the case of `check_for_actual_summarization` is `False`

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 21
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
    

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 24
def append_to_notation_note_summarization_database(
        vault: PathLike, # The vault freom which the data is drawn
        file: PathLike, # The path to a CSV file
        notes: list[VaultNote], # the notation notes to consider adding to the database. 
        backup: bool = True # If `True`, makes a copy of `file` in the same directory and with the same name, except with an added extension of `.bak`.
        ) -> None:
    """
    Either create a `csv` file containing data for notation note
    summarization or append to an existing `csv` file.

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
      'Time modified', 'Processed main note contents', 'Notation', 'Latex in original', 'Summary', 'Main note name']
    append_to_database(
        file, new_df, cols, 'Notation note name', cols_to_update, backup)
# TODO: think about whether the 'Notation note name' column would make for an
# appropriate pivot.

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 33
def single_input_for_notation_summarization(
        main_note_content: str, # The mathematical text that introduces the notation and from which to summarize a notation.
        latex_in_original: str, # A substring in main_note_content which is a latex string in which the notation is introduced.
        latex_in_original_comes_first: bool = True # If `True`, the `latex_in_original` piece appears before the `main_note_content`
        ) -> str:
    """
    Format an input for a
    `transformers.pipelines.text2text_generation.SummarizationPipeline`
    object to summarize a notation introduced in a mathematical text.

    The input consists of `main_note_content` as well as a part that is formatted as
    `f"latex_in_original: {latex_in_original}"`.

    Note that this function is used to format data used to train/validate
    the summarization model within the `SummarizationPipeline`.
    """
    if latex_in_original_comes_first:
        return f"latex_in_original: {latex_in_original}\n\n{main_note_content}"
    else:
        return f"{main_note_content}\n\nlatex_in_original: {latex_in_original}"

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 40
# TODO: I wonder if I should also keep text that doesn't take 
# Latex in original but rather the notation itself.
def append_column_for_single_text(
        df: pd.DataFrame, # Assumed to be structured just as a dataframe of a CSV file created/modified by append_to_notation_note_summarization_database``
        latex_in_original_comes_first: bool = True # This is a parameter to pass to calls to the `single_input_for_notation_summarization` function. If `True`, the `latex_in_original` piece appears before the `main_note_content`
        ) -> None:
    """Append a column `"Single text"` to the notation note summarization
    DataFrame to represent the input into an ML model as a single text
    """
    single_text_column = df.apply(
        lambda row: single_input_for_notation_summarization(
            row["Processed main note contents"], row["Latex in original"],
            latex_in_original_comes_first),
        axis=1)
    df["Single text"] = single_text_column

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 47
def summarize_notation(
        main_content: Union[str, MarkdownFile],
        latex_in_original: str,
        summarizer: pipelines.text2text_generation.SummarizationPipeline,
        fix_formatting: bool = True, # If `True`, run `fix_autogen_formatting` on `summarizer`'s summary before retuning it.
        latex_in_original_comes_first: bool = True, # This is a parameter to pass to calls to the `single_input_for_notation_summarization` function. If `True`, the `latex_in_original` piece appears before the `main_note_content`
        correct_syntax_error: bool = True # If `True`, attempt to correct latex syntax error 
        ) -> str:
    """Summarize a notation introduced in a mathematical text using
    a huggingface pipeline.

    Assumes that `main_content` is a mathematical text introducing
    a notation and that `latex_in_original` is a substring of
    `main_content` in which a notation is introduced.

    By setting `correct_latex_syntax_error` to `True`, this function
    consider each math mode text in the generated summary, and attempts
    to, if not syntactically correct, replace it with a math mode text
    closely resembling it within `main_content`. More specifically,
    each math mode text within `main_content` is considered, and
    substrings within those math mode texts are considered. The
    syntactically correct substring (Determined via
    `math_mode_string_is_syntactically_valid`) that also most closely
    resembles (determined via Levenshtein distance) the math mode text
    originally in the generated summary.
    """
    summarizer_output = summarizer(
        single_input_for_notation_summarization(
            main_content, latex_in_original, latex_in_original_comes_first))
    summary = summarizer_output[0]['summary_text']
    if correct_syntax_error:
        # TODO: do the below
        replacement_candidates = _list_of_candidates_from_math_mode_strings(str(main_content))
        summary = correct_latex_syntax_error(summary, replacement_candidates)
    if fix_formatting:
        summary = fix_autogen_formatting(summary)
    return summary

# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 50
def append_summary_to_notation_note(
        notation_note: VaultNote,
        vault: PathLike,
        summarizer: pipelines.text2text_generation.SummarizationPipeline, # Contains an ML model which summarizes the notation, see `summarize_notation` function.
        main_note: Optional[VaultNote] = None, # The main note from which the notation comes from. If this is `None`, then the `main_note` is obtained via the `main_of_notation` function.
        overwrite_previous_autogenerated_summary: bool = False, # If `True`, overwrite previously autogenerated summaries
        latex_in_original_comes_first: bool = True # This is a parameter to pass to calls to the `single_input_for_notation_summarization` function. If `True`, the `latex_in_original` piece appears before the `main_note_content`. While the default value of `True` is recommended, passing `False` to this parameter may be necessary to use the older version of the summarization model in the repo [`notation_summarizations_model`](https://huggingface.co/hyunjongkimmath/notation_summarizations_model).
    ) -> None:
    """Summarize a notation introduced in a mathematical text
    using a huggingface pipeline and append said summarization to
    `notation_note`.

    If `notation_note` does not have a YAML frontmatter meta or
    does not have a `latex_in_original` field in its YAML frontmatter
    meta, then the actual notation is used as the `latex_in_original`.

    The following describes the circumstances under which the
    summarization does not happen:

    - If `main_note` is `None` and no main note of `notation_note` can
    be determined via the `main_of_notation` function.
    - If `overwrite_previous_autogenerated_summary` is `False` and
    `notation_note` has the `_auto/notation_summary` tag in its
    YAML frontmatter meta (if available).
    - If `notation_note` does not have a YAML frontmatter meta or 
    the `_auto/notation_summary` tag is not present in the
    YAML frontmatter meta and `notation_note` has nontrivial
    content (i.e. its content is not merely of the form
    `$<notation>$ [[<link_to_main_note|denotes]]`).

    If an auto-generated summary is appended, then this function
    adds an `_auto/notation_summary` tag to the notation note's
    YAML frontmatter, if not already present.
    This tag is intended to be used as follows:

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
    metadata, notation_str, main_note_name,\
        notation_note_content_mf, _\
        = parse_notation_note(notation_note, vault)
    summary_should_be_generated, main_mf = _summary_should_be_generated(
        main_note, main_note_name, vault,
        overwrite_previous_autogenerated_summary,
        metadata, notation_note_content_mf)
    if not summary_should_be_generated:
        return
    summary = _get_summary(
        metadata, notation_str, main_mf, summarizer,
        latex_in_original_comes_first)
    _write_summary_to_notation_note(notation_note, summary)


def _summary_should_be_generated(
        main_note: Union[VaultNote, None],
        main_note_name: str,
        vault: PathLike,
        overwrite_previous_autogenerated_summary: bool,
        metadata: Union[dict, None],
        notation_note_content_mf: MarkdownFile
        ) -> tuple[bool, Union[MarkdownFile, None]]:
    """This is a helper function of `append_summary_to_notation_note`.
    
    **Returns**
    - `tuple[bool, Union[MarkdownFile, None]]`
        - the `bool` is `True` if a new summary should be generated. The
        `MarkdownFile` is the processed `MarkdownFile` of `main_note`.
    """
    if main_note is None and main_note_name is not None:
        main_note = VaultNote(vault, name=main_note_name)

    if main_note is None:
        return False, None
    main_mf = MarkdownFile.from_vault_note(main_note)
    process_standard_information_note(main_mf, vault)
    if (not overwrite_previous_autogenerated_summary 
            and _metadata_dict_has_auto_notation_summary_tag(metadata)):
        return False, main_mf
    notation_note_content = str(notation_note_content_mf)
    if (not _metadata_dict_has_auto_notation_summary_tag(metadata)
            and len(notation_note_content.strip()) != 0):
        # TODO: warn that the notation note already had
        # contents, so no new ones were added.
        return False, main_mf
    return True, main_mf



def _get_summary(
        metadata,
        notation_str,
        main_mf,
        summarizer,
        latex_in_original_comes_first: bool) -> str:
    """
    This is a helper function of `append_summary_to_notation_note`.
    """
    latex_in_original = get_latex_in_original_from_parsed_notation_note_data(
        metadata, notation_str)
    summary = summarize_notation(
        main_mf, latex_in_original, summarizer, latex_in_original_comes_first)
    return summary


def _write_summary_to_notation_note(
        notation_note: VaultNote, summary: str) -> None:
    """
    Add `summary` to `notation_note`, replacing an already existing summary
    if necessary.
    This is a helper function of `append_summary_to_notation_note`.

    """
    _, raw_notation, main_note_name, _, _ = parse_notation_note(notation_note)
    raw_notation = _raw_notation(raw_notation)
    without_metadata = _notation_string_no_metadata(
        raw_notation,
        ObsidianLink.from_text(f'[[{main_note_name}|denotes]]'),
        summary)
    notation_note_mf = MarkdownFile.from_vault_note(notation_note)
    _, end_metadata_line = notation_note_mf.metadata_lines()
    notation_note_mf.parts = notation_note_mf.parts[:end_metadata_line+1]
    notation_note_mf.add_line_to_end({'line': without_metadata, 'type': MarkdownLineEnum.DEFAULT})

    notation_note_mf.add_tags(
        ['_auto/notation_summary'],
        enquote_entries_in_metadata_fields=['latex_in_original'])
    notation_note_mf.write(notation_note)


def _metadata_dict_has_auto_notation_summary_tag(
        metadata: Union[dict, None]):
    """
    This is a helper function of `append_summary_to_notation_note`.
    """
    return (metadata is not None
            and 'tags' in metadata
            and '_auto/notation_summary' in metadata['tags'])
    


    
