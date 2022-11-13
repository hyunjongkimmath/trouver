# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_helper.ipynb.

# %% ../nbs/00_helper.ipynb 2
from __future__ import annotations
from collections import OrderedDict
from collections.abc import Iterable
import datetime
from datetime import timezone
import errno
import glob
from graphlib import TopologicalSorter
from itertools import product
import os
from os import PathLike
from pathlib import Path
import platform
import re
from typing import Callable, Optional, Pattern, Sequence, Union

from deprecated import deprecated
from natsort import natsorted

# %% auto 0
__all__ = ['ALPHABET_TO_ALPHABET_GROUP_DICT', 'ALPHABET_OR_GREEK_TO_ALPHABET_DICT', 'find_regex_in_text',
           'replace_string_by_indices', 'double_asterisk_indices', 'notation_asterisk_indices',
           'definition_asterisk_indices', 'defs_and_notats_separations', 'latex_indices', 'is_number', 'existing_path',
           'file_existence_test', 'path_name_no_ext', 'path_no_ext', 'text_from_file', 'files_of_format_sorted',
           'current_time_formatted_to_minutes', 'containing_string_priority', 'default_str_comparison',
           'natsort_comparison', 'graph_for_topological_sort', 'dict_with_keys_topologically_sorted',
           'alphabet_to_alphabet_group', 'alphabet_or_latex_command_to_alphabet',
           'alphabet_or_latex_command_to_alphabet_group']

# %% ../nbs/00_helper.ipynb 5
def find_regex_in_text(
        text: str, # Text in which to find regex patter
        pattern: str | Pattern[str] # The regex pattern
        ) -> list[tuple[int]]: # Each tuple is of the form `(a,b)` where `text[a:b]` is the regex match.
    # TODO: rename into regex_indices_in_text
    # TODO: swap parameters.
    """Return ranges in `text` where `pattern` occurs.
    """
    matches = re.finditer(pattern, text)
    return [match.span() for match in matches]

# %% ../nbs/00_helper.ipynb 14
def replace_string_by_indices(
        string: str, # String in which to make replacemenets 
        replace_ranges: Sequence[Union[Sequence[int], int]], # A list of lists/tuples of int's or a single list/tuple of int's. Each 
        replace_with: Sequence[str] | str # The str(s) which will replace the substrings at `replace_ranges` in `string`. `replace_with` must be a str exactly when `replace_ranges` is a Sequence of a single Sequence of int.
        ) -> str:  # The str obtained by replacing the substrings at `replace_range` in `string` by the strs specified by `replace_with`.
    """Replace parts of ``string`` at the specified locations"

    Use this with `find_regex_in_text`.

    **Parameters**

    - ``string`` - `str`
    - ``replace_ranges`` - `Sequence[Sequence[int] | int]`
        - Either a list of lists/tuples of one or two int's. A list/tuple
        ``[a,b]`` or ``(a,b)`` means that ``string[a:b]`` is to be replaced.
        ``[a]`` or ``(a)`` means that ``string[a:]`` is to be replaced. The ranges should
        not overlap and should be arranged in chronological order.
    - ``replace_with`` - `Sequence[str] | str`
        - The str's which will replace the parts represented by 
        ``replace_ranges``. ``replace_ranges`` and ``replace_with`` must be
        both lists or both not lists. If they are lists, they must be of 
        the same length.

    **Returns**

    - str

    """
    if isinstance(replace_with, str):
        replace_ranges = [replace_ranges]
        replace_with = [replace_with]
    if len(replace_ranges) != len(replace_with):
        raise ValueError(
            'The lengths of `replace_ranges` and `replace_with` are different.')
    if len(replace_ranges) == 0:
        return string

    str_parts = _str_parts(string, replace_ranges, replace_with)
    return "".join(str_parts)


def _str_parts(string, replace_ranges, replace_with):
    """Divide `string` into parts divided outside of `replace_ranges`
    and with `replace_with` inserted."""
    str_parts = []
    for i, replace_string in enumerate(replace_ranges):
        replace_string = replace_with[i]
        if i > 0 and len(replace_ranges[i-1]) == 1:
            unreplaced_start_index = len(string)
        elif i > 0 and len(replace_ranges[i-1]) != 1:
            unreplaced_start_index = replace_ranges[i-1][1]
        else:
            unreplaced_start_index = 0
        unreplaced_end_index = replace_ranges[i][0]
        str_parts.append(string[unreplaced_start_index:unreplaced_end_index])
        str_parts.append(replace_string)
    # Add the last (unreplaced) part to str_parts.
    if len(replace_ranges[-1]) == 1:
        unreplaced_start_index = len(string)
    else:
        unreplaced_start_index = replace_ranges[-1][1]
    str_parts.append(string[unreplaced_start_index:])
    return str_parts

# %% ../nbs/00_helper.ipynb 21
def double_asterisk_indices(
        text: str # the str in which to find the indices of double asterisk surrounded text.
        ) -> list[tuple[int]]: # Each tuple is of the form `(start,end)`, where `text[start:end]` is a part in `text` with double asterisks, including the double asterisks.
    # TODO: fix double asterisks in math mode.
    """Return the indices in `str` of text surrounded by double asterisks.
    
    Assumes there no LaTeX math mode string has double asterisks.

    **See Also**
    
    - `notation_asterisk_indices`
    - `definition_asterisk_indices`
    """
    return find_regex_in_text(text, pattern='\*\*[^*]+\*\*')



# %% ../nbs/00_helper.ipynb 23
def notation_asterisk_indices(
        text: str # the str in which to find the indices of notations surrounded by double asterisks.
        ) -> list[tuple[int]]: # Each tuple is of the form `(start,end)`, where `text[start:end]` is a part in `text` with LaTeX math mode text with double asterisks, including the double asterisks.
    """Return the indices of notation text surrounded by double asterisks.
    
    A double-asterisk-surrounded-text is a notation almost always
    when it is purely LaTeX math mode text. 

    Assumes that no LaTeX math mode string has the dollar sign character
    within it.
    """
    return find_regex_in_text(
        text, pattern='\*\*\$\$[^$]+\$\$\*\*|\*\*\$[^$]+\$\*\*')
    # I previous used this, but it was not picking up notation LaTeX str
    # containing asterisks, e.g. `**$\pi^*$**``, `**$\pi_*$**`.`
    return find_regex_in_text(
        text, pattern='\*\*\$\$[^*$]+\$\$\*\*|\*\*\$[^*$]+\$\*\*')


def definition_asterisk_indices(text: str) -> list[tuple[int]]:
    """Returns the indices of definition text surrounded by double asterisks.
    
    A double-asterisk-surrounded-text is a definition almost always
    when it is not purely LaTeX math mode text.
    
    Assumes that no LaTeX math mode string has double asterisks and that no
    LaTeX math mode string has the dollar sign character within it.
    """
    all_double_asterisks = double_asterisk_indices(text)
    notations = notation_asterisk_indices(text)
    return [tuppy for tuppy in all_double_asterisks if tuppy not in notations]

# %% ../nbs/00_helper.ipynb 37
def defs_and_notats_separations(
        text: str 
        )-> list[tuple[int, bool]]:
    """Finds the indices in the text where double asterisks occur and
    categorizes whether each index is for a definition or a notation.
    
    **Parameters**

    - text - str

    **Returns**

    - list[tuple[int, bool]]
        - Each tuple is of the form `(start, end, is_notation)`, where
        `text[start:end]` is the double-asterisk surrounded string,
        including the double asterisks.
    """
    all_double_asterisks = double_asterisk_indices(text)
    notations = notation_asterisk_indices(text)
    return [(start, end, (start, end) in notations)
            for start, end in all_double_asterisks]

# %% ../nbs/00_helper.ipynb 41
def latex_indices(text: str) -> list[tuple[int]]:
    """Returns the indices in the text containing LaTeX str.
    
    This may not work correctly if the text has a LaTeX
    formatting issue or if any LaTeX string has a dollar sign `\$`.
    
    **Parameters**

    - text - str

    **Returns**

    - tuple[int]
        - Each tuple is of the form `(start, end)` where
        `text[start:end]` is a LaTeX string, including any leading trailing
        dollar signs (`$` or `$$`).
    """
    # r'(?<!\\)\$.*(?<!\\)\$|(?<!\\)\$(?<!\\)\$.*(?<!\\)\$(?<!\\)\$'
    return find_regex_in_text(text, r'((?<!\\)\$\$?)[^\$]*\1')
    # return find_regex_in_text(text, '\$\$[^\$]*\$\$|\$[^\$]*\$')

# %% ../nbs/00_helper.ipynb 49
def is_number(
        x: Union[float, int, complex, str]
        ) -> bool:
    """Return `True` if the input `x` represents a number.
    
    This function is different from Python's built-in `is_numeric`
    function, which returns `True` when all characters of a string
    are digits.
    """
    if isinstance(x, (float, int, complex)):
        return True
    #For the case where string is None
    if x is None:
        return False
    if x and x[0] == '-': x = x[1:]
    return x.replace(".", "1", 1).isdigit()

# %% ../nbs/00_helper.ipynb 53
def existing_path(
        path: PathLike,  # A file or directory path. Either absolute or relative to `relative_to`.
        relative_to: Optional[PathLike] = None  # Path to the directory that `file` is relative to.  If `None`, then `path` is an absolute path.
        ) -> Path: # The path formed by `relative_to` adjoined with `path`.  Defaults to `None`
    """Returns a path relative to a specified path as an absolute path
    that exists.

    **Raises**

    - `FileNotFoundError`
        - If `relative_to` is not `None` but does not exist, or if
        `file` does not exist.
    - `ValueError`
        - If `relative_to` is not `None` and yet not an absolute path, or
        if `relative_to` is `None` at yet `path` is not an absolute path.
    
    **Notes**
    - This function may add the string `'\\\\?\\'` in front, which identifies
    very long paths.
    """
    if relative_to is not None:
        if not os.path.isabs(relative_to):
            raise ValueError(
                f'The parameter `relative_to` is expected to be an'
                f' absolute path, but it is not: {relative_to}')
        if not os.path.exists(relative_to):
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), relative_to)
        path = Path(relative_to) / path
    elif not os.path.isabs(path):
        raise ValueError(
            f'The parameter `path` is expected to be an absolute path,'
            f' but it is not: {path}')
    if not os.path.exists(path) and platform.system() == 'Windows':
        path = f'\\\\?\\{str(path)}'  # For long file names
    if not os.path.exists(path):
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), path)
    return Path(path)


@deprecated(reason="The function has been renamed to `existing_path`")
def file_existence_test(
        path: PathLike,  # A file or directory path. Either absolute or relative to `relative_to`.
        relative_to: Optional[PathLike] = None  # Path to the directory that `file` is relative to.  If `None`, then `path` is an absolute path.
        ) -> Path: # The path formed by `relative_to` adjoined with `path`.  Defaults to `None`
    """
    **Deprecated. Use `existing_path` instead.**
    
    Returns a path relative to a specified path as an absolute path
    that exists.

    **Raises**
    - `FileNotFoundError`
        - If `relative_to` is not `None` but does not exist, or if
        `file` does not exist.
    
    **Notes**
    - This function may add the string `'\\\\?\\'` in front, which identifies
    very long paths.
    """
    if relative_to is not None:
        if not os.path.isabs(relative_to):
            raise ValueError(
                f'The parameter `relative_to` is expected to be an'
                f' absolute path, but it is not: {relative_to}')
        if not os.path.exists(relative_to):
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), relative_to)
        path = Path(relative_to) / path
    elif not os.path.isabs(path):
        raise ValueError(
            f'The parmaeter `path` is expected to be an absolute path,'
            f' but it is not: {path}')
    if not os.path.exists(path) and platform.system() == 'Windows':
        path = f'\\\\?\\{str(path)}'  # For long file names
    if not os.path.exists(path):
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), path)
    return Path(path)

# %% ../nbs/00_helper.ipynb 66
def path_name_no_ext(
        path: PathLike # The path of the file or directory. This may be absolute or relative to any directory.
        ) -> str: # The name of the file or directory without the extension.
    """Return the name of a file or directory from its path without the
    extension.
    
    The file or directory does not have to exist.
    """
    name_with_extension = os.path.basename(path)
    return os.path.splitext(name_with_extension)[0]

# %% ../nbs/00_helper.ipynb 73
def path_no_ext(
    path: PathLike # The path of the file or directory. This may be absolute or relative to any directory.
    ) -> str: # The path of the file or directory without the extension. If `path` is a path to a directory, then the output should be essentially the same as `path`.
    """Returns the path of a file or directory without the extension.
    
    The file or directory does not have to exist.
    """
    return os.path.splitext(str(path))[0]

# %% ../nbs/00_helper.ipynb 77
def text_from_file(
        path: PathLike, # The absolute path of the file.
        encoding: str = 'utf8' # The encoding of the file to be read. Defaults to `'utf8'`.
        ) -> str: # The entire text from a file
    """Return the entire text from a file.
    """
    with open(path, 'r', encoding=encoding) as file:
        text = file.read()
        file.close()
    return text

# %% ../nbs/00_helper.ipynb 79
def files_of_format_sorted(
        directory: PathLike, # The directory in which to find the files
        extension: str = 'txt' # Extension of the files to find. Defaults to 'txt'.
        ) -> list[str]:
    """Return a list of path str of files in the directory (but not subdirectories)
    sorted via `natsort`.
    """
    return natsorted(glob.glob(str(Path(directory) / f'*.{extension}')))

# %% ../nbs/00_helper.ipynb 83
def current_time_formatted_to_minutes(
        ) -> str:
    """Return the current time to minutes.

    **Returns**

    - str
        - In UTC time, to minutes.
    """
    dt = datetime.datetime.now(timezone.utc)
    formatted = dt.isoformat(timespec='minutes')
    return formatted[:16]

# %% ../nbs/00_helper.ipynb 91
def containing_string_priority(str1: str, str2: str) -> int:
    """Returns 1, 0, -1 depending on whether one string contains the other.
    
    TODO make the string containment criterion looser, e.g. finite Galois etale cover
    "contains" finite etale cover.
    
    **Parameters**
    - str1 - str
    - str2 - str
    """
    if str2 in str1:
        return -1
    elif str1 in str2:
        return 1
    else:
        # return len(str2) - len(str1)
        return 0


def default_str_comparison(str1: str, str2: str) -> int:
    """
    
    **Parameters**
    - str1 - str
    - str2 - str
    """
    if str1 > str2:
        return 1
    elif str1 < str2:
        return -1
    else:
        return 0


def natsort_comparison(str1: str, str2: str) -> int:
    """
    
    **Parameters**
    - str1 - str
    - str2 - str
    """
    if str1 == str2:
        return 0
    listy = [str1, str2]
    natsorted(listy)
    if listy[0] == str1:
        return -1
    else:
        return 1

# %% ../nbs/00_helper.ipynb 92
def graph_for_topological_sort(
        items_to_sort: Iterable[str],
        key_order: Callable[[str, str], int]) -> dict[str, set[str]]:
    """
    **Parameters**
    - items_to_sort - Iterable[str]
    - key_order: Callable[[str, str], int]
        - Comparing str1 against str2 results in a positive number if
        str1 is "greater" than str2 (i.e. str1 is of a later priority)
    
    **Returns**
    - dict[str, set[str]]
        - A dict whose keys are the elements `k` of `items_to_sort` and
        whose values are sets of elements `k2` of `items_to_sort` such that
        `key_order(k, k2) > 0`.
    """
    graph = dict()
    for key_1, key_2 in product(items_to_sort, items_to_sort):
        # print(key_1, key_2)
        if key_1 == key_2:
            continue
        # print(key_1, key_2)
        # print(key_order(key_1, key_2))
        if key_1 not in graph:
            graph[key_1] = set()
        if key_order(key_1, key_2) > 0:
            graph[key_1].add(key_2)
    return graph

# %% ../nbs/00_helper.ipynb 93
def dict_with_keys_topologically_sorted(
        dict_to_sort: dict[str],
        key_order: Callable[[str, str], int],
        reverse: bool = False) -> OrderedDict[str]:
    """Returns an OrderedDict whose keys are sorted topologically by
    the specified key order.
    
    **Parameters**
    - dict_to_sort - dict[str]
        - The dict whose keys need to be ordered.
    - key_order
        - The comparison function on the keys of `dict_to_sort`. Defaults to
        the key function for the comparison ``containing_string_priority``.
    - reverse - bool
        - Defaults to `False`
        
    **Returns**
    - OrderedDict[str]
    """
    graph = graph_for_topological_sort(dict_to_sort, key_order)
    ts = TopologicalSorter(graph)
    keys_ordered = list(ts.static_order())
    if reverse:
        keys_ordered = list(reversed(keys_ordered))
    return OrderedDict((key, dict_to_sort[key]) for key in keys_ordered)


# %% ../nbs/00_helper.ipynb 96
ALPHABET_TO_ALPHABET_GROUP_DICT = {'A': 'A-E', 'B': 'A-E', 'C': 'A-E', 'D': 'A-E', 'E': 'A-E', 'F': 'F-J', 'G': 'F-J', 'H': 'F-J', 'I': 'F-J', 'J': 'F-J', 'K': 'K-O', 'L': 'K-O', 'M': 'K-O', 'N': 'K-O', 'O': 'K-O', 'P': 'P-T', 'Q': 'P-T', 'R': 'P-T', 'S': 'P-T', 'T': 'P-T', 'U': 'U-Z', 'V': 'U-Z', 'W': 'U-Z', 'X': 'U-Z', 'Y': 'U-Z', 'Z': 'U-Z'}
ALPHABET_OR_GREEK_TO_ALPHABET_DICT = {}
def alphabet_to_alphabet_group(character) -> str:
    """
    Returns the alphabet group
    
    In my vaults, I often alphabetize things and also group
    the alphabet as follows:
    - A-E
    - F-J
    - K-O
    - P-T
    - U-V
    
    **Parameters**
    - character - str
    
    **Returns**
    - str or `None`
        - Returns `None` if `character` is not an alphabet.
    """
    character = character.upper()
    if character in ALPHABET_TO_ALPHABET_GROUP_DICT:
        return ALPHABET_TO_ALPHABET_GROUP_DICT[character]
    else:
        return None

def alphabet_or_latex_command_to_alphabet(character):
    """Returns the alphabet that the character "corresponds to".
    
    """
    # TODO
    return

def alphabet_or_latex_command_to_alphabet_group(character):
    return alphabet_to_alphabet_group(
        alphabet_or_latex_command_to_alphabet(character))
