# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb.

# %% auto 0
__all__ = ['CHARACTER_ORDERING_LIST', 'DECORATING_CHARACTERS', 'NONEFFECTIVE_CHARACTERS', 'TO_REMOVE', 'TO_UNDERSCORE',
           'MAX_NOTE_NAME_LENGTH', 'SPECIAL_CHARACTERS', 'replaceable_groups', 'REPLACEABLES',
           'latex_to_path_accepted_string', 'parse_notation_note', 'notation_in_note', 'main_of_notation',
           'notation_str_in_a_standard_information_note', 'notation_notes_linked_in_see_also_section',
           'notations_and_main_notes', 'notation_note_is_linked_in_see_also_section', 'add_notation_note_to_see_also',
           'add_missing_notation_links_to_information_notes', 'notations_to_add_in_index',
           'index_notation_note_formatted_entry', 'make_a_notation_note', 'make_notation_notes_from_double_asts',
           'regex_from_latex', 'regex_from_notation_note']

# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 2
from os import PathLike
from pathlib import Path
import re
from typing import Optional, Union
import warnings

from multiset import Multiset
from pylatexenc.latexwalker import LatexNode, LatexMacroNode, LatexWalker, LatexGroupNode, LatexCharsNode

from ....helper import notation_asterisk_indices
from ...markdown.file import MarkdownFile, MarkdownLineEnum
from trouver.markdown.obsidian.links import (
    find_links_in_markdown_text, LinkType, ObsidianLink, MARKDOWNLINK_PATTERN, WIKILINK_PATTERN
)
from .information_notes import bulleted_links_of_type_in_section
from trouver.markdown.obsidian.personal.note_type import (
    PersonalNoteTypeEnum, assert_note_is_of_type, note_is_of_type
)
from ..vault import VaultNote, NotePathIsNotIdentifiedError, NoteDoesNotExistError

# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 5
CHARACTER_ORDERING_LIST =\
    ['A', 'a', r'\Alpha', r'\alpha', 'B', 'b', r'\Beta', r'\beta', 'C', 'c', r'\Gamma',
     r'\gamma', 'D', 'd', r'\Delta', r'\delta', 'E', 'e', r'\Epsilon', r'\epsilon',
     'F', 'f', 'G', 'g', 'H', 'h', r'\Eta', r'\eta', 'I', 'i', r'\Iota', r'\iota',
     'J', 'j', 'K', 'k', r'\Kappa', r'\kappa', 'L', 'l', r'\Lambda', r'\lambda', 'M',
     'm', r'\Mu', r'\mu', 'N', 'n', r'\Nu', r'\nu', 'O', 'o', r'\Omicron', r'\omicron'
     'P', 'p', r'\Pi', r'\pi', r'\Phi', r'\phi', r'\Psi', r'\psi', 'Q', 'q', 'R', 'r', 
     r'\Rho', r'\rho', 'S', 's', r'\Sigma', r'\sigma', 'T', 't', r'\Theta', r'\theta',
     r'\Tau', r'\tau', 'U', 'u', r'\Upsilon', r'\upsilon', 'V', 'v', 'W', 'w', r'\Omega', r'\omega',
     'X', 'x', '\Chi', '\chi', 'Y', 'y', 'Z', 'z', '\Zeta', '\zeta', '*', r'\bullet']
DECORATING_CHARACTERS =\
    [r'\tilde', r'\hat', r'\overline', r'\bar', r'\mathscr', r'\mathcal',
     r'\mathfrak', r'\\operatorname', r'\\text', r'\\bf']
NONEFFECTIVE_CHARACTERS =\
    ['^', '_', '{', '}', '(', ')', '[', ']']

# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 6
TO_REMOVE = [
    '.', '\'', '$', ')', '{', '}', ':', '?', '!', '#', '%', '&',
    '\\', '<', '>', '*', '?', '"', '@', '+', '`', '|', '=', '[', ']',
    'mathscr', 'mathbf', 'mathrm', 'mathfrak', 'mathcal', 'mathbb', 'operatorname',
    'left', 'right']
TO_UNDERSCORE = [' ', '-', '^', '(', ',', '/']

# TODO: make a universal latex to path string; it seems that latex.convert
# might do something different when naming files.

def latex_to_path_accepted_string(latex: str) -> str:
    """Convert a latex string to a path accepted string
    """
    for to_remove in TO_REMOVE:
        latex, _ = re.subn(re.escape(to_remove), '', latex)
    for to_underscore in TO_UNDERSCORE:
        latex, _ = re.subn(re.escape(to_underscore), '_', latex)
    return latex

# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 11
def _main_of_notation_from_text(
        file_text: str # Text of notation note
        ) -> Union[str, VaultNote, None]: # The name main information note that `notation_note` comes from. Returns `None` if `notation_note` does not come from such a note.
    """Return the name of the note from which the notation comes from.

    Helper function for `parse_notation_string`.
    """
    if '%%' in file_text and 'main: ' in file_text:
        return None

    # First, get rid of the notation, i.e. the first latex math mode string
    match = re.search(fr'\$.+?\$\s+', file_text) 
    if match is None:
        raise ValueError(
            'There seems to be a formatting error in a notation note'
            ' and the notation has not been identified. The following is the'
            f' name of the notation note: {notation_note.name}')
    start, end = match.span()
    file_text = file_text[end:]
    
    link_locations = find_links_in_markdown_text(file_text)
    if not link_locations:
        return None
    start, end = link_locations[0]
    link_str = file_text[start:end]
    link_parse = ObsidianLink.from_text(link_str)
    main_note_name = link_parse.file_name
    return main_note_name

# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 15
def _divide_bulleted_list_mf_at_end(
        mf: MarkdownFile
        ) -> tuple[MarkdownFile, Union[MarkdownFile, None]]: # The first MarkdownFile contains the main content. The second MarkdonwFile contains the bulleted list at the end; if no such bulleted list exists, then this is None.
    """Divide a `MarkdownFile` for a notation note into two MarkdownFiles, one
    of the main content and the other for the trailing bulleted list of links
    for notations used in the notation note.

    Assumes that the bulleted list is formatted correctly
    (i.e. each line is of the form `- [<notation>](<link>)`)

    Helper function for `parse_notation_note`.
    """
    main_parts = mf.parts.copy()
    trailing_parts = []
    for part in reversed(mf.parts):
        if part['type'] == MarkdownLineEnum.BLANK_LINE:
            main_parts.pop()
            continue
        if not _part_is_unordered_list_and_is_of_markdownstyle_link(part):
            break
        last_part = main_parts.pop() # Should be the same as `part`
        trailing_parts.insert(0, last_part)
    
    if trailing_parts:
        bulleted_list_mf = MarkdownFile(trailing_parts)
    else:
        bulleted_list_mf = None
    return MarkdownFile(main_parts), bulleted_list_mf

def _part_is_unordered_list_and_is_of_markdownstyle_link(
        part: dict[str, Union[str, MarkdownLineEnum]]
        ) -> bool:
    """
    
    Helper function for `_divide_bulleted_list_mf_at_end`
    """
    if part['type'] != MarkdownLineEnum.UNORDERED_LIST:
        return False
    if not part['line'].startswith('- '):
        return False
    if not re.match(MARKDOWNLINK_PATTERN, part['line'][2:]):
        return False
    return True
    

# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 17
def parse_notation_note(
        notation_note: Union[str, VaultNote],
        vault: Optional[PathLike] = None # The vault If `None`, then uses th
        ) -> tuple[Union[dict, None], Union[str, None], str, MarkdownFile,
                   Union[MarkdownFile, None]]:
    """Parse information from the notation note.

    **Returns**

    - tuple[Union[dict, None], str, ObsidianLink, MarkdownFile, MarkdownFile]
        - The first entry is the YAML frontmatter meta, if available.
        - The second entry is the notation string
        - The third entry is the name of the "main note" of the notation note. This is usual
          the linked note in the link `[[<linked_note>|denotes]]`. If no such main note
          exists, then this is `None`.
        - The fourth entry is the MarkdownFile consisting of the "main" content of the note,
          which excludes the information given by all of the other entries.
        - The fifth entry is the MarkdownFile consisting of the ending bulleted list, listing
          the notations used in the notation notes along with links to the notation notes
          describing these notations. If there is not such bulleted list, then this entry
          is `None`. 

    **Raises**

    - UserWarning
        - If the (non-YAML frontmatter meta) contents of the note do not start
        inn the form `<Notation> [[<link_to_note>|denotes]]`; the name of the
        notation note is included in the warning message.
    - ValueError
        - If the notation note is not formatted correctly by starting
        with the notation with dollar signs `$`.
    - AssertionError
        - If `notation_note` is not determined to be a notation note.
    """
    if isinstance(notation_note, str):
        notation_note = VaultNote(vault, name=notation_note)
    if not vault:
        vault = notation_note.vault
    assert_note_is_of_type(notation_note, PersonalNoteTypeEnum.NOTATION_NOTE)

    mf = MarkdownFile.from_vault_note(notation_note)
    metadata = mf.metadata()
    mf_without_metadata = MarkdownFile(
        [part for part in mf.parts if part['type'] != MarkdownLineEnum.META])

    file_text = str(mf_without_metadata)

    main_mf, mf_with_links_to_notations = _divide_bulleted_list_mf_at_end(mf_without_metadata)
    _remove_the_notation_str_and_denotes_in_main_mf(main_mf, notation_note)

    return (metadata, _get_notation_string(file_text, notation_note),
            _main_of_notation_from_text(file_text), main_mf,
            mf_with_links_to_notations)


def _get_notation_string(
        file_text: str,
        notation_note: VaultNote
        ) -> str:
    """Return the notation string from the text of the notation note..

    Assumes that the notation string exists and is well formatted.

    Helper function for `parse_notation_note`.
    """
    try:
        return re.search(r'\$.+?\$', file_text).group()
    except AttributeError as e:
        raise ValueError(
            'There seems to be a formatting error in a notation note'
            ' and the notation has not been identified. The following is the'
            f' name of the notation note: {notation_note.name}')
    

def _remove_the_notation_str_and_denotes_in_main_mf(
        main_mf: MarkdownFile,
        notation_note: VaultNote):
    """Remove the text `<notation> denotes ` which starts the
    notation description.

    Helper function of `parse_notation_note`.
    """
    for part in main_mf.parts:
        if part['type'] == MarkdownLineEnum.BLANK_LINE:
            continue
        match = re.match(fr'^\$.+?\$ ({WIKILINK_PATTERN}|denotes)\s*', part['line']) 
        if match is None:
            raise ValueError(
                'There seems to be a formatting error in a notation note'
                ' and the notation has not been identified. The following is the'
                f' name of the notation note: {notation_note.name}')
        else:
            start, end = match.span()
            part['line'] = part['line'][end:]
            break
    

# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 24
def notation_in_note(
        notation_note: Union[str, VaultNote],
        vault: Optional[PathLike] = None 
        ) -> str:
    """Return the name of the note from which the notation comes from.
    
    **Parameters**

    - `notation_note` - Union[str, VaultNote]
        - Either
            
            - The name of the notation note or
            - The `VaultNote` object of the notation note. 
            
        The note name is expected to be unique
        inside the vault specified by `vault`. 
        This is expected to contain `'notation'` as a substring. 
        Usually, this is expected to be formatted in one of
        the following forms:
            - `'<reference_name>_notation_<rest_of_note_name>'`
            - `'notation.<rest_of_note_name>'
    - `vault` - Pathlike or `None`
        - Defaults to `None`
        
    **Returns**

    - str
        - The notation in LaTeX, including the dollar signs `$`.

    **Raises**

    """
    _, notation_in_note, _, _, _ = parse_notation_note(notation_note, vault)
    return notation_in_note

# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 27
def main_of_notation(
        notation_note: VaultNote, # The VaultNote object representing the notation note.
        as_note: bool = False # If `False`, then returns the name of the note, and returns a VaultNote object with the same vault as `notation_note` otherwise. The vault used to get the `VaultNote` is the vault of `notation_note`.
        ) -> Union[str, VaultNote, None]: # The (name of the) main information note that `notation_note` comes from. Returns `None` if `notation_note` does not come from such a note.
    """Return the name of the note from which the notation comes from.
            
    **Raises**

    - ValueError
        - If the notation note is not formatted correctly by starting
        with the notation with dollar signs `$`.
    """
    vault = notation_note.vault
    _, _, main_note_name, _, _ = parse_notation_note(notation_note, vault)
    if main_note_name is None:
        return None
    if as_note:
        return VaultNote(notation_note.vault, name=main_note_name)
    else:
        return main_note_name

# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 36
def notation_str_in_a_standard_information_note(
        info_note: VaultNote
        ) -> list[str]: # Each str is a LaTeX str, beginning and trailing dollar signs `$` (single or double) included.
    """
    Return the LaTeX str's with notations in a standard information note.

    A LaTeX str is deemed to be a notation if it is surrounded by double
    asterisks `**`
    """
    mf = MarkdownFile.from_vault_note(info_note)
    notations = []
    for part in mf.parts:
        indices = notation_asterisk_indices(part['line'])
        notations.extend([
            part['line'][start+2:end-2] for start, end in indices])
    return notations

# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 41
def notation_notes_linked_in_see_also_section(
        info_note: VaultNote,
        vault: PathLike, # Path to the vault directory.
        as_vault_notes: bool = True # If `True`, returns each notation note as a `VaultNote` object.  Otherwise, returns the name of each notation note. Defaults to `True`.
        ) -> Union[list[VaultNote], list[str]]: # Each entry corresponds to a notation note in the vault.
    """Return a list of notation notes listed in the
    `See Also` section of the standard information note.

    In the current implementation of this function, only 
    "notation notes" that actually exist are included in
    the returned list.
    """
    links = bulleted_links_of_type_in_section(
        info_note, vault, section="See Also",
        note_type=PersonalNoteTypeEnum.NOTATION_NOTE)
    note_names = [link.file_name for link in links]
    if as_vault_notes:
        return [VaultNote(vault, name=note_name) for note_name in note_names]
    else:
        return note_names


# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 50
def notations_and_main_notes(
        vault: PathLike, # Path to the vault directory.
        subdirectory: Optional[PathLike] = None, # Path to the subdirectory, relative to `vault`, to find the notation notes. Searches for all notation notes here and in subdirectories of this subdirectory. If `None`, then the `note parameter is used to determined the subdirectory. If `subdirectory` is the empty str, then all notation notes in the vault are searched. Defaults to `None`. 
        note: Optional[VaultNote] = None # A note in the vault. The directory that this note is in determines the `subdirectory` parameter if the argument passed to `subdirectory` is the blank str. This note can usually be an index note, e.g. `'_index_silverman'`. Defaults to `None`, in which case `subdirectory` must be specified.
        ) -> dict[str, Union[str, None]]: # A key is the unique name of a notation note in the vault and its corresponding value is the name of the main note of the notation note. Each main note may not actually exist, but each notation note definitely exists. If the notation note has no main note (i.e. has no links to other notes), then the value is `None`.
    """Return a `dict` with all of notation notes in a specified
    subdirectory of a vault and the names of the main notes of these
    notation notes.
    
    **Returns**
    - `dict`

    **Raises**

    - ValueError
        - If `subdirectory` and `note` are both `None`.
    """
    if note is None and subdirectory is None:
        raise ValueError(
            'Both the `subdirectory` and `note` parameters are None.')
    # vault = vault if vault is not None else ''
    if subdirectory is None:
        subdirectory = Path(note.rel_path).parent
    subdirectory_path = Path(vault) / subdirectory
    notes_in_subdirectory = subdirectory_path.glob(f'**/*.md') 
    relative_paths = [Path(note_path).relative_to(subdirectory_path)
                      for note_path in notes_in_subdirectory]
    vn_objects = [VaultNote(vault, rel_path=Path(subdirectory) / rel_path)
                  for rel_path in relative_paths]
    return {vn.name: main_of_notation(vn) for vn in vn_objects
            if note_is_of_type(vn, PersonalNoteTypeEnum.NOTATION_NOTE)}

# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 58
def notation_note_is_linked_in_see_also_section(
        notation_note: VaultNote,
        info_note: Optional[VaultNote] = None # The note in which to find the link to `notation_note`. Defaults to `None`, in which case the main note is determined to be the first linked note of `notation_note`.
        ) -> bool:
    """Return `True` if a notation note is linked in the `See Also`
    section of a standard information note. 
    """
    if not info_note:
        info_note = main_of_notation(notation_note, as_note=True)
    notes = notation_notes_linked_in_see_also_section(
        info_note, vault=notation_note.vault, as_vault_notes=False)
    return notation_note.name in notes


# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 65
def add_notation_note_to_see_also(
        notation_note: VaultNote,
        info_note: Optional[VaultNote] = None, # The note in which to link `notation_note`. Defaults to `None`, in which case the main note is determined to be the first linked note of `notation_note`.
        do_not_repeat: bool = True # If `True`, do not add a link to `notation_note` in if there is already a such a link.
        ) -> None:
    """Add a link to a notation note in the `See Also` section of
    a standard information note.

    **Raises**

    - NoteDoesNotExistError
        - If the information note to link to does not exist.
    
    """
    if not info_note:
        info_note = main_of_notation(notation_note, as_note=True)
    if not info_note.exists():
        raise NoteDoesNotExistError
    if do_not_repeat and notation_note_is_linked_in_see_also_section(
            notation_note, info_note):
        return
    mf = MarkdownFile.from_vault_note(info_note)
    link = ObsidianLink(False, notation_note.name, 0, 0)
    mf.add_line_in_section(
        'See Also', {'type': MarkdownLineEnum.UNORDERED_LIST,
                     'line': f'- {str(link)}'})
    mf.write(info_note)



# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 78
def add_missing_notation_links_to_information_notes(
        vault: PathLike, # Path to the vault directory.
        subdirectory: Optional[PathLike] = None, # Path to the subdirectory, relative to `vault`, to find the notation notes and their main notes. Searches for all notation notes here and in subdirectories of this subdirectory. If `None`, then the `note` parameter is used to determine `subdirectory`. Defaults to `None`. 
        note: Optional[VaultNote] = None # A note in the vault. The directory that this note is in determines the `subdirectory` parameter if it is `None`.  Defaults to `None`, in which case `subdirectory` must be specified.
        ) -> None:
    # TODO: deal with possibility that note does not exist.
    """For each notation note in a specified subdirectory, Add links
    to notation notes in their main information notes if the notation
    links are not already present.
    
    **Raises**

    - ValueError
        - If `subdirectory` and `note` are both `None`.
    """
    mains_dict = notations_and_main_notes(vault, subdirectory, note)
    to_check = {key: value for key, value in mains_dict.items()
                if value is not None}
    for notation, main in to_check.items():
        if not main:
            continue
        notation_note = VaultNote(vault, name=notation)
        try:
            main_note = VaultNote(vault, name=main)  # TODO add the subdirectory parameter here appropriately. See Also `notations_and_main_note` 
            add_notation_note_to_see_also(notation_note, main_note)
        except NoteDoesNotExistError:
            continue

# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 82
def notations_to_add_in_index(
        vault: PathLike, # Path to the vault directory.
        notation_index_note = VaultNote, # The notation index note in the vault where the notations should be added to.
        subdirectory: Optional[PathLike] = None , # Path to the subdirectory, relative to `vault`, to find the notation notes. Searches for all notation notes here and in subdirectories of this subdirectory. If `None`, then the `note parameter is used to determined the subdirectory. If `subdirectory` is the empty str, then all notation notes in the vault are searched. Defaults to `None`. 
        note: Optional[VaultNote] = None # The directory that this note is in determines the argument to `subdirectory` parameter if it is `None`. Defaults to `None`, in which case `subdirectory` must be specified.
        ) -> list[tuple[str, ObsidianLink]]: # Each tuple in the list consists of the notation str of the notation note (including surrounding dollar signs `$`) and the (nonembedded) ObsidianLink object for a link to the notation note.
    """Returns notations and links of notation notes to that ought to be
    added in the corresponding notation index, i.e. are in the reference
    folder but not linked by the notation index note.

    If a notation note is not properly formatted, e.g. does not have a
    notation, then the notation and link for the notation note will not
    be included.
    
    **Raises**
    - ValueError
        - If `subdirectory` and `note` are both `None`.

    """
    vault = vault if vault is not None else ''
    mains_dict = notations_and_main_notes(vault, subdirectory, note)
    mf_object = MarkdownFile.from_file(notation_index_note.path())
    mf_text = str(mf_object)
    notations_and_links = []
    for notation, _ in mains_dict.items():
        link_object = ObsidianLink(
            is_embedded=True, file_name=notation, anchor=0, custom_text=0,
            link_type=LinkType.WIKILINK)
        link = link_object.to_string()
        try:
            notation_str = notation_in_note(notation, vault)
        except AttributeError:  # When a notation note is incomplete.
            continue  # TODO: print a warning
        if not link in mf_text:
            notations_and_links.append((notation_str, link_object))
    return notations_and_links



# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 85
def index_notation_note_formatted_entry(
        notation_str: str, # The str of the notation, including the surrounding dollar signs `$`.
        link: ObsidianLink # The embedded link to the notation note. 
        ) -> str:
    """Return a str formatted for an index notation note entry.

    It is recommended to pass the outputs of
    `notations_to_add_in_index` to this function.
    """
    return f'### {notation_str}\n- {link.to_string()}'

# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 89
def make_a_notation_note(
        main_note: VaultNote, # The note from which the notation originates.
        vault: PathLike,
        notation: str, # The notation typed in latex. May or may not be surrounded by dollar signs
        description: str, # The rest of the text describing notation.
        notation_note_name: str, # The name of the new notation note to be created.
        destination: Optional[PathLike] = None, # The directory to create the new notation note in.  If `None`, then creates the new notation note in the same place as the note specified by `note_name`
        overwrite: bool = False, # If `True`, overwrite file of the same path as the new notation file to be written, if such a file exists.  Otherwise, does nothing. Even if a link to the old notation note exists in `main_note`, a new link will still be added.  Defaults to `False`.
        add_to_main: bool = True # If `True`, adds a link to the notation note in the `See Also` section of the main note.
        ) -> Union[VaultNote, None]: # The newly created notation note. If no note is created, then returns `None`.
    """Make a new notation note, optionally add a link to it in the
    `See Also` section of its main note, returns it.

    The notation note is created in the same directory as the main note.
    The meta of the notation note has a `latex_in_original` section which
    lists the contents of the latex string in the main note from which the
    notation note comes from. This is so that the
    `make_notation_notes_from_double_asts` method can distinguish between
    notations for which a note has been created and for which a note has
    not been created.
    """
    if destination is None:
        destination = main_note.directory(relative=True)
    notation_note = VaultNote(
        vault, rel_path=destination / f'{notation_note_name}.md')
    if not overwrite and notation_note.exists():
        return
    if not notation_note.exists():
        notation_note.create()
    to_print = _full_notation_string(main_note, notation, description)
    # TODO: change this to use VaultNote method
    with open(notation_note.path(), 'w+', encoding='utf8') as notation_file:
        notation_file.write(to_print)
    if add_to_main:
        add_notation_note_to_see_also(notation_note, main_note)
    return notation_note
    

def _full_notation_string(
        main_note: VaultNote, notation: str, description: str) -> str:
    """The full "statement" of a notation.
    
    Says something like "<notation> denotes <description of notation>", e.g.
    "$\dim V$ denotes the dimension of the vector space $V$".
    
    **Parameters**
    - notation - str
        - Notation written in LaTeX.
    - description - str
        - The full description of the notation.
        
    **Returns**
    - str
    """
    raw_notation = f'{_raw_notation(notation)}'
    denote_link = ObsidianLink(False, main_note.name, 0, 'denotes')
    meta_notation = raw_notation.replace('\\', '\\\\')
    return (f'---\ndetect_regex: []\n'
            f'latex_in_original: ["{meta_notation}"]'
            f'\n---\n${raw_notation}$ {str(denote_link)} {description}')


def _raw_notation(notation: str):
    """
    """
    notation = notation.strip()
    notation = notation.strip('$')
    notation = notation.strip()
    return notation


# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 103
def make_notation_notes_from_double_asts(
        main_note: VaultNote, # The standard information note from which the notations are marked with double asterisks
        vault: PathLike, # The name of the reference; the notation note's name will start with `{reference_name}_notation_`.
        reference_name: str,
        destination: Optional[PathLike] = None, # The directory to create the new notation notes in.  If `None`, then creates the new notation note in the same place as the note specified by `note_name`
        overwrite: bool = False, # If `True`, overwrite file of the same path as the new notation file to be written, if such a file exists.  Otherwise, does nothing. Defaults to `False`.
        add_to_main: bool = True # If `True`, adds links to the notation note in the `See Also` section of the main note.
        ) -> list[VaultNote]: # The list of VaultNotes that are newly created/modified.
    """Make notation notes based on double asterisks surrounding LaTeX text in
    a standard information note.

    Notations are deemed to be completely LaTeX text in info notes that
    are surrounded by double asterisks. In basicality, if such a LaTeX
    text (without surrounding dollars signs `$` or `$$`) is listed in
    the `latex_in_original` metadata section of some notation note in the same
    directory as the info note whose main note is the info note in question,
    then a new notation note for that LaTeX text 
    is not created. However, if there are multiple instances of the same
    LaTeX text, then some notation notes may be created so that the number
    of times the LaTeX text appears in the info note is the no more than
    the number of times the LaTeX text appears in `latex_in_original` metadata
    sections of notation notes (in the same directory as the info note whose
    main note is the info note).

    For example, if there is an info note with notations `A`, `A`, `'A'`,
    `'A'`, and `B` and if there is a single notation note in the same
    directory as the info note with two `'A'` and `'A'` entries in its
    `latex_in_original` metadata section, then three notation notes will be
    created: two with `'A'` listed in their `latex_in_original` sections, and
    one with `'B'` listed in its `latex_in_original` section.

    **Raises**

    - Warning
        - If there are notation notes whose main note is determined to
        be to `main_note` and whose notations "excessively cover" those
        in `main_note`, i.e. the notation notes have more notations than
        `main_note` introduces. The main note and the excessive
        notations are printed; the notations are printed instead of the 
        notation notes because the same notation may span either multiple
        or single notation notes.
    """
    # Find notations
    notations = notation_str_in_a_standard_information_note(main_note)
    notations = [_raw_notation(notation) for notation in notations]
    # Get only the notations not already made into notes based on
    # latex_in_original
    all_latex_in_original = _latex_in_original_from_notat_notes_to_main_note(
        vault, main_note)
    notations_to_create = Multiset(notations).difference(all_latex_in_original)
    notations_to_create = list(notations_to_create)
    # Alert of existing notations that should not be there
    excess_notations = all_latex_in_original.difference(Multiset(notations))
    excess_notations = list(excess_notations)
    if excess_notations:
        warnings.warn(
            f"The following note has the following excess notations: "
            f"{main_note.name}, {', '.join(excess_notations)}")
    # Make notations
    return _make_new_notes_from_sifted_double_asts(
        main_note, vault, reference_name, notations_to_create,
        destination, overwrite, add_to_main)
    

def _latex_in_original_in_notat(
        notation_note: VaultNote
        ) -> list[str]:
    """Return the `latex_in_original` metadata section of the notation note.
    
    If the `latex_in_original` metadata section does not exist, then returns
    the list consisting of the notation in the notation note.
    """
    # TODO: test in the case that `latex_in_original` section does not exist
    mf = MarkdownFile.from_vault_note(notation_note)
    metadata = mf.metadata()
    if metadata is not None:
        return metadata.get('latex_in_original',
                            [notation_in_note(notation_note).strip('$')])
    else:
        return [notation_in_note(notation_note)]

    
def _latex_in_original_from_notat_notes_to_main_note(
        vault: PathLike,
        main_note: VaultNote # The info note
        ) -> Multiset:
    """Return a Multiset enumerating the entries of `latex_in_original`
    in the notation notes in the same directory as an info note
    """
    notation_notes_in_folder = notations_and_main_notes(vault, note=main_note)
    notation_notes_of_main_note = [
        VaultNote(vault, name=notation_note) for notation_note, info_note
        in notation_notes_in_folder.items()
        if main_note.name == info_note]

    all_latex_in_original = Multiset()
    for notat_note in notation_notes_of_main_note:
        all_latex_in_original.update(_latex_in_original_in_notat(notat_note))
    return all_latex_in_original


MAX_NOTE_NAME_LENGTH = 80
def _make_new_notes_from_sifted_double_asts(
        main_note: VaultNote, vault: PathLike, reference_name: str,
        notations: list[str], destination: Optional[PathLike],
        overwrite: bool, add_to_main: bool) -> list[VaultNote]:
    """
    Actually makes the notation notes found from the double asterisked LaTeX
    str's
    """
    # TODO: test that note names aren't too long.
    new_notes = []
    for notation in reversed(notations):
        notation_note_name = f'{reference_name}_notation_'\
            f'{latex_to_path_accepted_string(notation)}'
        if len(notation_note_name) > MAX_NOTE_NAME_LENGTH:
            notation_note_name = notation_note_name[:MAX_NOTE_NAME_LENGTH]
        notation_note_name = VaultNote.unique_name(
            notation_note_name, vault)
        new_note = make_a_notation_note(
            main_note, vault, notation, '', notation_note_name,
            destination, overwrite, add_to_main)
        if new_note:
            new_notes.append(new_note)
    return new_notes
    



# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 122
SPECIAL_CHARACTERS = ['.', '+', '*', '?', '^', '$', '(', ')',
                      '[', ']', '{', '}', '|', '\\']
replaceable_groups = [['mathrm', 'operatorname', 'rm', 'text'],
                      ['mathbf', 'bf'],
                      ['mathit', 'it']]


def _build_replacables_from_groups(
        replaceable_groups: list[list[str]]) -> dict[str, set[str]]:
    total_dict = {}
    for listy in replaceable_groups:
        set_for_group = set(listy)
        for macro in listy:
            total_dict[macro] = set_for_group
    return total_dict


REPLACEABLES = _build_replacables_from_groups(replaceable_groups)
    

def regex_from_latex(
        latex: str, replaceables: dict[str, set[str]] = REPLACEABLES,
        special_characters: list[str] = SPECIAL_CHARACTERS) -> str:
    """Returns regex to match latex math mode string which is essentially
    equivalent to a specified latex math mode string.
    
    The outputs of this function may not work correctly.
    The regex pattern does not have to fully match equivalent string.
    
    **Parameters**

    - latex - str
        - The latex math mode string. Does not include math mode delimiters
        such as `$`, `$$`, `\[ \]` (although the characters `'\['` and `'\]'`
        can still be part of the string, e.g. for optional arguments of a
        macro/operator). Can include "placeholders" `r'\1'`, `r'\2'`, `r'\3'`,
        etc. to indicate substitutable/generics; the placeholders can be
        substituted with any string.
    - replaceables - dict[str, set[str]]
        - latex strings/commands which are considered "interreplacable"
    - special_characters - list[str]
        - characters to add a backslash `'\'` in front of for regex.
        Defaults to a list consisting of special characters in regex.
    """
    if not replaceables:
        replaceables = {}
    w = LatexWalker(latex)
    nodelist, _, _ = w.get_latex_nodes(pos=0)
    regex_parts = []
    # print(nodelist)
    for node in nodelist:
        _look_into_node(node, regex_parts,
                        replaceables, special_characters)
    regex_parts.append('(?:[ \\{\\}]*)')
    return ''.join(regex_parts)
    
def _look_into_node(
        node: LatexNode, regex_parts: list[str],
        replaceables: dict[str, set[str]],
        special_characters: list[str]) -> None:
    """Appends to `regex_parts`"""
    # hasattr(node, 'nodeargd')
    # print(node)
    if isinstance(node, LatexMacroNode):
        macroname = node.macroname
        if _macro_is_actually_placeholder(macroname):
            regex_parts.append('(?:.*)')
        else:
            if macroname in replaceables:
                replaceable_macros = replaceables[macroname]
            else:
                replaceable_macros = [macroname]
            options_str = '|'.join(replaceable_macros)
            options_str = f'(?:{options_str})'
            regex_parts.append(fr'(?: *?)\\{options_str}(?: *?)')
        for node in node.nodeargd.argnlist:
            _look_into_node(node, regex_parts,
                            replaceables, special_characters)
    elif isinstance(node, LatexGroupNode):
        # print('\nGroup Node')
        # print(node)
        # print(node.nodelist)
        delimiters = node.delimiters
        regex_parts.append(f'\\{delimiters[0]}(?: *?)')
        for node in node.nodelist:
            _look_into_node(node, regex_parts,
                            replaceables, special_characters)
        regex_parts.append(f'(?: *?)\\{delimiters[1]}')
    elif isinstance(node, LatexCharsNode):
        # print('\nChars Node')
        # print(node)
        # print(node.chars)
        chars = node.chars.strip()
        chars = list(chars)
        chars = [f'\\{char}' if char in special_characters else char
                 for char in chars]
        # print(chars)
        chars.insert(0, '')  # add the misc spaces/brackets front and back
        chars.append('')
        regex_optional_spaces_and_brackets = '(?:[ \\{\\}]*?)'.join(chars)
        regex_parts.append(regex_optional_spaces_and_brackets)
        
def _macro_is_actually_placeholder(macro: str) -> bool:
    return macro.isnumeric()

# %% ../../../../nbs/20_markdown.obsidian.personal.notation.ipynb 126
def regex_from_notation_note(vault: PathLike, note: VaultNote) -> str:
    """Returns a regex str to detect the notation of the notation note.
    
    The regex detection strings should be in a list labeled `detect_regex` in
    the yaml frontmatter. If multiple strings are in the list, then the regex
    will detect latex math mode strings roughly corresponding to any of them.
    If multiple strings are in the list, then they must be ordered 
    "by priority", with the higher priority regexes coming first. It is good
    to have these string in quotes `""` to make sure that yaml can load them
    safely. When doing so, make sure to escape characters, e.g. backslash
    should be typed as `\\`, etc.
    
    The strings in `detect_regex` can include placeholders, cf.
    ``regex_from_latex``.
    
    **Parameters**
    - vault - PathLike
    - note - VaultNote
    
    **Returns**
    - str
        - Of the regex used to detect the notation. The regex does not need to
        fully match instances of the notation.
    """
    assert note_is_of_type(note, PersonalNoteTypeEnum.NOTATION_NOTE)
    mf = MarkdownFile.from_vault_note(note)
    metadata = mf.metadata()
    if metadata and 'detect_regex' in metadata:
        detects = metadata['detect_regex']
        regexes = [regex_from_latex(detect) for detect in detects]
        return '|'.join(regexes)
    else:
        notation = notation_in_note(note, vault)
        return regex_from_latex(notation[1:-1])  # Get rid of `'$'`.
