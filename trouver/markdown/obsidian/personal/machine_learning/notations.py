# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../../../nbs/18_markdown.obsidian.personal.machine_learning.notations.ipynb.

# %% auto 0
__all__ = []

# %% ../../../../../nbs/18_markdown.obsidian.personal.machine_learning.notations.ipynb 2
from deprecated import deprecated
from os import PathLike
import re
from typing import Optional

from fastai.text.all import *
import pandas as pd
import spacy
from trouver.helper import (
    current_time_formatted_to_minutes, find_regex_in_text,
    defs_and_notats_separations, replace_string_by_indices,
    notation_asterisk_indices,
    double_asterisk_indices, latex_indices
)
# from trouver.machine_learning.text.encoder_decoder import (
#     EncoderRNN, AttnDecoderRNN, train, trainIters, evaluate,
#     evaluateRandomly
# )
# from trouver.machine_learning.text.tokenize import (
#     replace_bold, replace_math_mode_strings, special_cases
# )
from ....markdown.file import MarkdownFile, MarkdownLineEnum
from trouver.markdown.obsidian.personal.note_processing import (
    process_standard_information_note
)
from ..notes import notes_linked_in_note, notes_linked_in_notes_linked_in_note
# from trouver.markdown.obsidian.personal.notation import (
#     make_a_notation_note, latex_to_path_accepted_string, make_notation_notes_from_double_asts)

from ...vault import VaultNote
