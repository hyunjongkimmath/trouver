# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb.

# %% auto 0
__all__ = ['convert_double_asterisks_to_html_tags', 'raw_text_with_html_tags_from_markdownfile', 'html_data_from_note',
           'tokenize_html_data', 'def_or_notat_from_html_tag', 'def_and_notat_preds_by_model',
           'auto_mark_def_and_notats']

# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 4
from itertools import pairwise
import os 
from os import PathLike
from pathlib import Path
from typing import Optional, Union
import warnings

import bs4
from transformers import BatchEncoding, pipelines, PreTrainedTokenizer, PreTrainedTokenizerFast

from .....helper import add_HTML_tag_data_to_raw_text, add_space_to_lt_symbols_without_space, double_asterisk_indices, latex_indices, notation_asterisk_indices, replace_string_by_indices, remove_html_tags_in_text
from ....markdown.file import MarkdownFile, MarkdownLineEnum
from ..note_processing import process_standard_information_note
from ...vault import VaultNote

# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 8
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


# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 10
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



# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 18
def html_data_from_note(
        note_or_mf: Union[VaultNote, MarkdownFile], # Either a `VaultNote`` object to a note or a `MarkdownFile` object from which to extra html data.
        vault: Optional[PathLike] = None, # If vault to use when processing the `MarkdownFile` objects (if `note_of_mf` is a `VaultNote`, then this `MarkdownFile` object is created from the text of the note), cf. the `process_standard_information_note` function.
        note_name: Optional[str] = None, # If `note_or_mf` is a `MarkdownFile`, `note_name` should be the name of the note from which the `MarkdownFile` comes from if applicable. If `note_or_mf` is a `VaultNote` object, then `note_name` is ignored and `note_or_mf.name` is used instead.
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
    if isinstance(note_or_mf, VaultNote) and not note_or_mf.exists():
        return None
    if isinstance(note_or_mf, VaultNote):
        mf = MarkdownFile.from_vault_note(note_or_mf)
        note_name = note_or_mf.name
    else: # isinstance(note_or_mf, MarkdownFile):
        mf = note_or_mf.copy(deep=False)
    if mf.has_tag('_auto/def_and_notat_identified'):
        return None
    raw_text_with_tags = raw_text_with_html_tags_from_markdownfile(mf, vault)
    raw_text, tags_and_locations = remove_html_tags_in_text(raw_text_with_tags)
    return {
        "Note name": note_name,
        "Raw text": raw_text,
        "Tag data": tags_and_locations}

# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 29
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
    # return tokenized["input_ids"], ner_ids
    tokens = [tokenizer.convert_ids_to_tokens(tokens_for_seq)
              for tokens_for_seq in tokenized["input_ids"]]
    return tokens, ner_ids


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

# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 55
def _make_tag(
        text: str,
        entity_type: str # 'definition' or 'notation'
        ) -> bs4.element.Tag:
    """
    Helper function to `_html_tag_data_from_part` and `_consolidate_token_preds`.
    """
    soup = bs4.BeautifulSoup('', 'html.parser')
    if entity_type == 'definition':
        tag = soup.new_tag(
            'b',
            style="border-width:1px;border-style:solid;padding:3px",
            definition="")
    else:
        tag = soup.new_tag(
            'span',
            style="border-width:1px;border-style:solid;padding:3px",
            notation="")
    tag.string = text
    return tag


def _html_tag_data_from_part(
        main_text: str,
        part: list[dict[str]]) -> tuple[bs4.element.Tag, int, int]:
    """
    Helper function to `_html_tags_from_token_preds`
    """
    start_token = part[0]
    end_token = part[-1]
    start_char = start_token['start']
    end_char = end_token['end']
    # the `'entity'` is either 'I-definition', 'B-definition', 'I-notation',
    # or 'B-notation'
    entity_type = start_token['entity'][2:]
    html_text = main_text[start_char:end_char]
    return (_make_tag(html_text, entity_type), start_char, end_char)


# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 57
def _current_token_continues_the_previous_token(
        current_token: dict, previous_token: dict, note: Optional[VaultNote]
        ) -> bool:
    """
    Helper function to `_divide_token_preds_into_parts`.
    """
    if current_token['entity'].startswith('I-'):
        if current_token['entity'][2:] == previous_token['entity'][2:]:
            return True
        elif note:
            warnings.warn(rf"""
                In the note {note.name} at {note.path()},
                The token '{previous_token['word']}' is marked as '{previous_token['entity']}'
                and the subsequent token '{current_token['word']}' is marked as '{current_token['entity']}',
                which is unusual because the two consecutive tokens seem to be of different
                entities, and yet the latter token does not start with a 'B-'.

                The latter token will be treated like the beginning of a new entity."""
                    )
            return False
    else:
        return False
        

# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 59
def _divide_token_preds_into_parts(
        token_preds: list[dict[str]],
        note: VaultNote,
        excessive_space_threshold: int
        ) -> list[list[dict[str]]]:
    """
    Divide `token_preds` into parts so that each part
    represents a single definition/notation marking.

    Helper function to `_html_tags_from_token_preds`.
    """
    token_preds_parts = []
    for current_token in token_preds:
        if not token_preds_parts:
            token_preds_parts.append([current_token])
            continue
        prev_token = token_preds_parts[-1][-1]
        if _current_token_continues_the_previous_token(
                current_token, prev_token, note):
            prev_token_end = prev_token['end']
            cur_token_start = current_token['start']
            if prev_token_end + excessive_space_threshold >= cur_token_start and note:
                Warning(rf"""
                    In the note {note.name} at {note.path()},
                    There seems to be excessive space between the token
                    {prev_token['word']} and {current_token['word']}, which
                    seem to be part of the same entity"""
                        )
            token_preds_parts[-1].append(current_token)
        else:
            token_preds_parts.append([current_token])
    return token_preds_parts


# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 61
def _ranges_overlap(
        current_1: tuple[bs4.element.Tag, int, int],
        current_2: tuple[bs4.element.Tag, int, int]
        ) -> bool:
    """
    Based on https://stackoverflow.com/a/64745177

    Helper function to `_collate_html_tags`, `_consolidate_token_preds`.
    """
    return max(current_1[1], current_2[1]) < min(current_1[2], current_2[2])


# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 63
def _consolidate_token_preds(
        main_text: str,
        tag_data: list[tuple[bs4.element.Tag, int, int]]
        ) -> list[tuple[bs4.element.Tag, int, int]]:
    """
    Since the model's predictions can yield some odd results
    (e.g. notations not being marked for an entire LaTeX string
    $<span notation="">$S_k := ...</span>$$), this function tries
    to consolidate some oddities.
    
    """
    latex_inds = latex_indices(main_text)
    extended_tag_data = _extend_tag_data_ranges(main_text, latex_inds, tag_data)
    tag_data_notats_chopped = _cutoff_notation_tag_data(main_text, extended_tag_data)
    # Go through the extended tag data to throw out overlapping ones.
    ultimate_tag_data = []
    for tag_point in tag_data_notats_chopped:
        if _no_overlap_with_previous_tag_data(ultimate_tag_data, tag_point):
            ultimate_tag_data.append(tag_point)
    return ultimate_tag_data


def _extend_tag_data_ranges(
        main_text: str,
        latex_inds: list[tuple[int, int]],
        tag_data: list[tuple[bs4.element.Tag, int, int]],
        ) -> list[tuple[bs4.element.Tag, int, int]]:
    """Helper function to `_consolidate_token_preds`.

    Extend tag data so that the tag data does not start or
    end within any latex math mode string. 
    """
    extended_tag_data = []
    for tag_tuple in tag_data:
    # for tex_range in latex_inds:
        combined_range = (tag_tuple[1], tag_tuple[2])
        for tex_range in latex_inds:
        # for tag_tuple in tag_data:
            if not _ranges_overlap((0, tex_range[0], tex_range[1]), tag_tuple):
                continue
            combined_range = (min(combined_range[0], tex_range[0]), max(combined_range[1], tex_range[1]))
        new_text = main_text[combined_range[0]:combined_range[1]]
        tag_type = 'definition' if 'definition' in tag_tuple[0].attrs else 'notation'
        extended_tag = _make_tag(new_text, tag_type)
        extended_tag_data.append((extended_tag, combined_range[0], combined_range[1]))
    return extended_tag_data


def _cutoff_notation_tag_data(
        main_text: str,
        tag_data: list[tuple[bs4.element.Tag, int, int]],
        ) -> list[tuple[bs4.element.Tag, int, int]]:
    """
    Helper function to `_consolidate_token_preds`.

    Guarantees that a notation tag is a pure math mode latex string
    by cutting only the pure math mode string
    that occurs within it. Assumes that `_extend_tag_data_ranges`
    works as intended.
    """
    cutout_notation_tag_data = []
    for tag, start, end in tag_data:
        if not 'notation' in tag.attrs:
            cutout_notation_tag_data.append((tag, start, end))
            continue
        tag_text = main_text[start:end]
        tex_inds_in_tagged = latex_indices(tag_text)
        for sub_start, sub_end in tex_inds_in_tagged:
            tex_str = main_text[start+sub_start:start+sub_end]
            cutout_tag = _make_tag(tex_str, 'notation')
            cutout_notation_tag_data.append(
                (cutout_tag, start+sub_start, start+sub_end))
    return cutout_notation_tag_data



def _no_overlap_with_previous_tag_data(
        ultimate_tag_data: list[tuple[bs4.element.Tag, int, int]],
        current_tag_data: tuple[bs4.element.Tag, int, int]  # Current tag data
        ) -> bool:
    """
    Return `True`, if the `current_tag_data` does not overlap with
    any tag data that will be ultimately added. 

    Helper function for `_consolidate_token_preds`.
    """
    # current_range = (current_tag_data[1], current_tag_data[2])
    for prev in reversed(ultimate_tag_data):
        # prev_range = (prev[1], prev[2])
        if _ranges_overlap(prev, current_tag_data):
            return False
    return True
    

# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 65
def _html_tags_from_token_preds(
        main_text: str,
        token_preds: list[dict[str]],
        note: VaultNote,
        excessive_space_threshold: int
        ) -> list[tuple[bs4.element.Tag, int, int]]:  # Tag element, start, end, where main_text[start:end] needs to be replaced by the tag element.
    """
    Return HTML tags for definition and notation classification.

    Helper function to `auto_mark_def_and_notats`.
    """
    parts = _divide_token_preds_into_parts(
        token_preds, note, excessive_space_threshold)
    return [_html_tag_data_from_part(main_text, part) for part in parts]


# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 66
def _collate_html_tags(
        tag_data_1: list[tuple[bs4.element.Tag, int, int]],
        tag_data_2: list[tuple[bs4.element.Tag, int, int]],
    ) -> list[tuple[bs4.element.Tag], int, int]:
    """
    Collates the lists of HTML tags and the indices within a certain text
    (which is not-needed for this function and hence not included)
    that the HTML tags need to replace.

    If there are entries in `tag_data_1` and `tag_data_2` with overlapping
    ranges, then the entry from `tag_data_1` is prioritized and the entry
    from `tag_data_2` is discarded.

    Helper function to `auto_mark_def_and_notats`
    """
    collated_list = []
    i, j = 0, 0
    while i < len(tag_data_1) and j < len(tag_data_2):
        current_1 = tag_data_1[i]
        current_2 = tag_data_2[j]
        if _ranges_overlap(current_1, current_2): # Ignore current_2
            j += 1
            continue
        if current_1[1] > current_2[1]:
            collated_list.append(current_2)
            j += 1
        else:
            collated_list.append(current_1)
            i += 1
    while i < len(tag_data_1):
        collated_list.append(tag_data_1[i])
        i += 1
    while j < len(tag_data_2):
        collated_list.append(tag_data_2[j])
        j += 1
    return collated_list




# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 68
def _add_nice_boxing_attrs_to_def_and_notat_tags(
        html_tag_data: list[tuple[bs4.element.Tag, int, int]]
        ) -> list[tuple[bs4.element.Tag, int, int]]:
    """
    Add HTML tag attributes to draw boxes around notation data

    Helper function to `auto_mark_def_and_notats`.
    """
    listy = []
    for tag, start, end in html_tag_data:
        if ('notation' in tag.attrs or 'definition' in tag.attrs) and 'style' not in tag.attrs:
            tag.attrs['style'] = "border-width:1px;border-style:solid;padding:3px"
        listy.append((tag, start, end)) 
    return listy



# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 70
def def_and_notat_preds_by_model(
        text: str,  
        pipeline # The pipeline object created using the token classification model and its tokenizer
        ) -> list[tuple[bs4.element.Tag, int, int]]: # Each tuple consists of an HTML tag carrying the data of the prediction and ints marking where in `text` the definition or notation is at.
    """
    Predict where definitions and notations occur in `text`

    This function uses some of the same helper functions as
    `auto_mark_def_and_notats`, but does not raise warning messages as
    in `auto_mark_def_and_notats`.
    """
    tag_data = _html_tags_from_token_preds(text, pipeline(text), None, 2)
    return tag_data

# %% ../../../../../nbs/28_markdown.obsidian.personal.machine_learning.tokenize.ipynb 72
def auto_mark_def_and_notats(
        note: VaultNote,  # The standard information note in which to find the definitions and notations.
        pipeline: pipelines.token_classification.TokenClassificationPipeline, # The token classification pipeline that is used to predict whether tokens are part of definitions or notations introduced in the text.
        # remove_existing_def_and_notat_markings: bool = False,  # If `True`, remove definition and notation markings (both via surrounding by double asterisks `**` as per the legacy method and via HTML tags)
        excessive_space_threshold: int = 2,
        add_boxing_attr_to_existing_def_and_notat_markings: bool = True # If `True`, then nice attributes are added to the existing notation HTML tags, if not already present.
    ) -> None:
    """
    Predict and mark where definitions and notation occur in a note using
    a token classification ML model.

    Assumes that the note is a standard information note that does not
    have a lot of "user modifications", such as footnotes, links,
    and HTML tags. If
    there are many modifications, then these might be deleted.

    Assumes that the paragraphs in the text of the note are "not too long".
    Currently, this means that the paragraphs in the number of tokens
    in the text of the note should (roughly) not exceed 
    `pipeline.tokenizer.model_max_length`.

    Existing markings for definition and notation data (i.e. by
    surrounding with double asterisks or by HTML tags) are preserved
    (and turned into HTML tags), unless the markings overlap with 
    predictions, in which case the original is preserved (and still
    turned into an HTML tag if possible)

    Since the model can make "invalid" predictions (mostly those which
    start or end within a LaTeX math mode str), the actual markings
    are not necessarily direct translates from the model's predictions.
    See the helper function `_consolidate_token_preds` for more details
    on how this is implemented.
    
    **Raises**
    Warning messages (`UserWarning`) are printed in the following situations:

    - There are two consecutive tokens within the `pipeline`'s predictions
      of different entity types (e.g. one is predicted to belong within a
      definition and the other within a notation), but the latter token's
      predicted `'entity'` more specifically begins with `'I-'` (i.e. is
      `'I-definition'` or `'I-notation'`) as opposed to `'B-'`.
        - `note`'s name, and path are included in the warning message in
          this case.
    - There are two consecutive tokens within the `pipeline`'s predictions
      which the pipeline predicts to belong to the same entity, and yet
      there is excessive space (specified by `excessive_space_threshold`)
      between the end of the first token and the start of the second.

    """
    mf = MarkdownFile.from_vault_note(note)
    _process_mf(mf)
    first_non_metadata_line, see_also_line = _get_main_text_lines(mf)
    # mf.merge_display_math_mode()
    # mf.merge_display_math_mode_into_preceding_text()
    # tuppy = mf.metadata_lines()
    # if tuppy is not None:
    #     first_non_metadata_line = tuppy[1] + 1
    # else:
    #     first_non_metadata_line = 0 
    # see_also_line = mf.get_line_number_of_heading('See Also')
     
    main_text = mf.text_of_lines(first_non_metadata_line, see_also_line)
    main_text = _format_main_text_and_add_html_tag_data(
        note, pipeline, add_boxing_attr_to_existing_def_and_notat_markings,
        excessive_space_threshold, main_text)
    _write_text_with_html_tag_preds_to_note(
        note, mf, main_text, first_non_metadata_line, see_also_line)
    # mf.remove_lines(first_non_metadata_line, see_also_line)
    # mf.insert_line(first_non_metadata_line,
    #                {'type': MarkdownLineEnum.DEFAULT, 'line': main_text})
    # mf.add_tags('_auto/def_and_notat_identified')
    # mf.write(note)


def _process_mf(
        mf: MarkdownFile) -> None:
    """Helper function to `auto_mark_def_and_notats`"""
    mf.merge_display_math_mode()
    mf.merge_display_math_mode_into_preceding_text()


def _get_main_text_lines(
        mf: MarkdownFile) -> tuple[int, int]:
    """Helper function to `auto_mark_def_and_notats`"""
    tuppy = mf.metadata_lines()
    if tuppy is not None:
        first_non_metadata_line = tuppy[1] + 1
    else:
        first_non_metadata_line = 0 
    see_also_line = mf.get_line_number_of_heading('See Also')
    return first_non_metadata_line, see_also_line


def _format_main_text_and_add_html_tag_data(
        note: VaultNote,
        pipeline: pipelines.token_classification.TokenClassificationPipeline, # The token classification pipeline that is used to predict whether tokens are part of definitions or notations introduced in the text.
        add_boxing_attr_to_existing_def_and_notat_markings: bool,
        excessive_space_threshold: int,
        main_text: str,  # The main text to format and to add HTML tag data to
        ) -> str:
    """Helper function to `auto_mark_def_and_notats`"""
    main_text = add_space_to_lt_symbols_without_space(main_text)
    main_text = convert_double_asterisks_to_html_tags(main_text)
    main_text, existing_html_tag_data = remove_html_tags_in_text(main_text)
    if add_boxing_attr_to_existing_def_and_notat_markings:
        existing_html_tag_data = _add_nice_boxing_attrs_to_def_and_notat_tags(
            existing_html_tag_data)

    # html_tags_to_add = _html_tags_from_token_preds(
    #     main_text, pipeline(main_text), note, excessive_space_threshold)
    # html_tags_to_add = _consolidate_token_preds(
    #     main_text, html_tags_to_add)
    html_tags_to_add = _get_token_preds_by_dividing_main_text(
        main_text, pipeline, note, excessive_space_threshold)

    html_tags_to_add_back = _collate_html_tags(
        existing_html_tag_data, html_tags_to_add)
    return add_HTML_tag_data_to_raw_text(main_text, html_tags_to_add_back)


def _get_token_preds_by_dividing_main_text(
        main_text: str,
        pipeline: pipelines.token_classification.TokenClassificationPipeline, # The token classification pipeline that is used to predict whether tokens are part of definitions or notations introduced in the text. Here, the tokenizer of this pipeline is used to estimate how many tokens a piece of subtext will have.
        note: VaultNote,
        excessive_space_threshold: int,    
        ) -> list[tuple[bs4.element.Tag, int, int]]:  # Tag element, start, end, where main_text[start:end] needs to be replaced by the tag element.
    """
    Divide the `main_text` into not-too-long pieces to return HTML tag predictions

    Helper function for `_format_main_text_and_add_html_tag_data`.
    """
    pieces_start_and_end = _divide_main_text(main_text, pipeline)
    cumulative_html_tags_in_main = []
    for start_of_piece, end_of_piece in pieces_start_and_end:
        # text = main_text[start_of_piece:end_of_piece]
        text = main_text[start_of_piece:]
        html_tags_in_piece = _html_tags_from_token_preds(
            text, pipeline(text), note, excessive_space_threshold)
        html_tags_in_piece = _consolidate_token_preds(
            text, html_tags_in_piece)
        # start and end indices need to be re-adjusted with respect to their places in `main_text`
        html_tags_for_piece_in_main_text = [
            (tag, start_of_piece + start, start_of_piece + end)
            for tag, start, end in html_tags_in_piece]
        cumulative_html_tags_in_main = _collate_html_tags(
            cumulative_html_tags_in_main, html_tags_for_piece_in_main_text)
    return cumulative_html_tags_in_main


def _divide_main_text(
        main_text: str,
        pipeline: pipelines.token_classification.TokenClassificationPipeline, # The token classification pipeline that is used to predict whether tokens are part of definitions or notations introduced in the text. Here, the tokenizer of this pipeline is used to estimate how many tokens a piece of subtext will have.
        # ) -> list[tuple[str, int, int]]:  # The str is a chunk of text, the first int is the index in `main_text` that the chunk starts at, and the second int is the approximate token length of the text. Appending all the chunks of text as they are should result back in the original text.
        ) -> list[tuple[int, int]]:  # Each tuple is a start and end range for pieces of `main_text` to be considered for predictions
    """Divides `main_text` so that predictions can be made on smaller chunks of text.
    
    Assumes that dividing `main_text` along newline characters `\n` will result in
    pieces that are "not too long".

    Helper function to `_format_main_text_and_add_html_tag_data`.


    """
    main_text.split('\n')
    tokenizer = pipeline.tokenizer
    newline_indices = [i for i, char in enumerate(main_text) if char == '\n']
    newline_indices.insert(0, 0)
    chunks = []  # list[tuple[str, int, int]]  # The str is a chunk of text, the first int is the index in `main_text` that the chunk starts at, and the second int is the approximate token length of the text. Appending all the chunks of text as they are should result back in the original text.
    for start, end in pairwise(newline_indices):
        chunk = main_text[start:end]
        chunks.append((chunk, start, len(tokenizer(chunk)['input_ids'])))
    last_chunk = main_text[newline_indices[-1]:]
    chunks.append((last_chunk, newline_indices[-1], len(tokenizer(chunk))))
    return _find_places_to_divide_from_chunks(chunks, pipeline)


def _find_places_to_divide_from_chunks(
        chunks: list[tuple[str, int, int]], # The str is a chunk of text, the first int is the index in `main_text` that the chunk starts at, and the second int is the approximate token length of the text. Appending all the chunks of text as they are should result back in the original text.
        pipeline: pipelines.token_classification.TokenClassificationPipeline, # The token classification pipeline that is used to predict whether tokens are part of definitions or notations introduced in the text. Here, the tokenizer of this pipeline is used to estimate how many tokens a piece of subtext will have.
        ) -> list[tuple[int, int]]: # Each tuple is a start and end range for pieces of `main_text` to be considered for predictions
    """Identify appropriate indices in `main_text` where (overlapping)
    pieces in `main_text` should start/end for predictions with `pipeline`.
    
    Helper function to `_divide_main_text`.

    We describe how this function is implemented: starting at the first chunk
    (chunks are non-overlapping), start to consider consecutive chunks to
    make up a piece. So maybe we have chunks

        A B C D E F ....

    We build a piece chunk-by-chunk, considering the total token length of the
    built sub-piece along the way. The first chunk within a sub-piece 
    that makes the sub-piece of token-length greater than half the max
    token length with respect to `pipeline.tokenizer` will become the start of the
    next piece, unless the very first chunk in the piece is already longer than half the max
    token length with respect to the tokenizer (this is to ensure that the
    piece-building process does not keep starting at the same chunk).
    Moreover, a piece will stop building as soon as its token-length exceeds
    the max length of the tokenizer.

    For instance, maybe the max length for the tokenizer is 512, and the chunks
    are of the following length:

        A   B    C  D   E    F     ...
        76  130  70 13  150  140   ...

    We first build the piece starting at A:

        A
        76

    We continue building the piece by "appending" B:

        A   B
        76  130

    Once we append C as well, the piece's length is now 276 and hence over half of 512,
    so the next piece will start at C: 

        A   B    C
        76  130  70

    Subsequently, we continue building the piece. Only once F is appended does the 
    length of the entire piece exceed 512 (the length is 579):

        A   B    C  D   E    F
        76  130  70 13  150  140
    
    And then we begin building the next piece from C.

    Also, consider an example where the first chunk's length exceeds half the max length
    of the tokenizer:

        A   B    C   ...
        300 200  100 ...

    Here, the first piece will consist of the chunks A, B, and C because
    the length of the piece exceeds the max length of 512 only after appending C.
    To guarantee that the next piece does not start with the chunk A again, B is 
    used as the first chunk in the next piece:

        B    C   ...
        200  100 ...

    If any chunk's token length exceeds the tokenizer's max_model_length, then
    the pipeline/model can only predict on the starting tokens in the chunk. 
    As such, the chunks must not be "too long" for best results on the model's predictions.
    """
    tokenizer = pipeline.tokenizer
    start_chunk_index, next_piece_start_chunk_index = 0, 0
    current_piece_token_len = 0
    pieces_start_and_end = []
    i = 0
    while i < len(chunks):
        chunk = chunks[i]
        current_piece_token_len = current_piece_token_len + chunk[2]
        if (current_piece_token_len > tokenizer.model_max_length / 2
                and start_chunk_index == next_piece_start_chunk_index):
            # Mark where the next piece should start
            next_piece_start_chunk_index = i if start_chunk_index != i else i+1
        if (current_piece_token_len > tokenizer.model_max_length):
            # Add a new item in the list and then Start a new piece
            # start_chunk, end_chunk = chunks[start_chunk_index], chunk
            # start_char_index = start_chunk[1]
            # end_char_index = end_chunk[1] + len(end_chunk[0])
            # pieces_start_and_end.append([start_char_index, end_char_index])
            _append_to_pieces_start_and_end(
                pieces_start_and_end, chunks[start_chunk_index], chunk)
            i, start_chunk_index = (
                next_piece_start_chunk_index, next_piece_start_chunk_index)
            current_piece_token_len = 0
            continue
        i += 1
    # Add the last chunk at the end
    _append_to_pieces_start_and_end(
        pieces_start_and_end, chunks[start_chunk_index], chunks[-1])
    return pieces_start_and_end


def _append_to_pieces_start_and_end(
        pieces_start_and_end: list[tuple[int, int]],
        start_chunk: tuple[str, int, int],
        end_chunk: tuple[str, int, int]
        ) -> None:
    """Helper function to `_find_places_to_divide_from_chunks`"""
    start_char_index = start_chunk[1]
    end_char_index = end_chunk[1] + len(end_chunk[0])
    pieces_start_and_end.append([start_char_index, end_char_index])



def _write_text_with_html_tag_preds_to_note(
        note: VaultNote,
        mf: MarkdownFile,
        main_text: str,
        first_non_metadata_line: int,
        see_also_line: int
        ) -> None:
    """Helper function to `auto_mark_def_and_notats`"""
    mf.remove_lines(first_non_metadata_line, see_also_line)
    mf.insert_line(first_non_metadata_line,
                   {'type': MarkdownLineEnum.DEFAULT, 'line': main_text})
    mf.add_tags('_auto/def_and_notat_identified')
    mf.write(note)

