# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../../../nbs/23_markdown.obsidian.personal.machine_learning.information_note_types.ipynb.

# %% auto 0
__all__ = ['LABEL_TAGS', 'note_is_labeled_with_tag', 'note_labels', 'gather_information_note_types',
           'append_to_information_note_type_database', 'predict_text_types', 'predict_note_types',
           'automatically_add_note_type_tags', 'convert_auto_tags_to_regular_tags_in_notes']

# %% ../../../../../nbs/23_markdown.obsidian.personal.machine_learning.information_note_types.ipynb 3
LABEL_TAGS = [
    '#_meta/concept', '#_meta/exercise', '#_meta/definition', '#_meta/example', 
    '#_meta/narrative', '#_meta/notation', '#_meta/proof', '#_meta/remark',
    '#_meta/TODO/split', '#_meta/TODO/merge', '#_meta/TODO/delete', '#_meta/hint',
    '#_meta/how_to', '#_meta/conjecture', '#_meta/convention',
    '#_meta/context',
]

# %% ../../../../../nbs/23_markdown.obsidian.personal.machine_learning.information_note_types.ipynb 6
import os
from os import PathLike
from pathlib import Path
import shutil
from typing import Optional
import warnings

from fastai.text.learner import TextLearner
import pandas as pd

from .....helper import current_time_formatted_to_minutes
from ....markdown.file import MarkdownFile
from .database_update import max_ID, append_to_database
from ..note_processing import process_standard_information_note
from ...vault import VaultNote

# %% ../../../../../nbs/23_markdown.obsidian.personal.machine_learning.information_note_types.ipynb 9
def note_is_labeled_with_tag(
        note: VaultNote,
        label_tag: str # A tag which labels a type that `note` is. Includes the beginning hashtag `#`, e.g. `#_meta/definition`, `#_meta/TODO/split`
        ) -> bool: # `True` if `note` is labeled as type `label_type`.
    """
    Return `True` if the standard information note is labeled as
    begin a specified type.

    **Raises**

    - `ValueError`
        - If `label_tag` does not include the beginning hashtag `#`.
    """
    # assert is_standard_information_note
    if not label_tag.startswith('#'):
        raise ValueError(f"`label_tag` does not start with a hashtag `#`: {label_tag}")
    label_tag = label_tag[1:]
    mf = MarkdownFile.from_vault_note(note)
    return label_tag in mf.metadata()['tags']



# %% ../../../../../nbs/23_markdown.obsidian.personal.machine_learning.information_note_types.ipynb 11
def note_labels(
        note: VaultNote
        ) -> dict[str, str]:
        # Each key is a string, which is a tag, including the starting hashtag `#`. Each value is a string, either `'IS {tag}'` or `'NOT {tag}'`.
    """Return a dict indicating what labels a note has.

    The labels come from the `LABEL_TAGS` dict.
    """
    label_dict = {label_tag: note_is_labeled_with_tag(note, label_tag)
                  for label_tag in LABEL_TAGS}
    return {tag: (f'IS {tag}' if flag else f'NOT {tag}')
            for tag, flag in label_dict.items()}
    

# %% ../../../../../nbs/23_markdown.obsidian.personal.machine_learning.information_note_types.ipynb 14
def gather_information_note_types(
        vault: PathLike,
        notes: list[VaultNote],
        ) -> pd.DataFrame: # Has columns `Time added`, `Time modified`, `Note name`, `Full note content`, `Processed note content` as well as columns for each tag label. See `append_to_information_note_type_database` for more details about these columns.
    """
    Return a `pandas.DataFrame` encapsulating the data of note labels.
    """
    labels_of_notes = [note_labels(note) for note in notes]
    rows = []
    current_time = current_time_formatted_to_minutes()
    for i, (note, labels_of_note) in enumerate(zip(notes, labels_of_notes)):
        mf = MarkdownFile.from_vault_note(note)
        rows.append({
            'Time added': current_time,
            'Time modified': current_time,
            'Note name': note.name,
            'Full note content': str(mf), 
            'Processed note content': str(process_standard_information_note(
                mf, vault)),
            **labels_of_note
        })
    return pd.DataFrame(rows)
    # notes_with_processed_text_and_
    # process_standard_information_note


# %% ../../../../../nbs/23_markdown.obsidian.personal.machine_learning.information_note_types.ipynb 16
def append_to_information_note_type_database(
        vault: PathLike, # The vault freom which the data is drawn
        file: PathLike, # The path to a CSV file
        notes: list[VaultNote], # the notes to add to the database
        backup: bool = True # If `True`, makes a copy of `file` in the same directory and with the same name, except with an added extension of `.bak`.
        ) -> None:
    """
    Either create a `csv` file containing data for information note type
    labels or append to an existing `csv` file.

    The columns of the database file are as follows:

    - `Time added` - The time when the row was added.
    - `Time modified` - The time when the labels of the row 
    - `Note name` - The name of the note from which the data for the row
      was derived.
    - `Full note content` - The entire content/text of the note.
    - `Processed note content` - The "raw" content of the note without
      the YAML frontmatter meta, Markdown headings, links, footnotes, etc. 

    All timestamps are in UTC time and specify time to minutes
    (i.e. no seconds/microseconds).
    
    If a "new" note has the same processed content as a pre-existing
    note and anything is different about the "new" note, then update
    the row of the existing note. In particular, the following are updated:
    - Time modified (set to current time)
    - Note name (overwritten)
    - Full note content (overwritten)
    - Columns for categorization (overwritten)
    
    This method assumes that all the processed content in the
    CSV file are all distinct if the CSV file exists.
    """
    if not notes:
      return
    file = Path(file)
    df = pd.read_csv(file) if os.path.exists(file) else None
    # start_ID_from = max_ID(df) + 1 if not df is None else 1
    new_df = gather_information_note_types(vault, notes)
    cols = [
        'Time added', 'Time modified', 'Note name',
        'Full note content', 'Processed note content']
    cols.extend(LABEL_TAGS)
    cols_to_update = ['Time modified', 'Note name', 'Full note content']
    cols_to_update.extend(LABEL_TAGS)
    append_to_database(
        file, new_df, cols, 'Processed note content', cols_to_update, backup)


# %% ../../../../../nbs/23_markdown.obsidian.personal.machine_learning.information_note_types.ipynb 20
def predict_text_types(
        learn: TextLearner, # The ML model predicting note types.
        texts: list[str],
        remove_NO_TAG: bool = True # If `True`, remove `NO_TAG`, which in theory is supposed to indicate that no types are predicted, but in practice can somehow be predicted along with actual types.
        ) -> list[list[str]]: # Each list corresponds to a text and contains the predicted types of the text.
    """Predict the types of mathematical texts using an ML model."""
    predictions = []
    for text in texts:
        with learn.no_bar(), learn.no_logging():
            pred, loss, _ = learn.predict(text)
        if remove_NO_TAG and 'NO_TAG' in pred:
            pred.remove('NO_TAG')
        predictions.append(list(pred))
    return predictions

# %% ../../../../../nbs/23_markdown.obsidian.personal.machine_learning.information_note_types.ipynb 24
def predict_note_types(
        learn: TextLearner, # The ML model predicting note types.
        vault: PathLike, # The vault with the notes.
        notes: list[VaultNote], # The notes with texts to predict
        remove_NO_TAG: bool = True # If `True`, remove `NO_TAG`, which in theory is supposed to indicate that no types are predicted, but in practice can somehow be predicted along with actual types.
        ) -> list[list[str]]:
    markdown_files = [
        MarkdownFile.from_vault_note(note) for note in notes]
    raw_note_contents = [
        str(process_standard_information_note(mf, vault)) for mf in markdown_files]
    return predict_text_types(learn, raw_note_contents, remove_NO_TAG)

# %% ../../../../../nbs/23_markdown.obsidian.personal.machine_learning.information_note_types.ipynb 28
def automatically_add_note_type_tags(
        learn: TextLearner, # The ML model predicting note types.
        vault: PathLike, # The vault with the notes
        notes: list[VaultNote],
        add_auto_label: bool = True, # If `True`, adds `"_auto"` to the front of the note type tag to indicate that the tags were added via this automated script.
        overwrite: Optional[str] = None # Either `'w'`, `'ws'`, `'ww'`, `'a'`, or `None`. If `'w'` or `'ws'`, then overwrite any already-existing note type tags (from LABEL_TAGS), whether or not these tags are `_auto` tags, with the predicted tags. IF `'ww'`, then overwrite only the `_auto` tags among the already-existing note type tags with the predicted tags. If `'a'`, then preserve already-existing note type tags and just append the newly predicted ones; in the case that `learn` predicts the note type whose tag is already in the note, a new tag of that type is not added, even if `add_auto_label=True`. If `None`, then do not make modifications to each note if any note type tags already exist in the note; if the predicted note types are different from the already existing note types, then raise a warning.
        ) -> None:
    """
    Predict note types and add the predicted types as
    frontmatter YAML tags in the notes.

    Non-`_auto`-labeled tags take precedent over `auto`-labeled tags,
    unless `overwrite='w'`.
    
    **Raises**

    - Warning:
        - If `overwrite=None`, a note already has some note type tags,
        and `learn` predicts different note types as those in the note.
    
    """
    if overwrite not in ['w', 'ws', 'ww', 'a'] and overwrite is not None:
        raise ValueError(
            f"`overwrite` was expected to be 'w', 'ws,', 'ww', 'a', or None," 
            f" but was {overwrite}")
    predictions = predict_note_types(learn, vault, notes)
    # remove hashtags
    predictions = [[tag[1:] if tag.startswith('#') else tag for tag in tags]
                   for tags in predictions]
    # Add `_auto/`
    all_label_tags = [*LABEL_TAGS]
    all_label_tags.extend([f'_auto/{tag}' for tag in LABEL_TAGS])
    for note, prediction in zip(notes, predictions):
        _change_label_tags_for_single_note(
            note, prediction, overwrite, add_auto_label,
            all_label_tags)


def _change_label_tags_for_single_note(
        note: VaultNote, prediction: list[str], overwrite: Optional[str],
        add_auto_label: bool, all_label_tags: list[str]):
    mf = MarkdownFile.from_vault_note(note)

    if add_auto_label:
        tags_to_add = _auto_prediction(prediction)
    else:
        tags_to_add = prediction

    if overwrite in ['w', 'ws']:
        mf.remove_tags(all_label_tags)
        mf.add_tags(tags_to_add, skip_repeated_auto=True)
    elif overwrite == 'ww':
        mf.remove_tags(
            [tag for tag in all_label_tags if tag.startswith('_auto/')])
    elif overwrite == 'a':
        for tag in prediction:
            _append_single_predicted_tag(mf, tag, add_auto_label)
    else:  # overwrite=None
        if not _has_any_label_tags(mf):
            mf.add_tags(tags_to_add, skip_repeated_auto=True)
        elif not _has_exactly_predicted_tags(mf, prediction):
            warnings.warn(
                "The note type labeling tags in the note are different "
                "from the predicted note types. "
                f"The note type tags in the note have NOT been modified:"
                f"\n\nNote name: {note.name}"
                f"\n\nPredicted types: {prediction}", UserWarning)        
    mf.write(note)


def _auto_prediction(prediction: list[str]):
    return [f'_auto/{tag}' for tag in prediction]


def _append_single_predicted_tag(
        mf, tag, add_auto_label):
    if tag in mf.metadata()['tags']:
        return
    elif f'_auto/{tag}' in mf.metadata()['tags'] and add_auto_label:
        return
    elif f'_auto/{tag}' in mf.metadata()['tags'] and not add_auto_label:
        mf.remove_tags([f'_auto/{tag}'])
        mf.add_tags([tag])
    else:
        mf.add_tags([f'_auto/{tag}'] if add_auto_label else [tag])
    

def _has_exactly_predicted_tags(
        mf, prediction: list[str]) -> bool:
    """Return `True` if the MarkdownFile already has the predicted tags
    (or the corresponding `_auto` tags)"""
    for tag in LABEL_TAGS:
        if (mf.has_tag(tag) or mf.has_tag(f'_auto/{tag}')) and tag in prediction:
            continue
        else:
            return False
    return True


def _has_any_label_tags(
        mf) -> bool:
    """Return `True` if the MarkdownFile has any label tags (or correspnoding `_auto` tags)"""
    for tag in LABEL_TAGS:
        if mf.has_tag(tag) or mf.has_tag(f'_auto/{tag}'):
            continue
        else:
            return False
    return True

# %% ../../../../../nbs/23_markdown.obsidian.personal.machine_learning.information_note_types.ipynb 42
def convert_auto_tags_to_regular_tags_in_notes(
        notes: list[VaultNote], 
        exclude: list[str] = ['links_added', 'notations_added'] # The tags whose `_auto/` tags should not be converted. The str should not start with `'#'` and should not start with `'_auto/'`.
        ) -> None:
    """Convert the auto tags into regular tags for the notes.
    """
    for note in notes:
        mf = MarkdownFile.from_vault_note(note)
        mf.replace_auto_tags_with_regular_tags(exclude)
        mf.write(note)
