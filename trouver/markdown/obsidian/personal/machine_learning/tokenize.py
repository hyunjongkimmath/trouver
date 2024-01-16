# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb.

# %% auto 0
__all__ = ['convert_double_asterisks_to_html_tags', 'raw_text_with_html_tags_from_markdownfile', 'html_data_from_note',
           'tokenize_html_data', 'def_or_notat_from_html_tag']

# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 3
import os 
from os import PathLike
from pathlib import Path
from typing import Union

import bs4
import pandas as pd
from transformers import BatchEncoding, PreTrainedTokenizer, PreTrainedTokenizerFast

from .....helper import current_time_formatted_to_minutes, definition_asterisk_indices, double_asterisk_indices, notation_asterisk_indices, replace_string_by_indices, remove_html_tags_in_text
from ....markdown.file import MarkdownFile
from ..note_processing import process_standard_information_note
from ...vault import VaultNote

# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 7
def convert_double_asterisks_to_html_tags(
        text: str
        ) -> str:
    """
    Replace the double asterisks, which signify definitions and notations,
    in `text` with HTML tags.
    """
    double_asts = double_asterisk_indices(text)
    replacement_html_tags = [
        _html_tag_from_double_ast(text[start:end])
        for start, end in double_asts]
    return replace_string_by_indices(
        text, double_asts, replacement_html_tags)


def _html_tag_from_double_ast(
        double_ast_string: str # Starts and ends with double asts
        ) -> str:
    """
    Get the HTML tag representing definition or notation data from
    a string surrounded by double asterisks.

    This is used in the `_convert_double_asterisks_to_html_tags` function.
    """
    no_asts = double_ast_string[2:-2]
    if notation_asterisk_indices(double_ast_string):
        return f'<span notation="">{no_asts}</span>'
    else:
        return f'<b definition="">{no_asts}</b>'


# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 9
def raw_text_with_html_tags_from_markdownfile(
        mf: MarkdownFile,
        vault: PathLike
        ) -> str:
    """
    Process the `MarkdownFile`, replacing the double asterisk surrounded
    text indicating definitions and notations to be HTML tags instead.
    """
    mf = process_standard_information_note(
        mf, vault, remove_double_asterisks=False,
        remove_html_tags=False)
    return convert_double_asterisks_to_html_tags(str(mf))



# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 17
# TODO: implement a measure to not get the definition identification data, e.g. by 
# detecting a `_auto/definition_identification` tag.
def html_data_from_note(
        note: VaultNote,
        vault: PathLike
        ) -> Union[dict, None]: # The keys to the dict are "Note name", "Raw text", "Tag data". However, `None` is returned if `note` does not exist or the note is marked with auto-generated, unverified data.
    # TODO: implement obtaining multiple datapoints from a single note
    # Via typos for example.
    """Obtain html data for token classification from the information note.

    Currently, the token types mainly revolve around definitions and
    notations.

    If `note` has the tag `_auto/def_and_notat_identified`, then the data
    in the note is assumed to be auto-generated and not verified and
    `None` is returned.

    **Returns**
    - Union[dict, None]
        - The keys-value pairs are 
            - `"Note name"` - The name of the note
            - `"Raw text"` - The raw text to include in the data.
            - `"Tag data"` - The list with HTML tags carrying definition/notation
              data and their locations in the Raw text. See the second output to
              the function `remove_html_tags_in_text`.
                - Each element of the list is a tuple consisting of a ``bs4.element.Tag``
                  and two ints.
    """
    if not note.exists():
        return None
    mf = MarkdownFile.from_vault_note(note)
    if mf.has_tag('_auto/def_and_notat_identified'):
        return None
    raw_text_with_tags = raw_text_with_html_tags_from_markdownfile(mf, vault)
    raw_text, tags_and_locations = remove_html_tags_in_text(raw_text_with_tags)
    return {
        "Note name": note.name,
        "Raw text": raw_text,
        "Tag data": tags_and_locations}

# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 20
def tokenize_html_data(
        html_locus: dict, # An output of `html_data_from_note`
        tokenizer: Union[PreTrainedTokenizer, PreTrainedTokenizerFast],
        max_length: int, # Max length for each sequence of tokens
        ner_tag_from_html_tag: callable, # takes in a bs4.element.Tag and outputs the ner_tag (as a string or `None`)
        label2id: dict[str, int], # The keys ner_tag's of the form f"I-{output}" or f"B-{output}" where `output` is an output of `ner_tag_from_html_tag`.
        default_label: str = "O", # The default label for the NER tagging.
        ) -> tuple[list[list[str]], list[list[int]]]: # The first list consists of the tokens and the second list consists of the named entity recognition tags.
    """Actually tokenize the html data outputted by `html_data_from_note`.

    To account for the possibility that the raw text is long,
    this function uses the `tokenizer.batch_encode_plus` function
    to tokenize the text into sequences. 
    """
    tokenized = tokenizer.batch_encode_plus(
        [html_locus["Raw text"]], max_length=max_length, return_overflowing_tokens=True,
        return_offsets_mapping=True, truncation=True)

    default_id = label2id[default_label]        
    ner_ids = [[default_id for _ in seq_input_ids]
               for seq_input_ids in tokenized['input_ids']]
    for tag, start, end in html_locus["Tag data"]:
        ner_tag = ner_tag_from_html_tag(tag)
        if ner_tag is None:
            continue  # `ner_tag` is not of relevant data.
        tuppy = _start_end_seqs_indices_for_html_tag(tokenized, start, end - 1)
        (start_seq, start_index_in_seq), (end_seq, end_index_in_seq) = tuppy
        _set_ner_ids_for_tag(
            ner_ids, start_seq, start_index_in_seq, end_seq, end_index_in_seq,
            label2id, ner_tag)
    return tokenized["input_ids"], ner_ids


def _start_end_seqs_indices_for_html_tag(
        tokenized: BatchEncoding,
        tag_start_ind: int,
        tag_end_ind: int
        ) -> tuple[tuple[int, int], tuple[int, int]]: # The first tuple is `(a, b)` where `tokenized['input_ids'][a][b]` is the token corresponding to the start of the HTML tag's (raw) text. The second tuple is `(c, d)` where `tokenized['input_ids'][c][d]` is the token corresponding to the end of the HTML tag's (raw) text.
    start_seq = _search_seq_ind_for_char(tokenized['offset_mapping'], tag_start_ind)
    # start_index_in_seq = tokenized.char_to_token(batch_or_char_index=start_seq, char_index=tag_start_ind)
    start_index_in_seq = _search_within_seq_for_char(tokenized['offset_mapping'][start_seq], tag_start_ind)
    end_seq = _search_seq_ind_for_char(tokenized['offset_mapping'], tag_end_ind)
    # end_index_in_seq = tokenized.char_to_token(batch_or_char_index=end_seq, char_index=tag_end_ind)
    end_index_in_seq = _search_within_seq_for_char(tokenized['offset_mapping'][end_seq], tag_end_ind)
    return (start_seq, start_index_in_seq), (end_seq, end_index_in_seq)


def _min_max_char_ind_for_seq(
        offset_for_seq: list[tuple[int,int]] # An item in tokenized['offset_mapping']
        ):
    min_char_ind, max_char_ind = 0, 0
    for inds in offset_for_seq:
        if inds != (0,0):
            min_char_ind = inds[0]
            break
    for inds in reversed(offset_for_seq):
        if inds != (0,0):
            max_char_ind = inds[1]
            break
    return min_char_ind, max_char_ind

def _char_is_in_seq(
        offset_for_seq: list[int], # An item in tokenized['offset_mapping']
        char: int # The index of a character in the original raw text
        ) -> bool:
    min_char_ind, max_char_ind = _min_max_char_ind_for_seq(offset_for_seq)
    return min_char_ind <= char and char < max_char_ind

def _search_seq_ind_for_char(
        offsets: list[tuple[int, int]], # tokenized['offset_mapping']
        char: int # The index of a character in the original raw text
        ) -> int:
    """
    Binary search the index of the sequence containing the token at the 
    location of the index `char` within the original (raw) text.

    Based on pseudocode from https://pseudoeditor.com/guides/binary-search
    """
    left = 0
    right = len(offsets) - 1
    while left <= right:
        mid = (left + right) // 2
        min_char_ind, max_char_ind = _min_max_char_ind_for_seq(offsets[mid])
        if min_char_ind <= char and char < max_char_ind:
            return mid
        elif max_char_ind <= char:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # This should not be returned under normal use.


def _search_within_seq_for_char(
        seq_offset: list[tuple[int, int]],
        char: int
    ) -> int:
    """
    Binary search for the index within the sequence corresponding
    to the token at the location of the index `char` within the
    original (raw) text.

    Based on pseudocode from https://pseudoeditor.com/guides/binary-search
    """
    left = 0
    right = len(seq_offset) - 1
    while left <= right:
        mid = (left + right) // 2
        min_char_ind, max_char_ind = seq_offset[mid] 
        if min_char_ind <= char and char < max_char_ind:
            return mid
        elif max_char_ind <= char:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # This should not be returned under normal use.


def _set_ner_ids_for_tag(
        ner_ids: list[list[int]],
        start_seq: int, 
        start_index_in_seq: int,
        end_seq: int,
        end_index_in_seq: int,
        label2id: dict[str, int],
        ner_tag: str
        ) -> None:
    """
    After the locations of the tokens corresponding to a HTML tag have been found, 
    mark within `ner_ids` the appropriate NER tags at the locations corresponding
    to the tokens' locations.
    """
    ner_ids[start_seq][start_index_in_seq] = label2id[f"B-{ner_tag}"]
    i_ner_id = label2id[f"I-{ner_tag}"]
    seq, ind = start_seq, start_index_in_seq + 1
    while seq < end_seq or ind <= end_index_in_seq:
        if len(ner_ids[seq]) <= ind:
            seq += 1
            ind = 0
        else:
            ner_ids[seq][ind] = i_ner_id 
            ind += 1
    


def def_or_notat_from_html_tag(
        tag: bs4.element.Tag
        ) -> Union[str, None]:
    """
    Can be passed as the `ner_tag_from_html_tag` argument in `tokenize_html_data`
    for the purposes of compiling a dataset for definition and notation
    identification.

    The strings f"I-{output}" and f"B-{output}" are valid ner_tags. To use for 
    """
    if "definition" in tag.attrs:
        return "definition"
    elif "notation" in tag.attrs:
        return "notation"
    return None  # If the HTML tag carries neither definition nor notation data.
