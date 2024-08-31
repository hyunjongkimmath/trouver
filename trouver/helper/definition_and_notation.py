"""Functions that deal with definitions and notations"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/39_helper.definition_and_notation.ipynb.

# %% auto 0
__all__ = ['double_asterisk_indices', 'notation_asterisk_indices', 'definition_asterisk_indices', 'defs_and_notats_separations']

# %% ../../nbs/39_helper.definition_and_notation.ipynb 2
from .regex import find_regex_in_text

# %% ../../nbs/39_helper.definition_and_notation.ipynb 6
def double_asterisk_indices(
        text: str # the str in which to find the indices of double asterisk surrounded text.
        ) -> list[tuple[int, int]]: # Each tuple is of the form `(start,end)`, where `text[start:end]` is a part in `text` with double asterisks, including the double asterisks.
    # TODO: fix double asterisks in math mode.
    """Return the indices in `str` of text surrounded by double asterisks.
    
    Assumes there no LaTeX math mode string has double asterisks.

    **See Also**
    
    - `notation_asterisk_indices`
    - `definition_asterisk_indices`
    """
    return find_regex_in_text(text, pattern='\*\*[^*]+\*\*')



# %% ../../nbs/39_helper.definition_and_notation.ipynb 8
def notation_asterisk_indices(
        text: str # the str in which to find the indices of notations surrounded by double asterisks.
        ) -> list[tuple[int, int]]: # Each tuple is of the form `(start,end)`, where `text[start:end]` is a part in `text` with LaTeX math mode text with double asterisks, including the double asterisks.
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


def definition_asterisk_indices(
        text: str # The str in which to find the indices of the definitions surrounded by double asterisks.
        ) -> list[tuple[int, int]]: # Each tuple is of the form `(start,end)`, where `text[start:end]` is a substring in `text` surrounded by double asterisks, including the double asterisks.
    """Return the indices of definition text surrounded by double asterisks.
    
    A double-asterisk-surrounded-text is a definition almost always
    when it is not purely LaTeX math mode text.
    
    Assumes that no LaTeX math mode string has double asterisks and that no
    LaTeX math mode string has the dollar sign character within it.
    """
    all_double_asterisks = double_asterisk_indices(text)
    notations = notation_asterisk_indices(text)
    return [tuppy for tuppy in all_double_asterisks if tuppy not in notations]

# %% ../../nbs/39_helper.definition_and_notation.ipynb 22
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