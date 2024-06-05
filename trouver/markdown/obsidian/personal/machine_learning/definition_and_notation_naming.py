# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../../../nbs/35_markdown.obsidian.personal.machine_learning.definition_and_notation_naming.ipynb.

# %% auto 0
__all__ = ['data_from_information_note', 'predict_names', 'add_names_to_html_tags_in_info_note']

# %% ../../../../../nbs/35_markdown.obsidian.personal.machine_learning.definition_and_notation_naming.ipynb 4
from typing import Optional

from bs4 import BeautifulSoup
from transformers import pipelines
import warnings

from .....helper import remove_html_tags_in_text, add_HTML_tag_data_to_raw_text
from ....markdown.file import MarkdownFile
from ..note_processing import process_standard_information_note
from ...vault import VaultNote


# %% ../../../../../nbs/35_markdown.obsidian.personal.machine_learning.definition_and_notation_naming.ipynb 6
# TODO: test
def data_from_information_note(
        info_note: VaultNote, # The standard information note from which to draw data.
    ) -> list[dict]: # Each dict corresponds to a single datapoint, which holds the data of the naming of a single definition or notation (latex str) introduced in `info_note`. 
    """
    Obtain data for naming definitions and notations for a standard information
    note.

    Definitions and notations should be marked by HTML tags (see
    `markdown.obsidian.personal.machine_learning.tokenize`).
    - A definition is to be marked by an HTML tag with a `definition` attribute,
      which is the definition's "name", i.e. words and/or phrases describing what
      the definition is called and to what objects/situations the definition
      is applicable. If multiple combinations of words/phrases are appropriate,
      then they are separated by a single semicolon `;`. If the `definition`
      attribute is `""`, then the definition name has not been marked, both manually
      and automatically.
    - A notation (technically the full LaTeX string in which the notation is
      introducedis) is to be marked by an HTML tag with a `notation` attribute,
      which is the notation's "name", i.e. the actual notation introduced in
      the LaTeX string (without surrounding dollar signs (`$` or `$$`)). If
      multiple notations are appropriate, then they are separated by
      double semicolons `;;`. If the `notation` attribute is `""`, then it
      means that either the notation has not been marked, or that the
      LaTeX string (minus the surrounding dollar signs) is exactly the
      introduced notation. 


    **Returns**
    - list[dict[str, str]]
        - Each dict corresponds to a single datapoint, which holds the data of
          the naming of a single definition or notation (latex str) introduced
          in `info_note`. The keys are `'text'` and `'definition`' or
          `'notation`'. The `text` entry should be the processed text of
          `info_note`, see `process_standard_information_note` 

    """
    mf = MarkdownFile.from_vault_note(info_note)

    # Processes the info note in all ways except for the HTML tags
    mf = process_standard_information_note(
        mf, info_note.vault,
        True, True, True, True, True, False, True, True, True, True,
        True, True, True, None, True)
    
    text_without_html_tags, removed_tags = remove_html_tags_in_text(str(mf))
    list_of_dicts = []
    for removed_tag, start, end in removed_tags:
        if 'definition' in removed_tag.attrs:
            def_or_notat = 'definition'
        elif 'notation' in removed_tag.attrs:
            def_or_notat = 'notation'
        else:
            continue
        data_point_dict = {def_or_notat: removed_tag.attrs[def_or_notat]}
        location_marking_tag = BeautifulSoup(f'<b {def_or_notat}="">{removed_tag.text}', 'html.parser')
        data_point_dict['text'] = add_HTML_tag_data_to_raw_text(
            text_without_html_tags, [(location_marking_tag, start, end)])
        list_of_dicts.append(data_point_dict)
    return list_of_dicts

# %% ../../../../../nbs/35_markdown.obsidian.personal.machine_learning.definition_and_notation_naming.ipynb 8
# TODO: mark the note with and `_auto` tag and make it so that 
def predict_names(
        info_note: VaultNote,
        def_and_notat_pipeline: Optional[pipelines.text2text_generation.SummarizationPipeline], # A pipeline wrapping an ML model which predicts the naming of both definition and notations.
        def_pipeline: Optional[pipelines.text2text_generation.SummarizationPipeline],  # A pipeline wrapping an ML model which predicts the naming of definitions. 
        notat_pipeline: Optional[pipelines.text2text_generation.SummarizationPipeline], # A pipeline wrapping an ML model which predicts the naming of notations. 
        ) -> list[str]:
    r"""
    Predict the names of the definitions and notations using the trained ML models

    Either `def_and_notat_pipeline` or both `def_pipeline` and `notat_pipeline`
    should be provided.
    """
    if (def_and_notat_pipeline is None and 
            (def_pipeline is None or notat_pipeline is None)):
        raise ValueError(
            "Expected `def_and_notat_pipeline` to be specified or "
            "both `def_pipeline` and `notat_pipeline` to be specified.")
    data_points = data_from_information_note(info_note)
    return [_name_prediction_for_data_point(
        data_point, def_and_notat_pipeline, def_pipeline, notat_pipeline)
        for data_point in data_points]


def _name_prediction_for_data_point(
        data_point: dict, 
        def_and_notat_pipeline: Optional[pipelines.text2text_generation.SummarizationPipeline], 
        def_pipeline: Optional[pipelines.text2text_generation.SummarizationPipeline],  
        notat_pipeline: Optional[pipelines.text2text_generation.SummarizationPipeline], 
        ) -> str:
    if def_and_notat_pipeline is not None:
        summarizer = def_and_notat_pipeline
    elif 'definition' in data_point:
        summarizer = def_pipeline
        summarizer_output = summarizer(data_point['text'])
    else:
        summarizer = notat_pipeline
        summarizer_output = summarizer(data_point['text'], max_length=20, min_length=0)
    return summarizer_output[0]['summary_text']


# %% ../../../../../nbs/35_markdown.obsidian.personal.machine_learning.definition_and_notation_naming.ipynb 9
def add_names_to_html_tags_in_info_note(
        info_note: VaultNote,
        def_and_notat_pipeline: Optional[pipelines.text2text_generation.SummarizationPipeline] = None, # A pipeline wrapping an ML model which predicts the naming of both definition and notations.
        def_pipeline: Optional[pipelines.text2text_generation.SummarizationPipeline] = None,  # A pipeline wrapping an ML model which predicts the naming of definitions. 
        notat_pipeline: Optional[pipelines.text2text_generation.SummarizationPipeline] = None, # A pipeline wrapping an ML model which predicts the naming of notations. 
        # summarizer: pipelines.text2text_generation.SummarizationPipeline, # The pipeline with the ML model
        overwrite: bool = False, # If `True`, overwrite pre-existing, nonempty attributes. If `False`, ignore pre-existing, nonempty attributes and only write on attributes that are empty.
        ) -> None:
    """
    Predict the names of definitions and notations marked with
    HTML tags within `info_note` and write those names in the
    `"definition"` or `"notation"` attributes in each tag.

    Either `def_and_notat_pipeline` or both `def_pipeline` and `notat_pipeline`
    should be provided.

    An `#_auto/notation_notes_linked` tag is added to
    `origin_notation_note` if such a tag is not already
    present.
    """
    raw_info_note_text = info_note.text()
    raw_info_note_text_minus_html_tags, tags_and_locats = remove_html_tags_in_text(
        raw_info_note_text)
    predicted_names = predict_names(
        info_note, def_and_notat_pipeline, def_pipeline,
        notat_pipeline)

    # If somehow a different number of HTML tags were found
    if len(predicted_names) != len(tags_and_locats):
        # TODO: do warning
        warnings.warn(
            "Somehow, an inconsistent number of HTML tags are "
            f"detected in the note: {info_note.name}.\n"
            "This will raise some indexing issues when marking the definition "
            "and notation names")
    new_tags_and_locations = []
    any_preds_written = False
    for name, (tag, start, end) in zip(predicted_names, tags_and_locats):
        if 'definition' in tag.attrs:
            def_or_notat = 'definition'
        elif 'notation' in tag.attrs:
            def_or_notat = 'notation'
        else:
            # tag could be neither a definition nor a notation tag.
            def_or_notat = ''
        if def_or_notat and (tag.attrs[def_or_notat] == "" or overwrite):
            tag[def_or_notat] = name
            any_preds_written = True
        new_tags_and_locations.append((tag, start, end))
    new_info_note_text = add_HTML_tag_data_to_raw_text(
        raw_info_note_text_minus_html_tags, new_tags_and_locations)
    mf = MarkdownFile.from_string(new_info_note_text)
    if any_preds_written:
        mf.add_tags('_auto/def_and_notat_names_added')
    mf.write(info_note)