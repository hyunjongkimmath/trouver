# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../../nbs/21_markdown.obsidian.personal.information_notes.ipynb.

# %% auto 0
__all__ = ['bulleted_links_of_type_in_section', 'links_to_common_terms_notes_in_see_also_section', 'main_content',
           'reference_notes_in_references_section_of_information_note', 'reference_of_information_note',
           'citation_location_string', 'fill_info_note_with_template', 'link_info_notes_to_index',
           'create_info_notes_and_link_to_index', 'create_generic_info_notes_and_link_to_index',
           'index_note_of_a_directory', 'index_note_of_note']

# %% ../../../../nbs/21_markdown.obsidian.personal.information_notes.ipynb 2
import glob
import os
from os import PathLike
from pathlib import Path
import re
from typing import Optional, Union, Tuple

from ....helper import path_name_no_ext
from trouver.markdown.markdown.file import (
    MarkdownFile, MarkdownLineEnum
)
from trouver.markdown.obsidian.footnotes import (
    find_footnote_descriptions_in_markdown_text
)
from trouver.markdown.obsidian.links import (
    ObsidianLink, LinkFormatError, LinkType, links_from_text
)
from trouver.markdown.obsidian.personal.note_type import (
    note_is_of_type, PersonalNoteTypeEnum, assert_note_is_of_type
)
from .notes import notes_linked_in_note
from trouver.markdown.obsidian.vault import (
    note_path_by_name, VaultNote, NoteDoesNotExistError
)



# %% ../../../../nbs/21_markdown.obsidian.personal.information_notes.ipynb 5
# TODO: deal with the possibility that the link points to a note that does not exist.
# TODO: reformat
def bulleted_links_of_type_in_section(
        info_note: VaultNote, vault: PathLike, section: str,
        note_type: Optional[PersonalNoteTypeEnum] = None)\
            -> list[ObsidianLink]:
    """Returns a list of ``ObsidianLink``s of notes of the given type 
    listed in the specified section of the standard information note.
    
    **Parameters**
    - `info_note` - VaultNote
        - Name of the information note.
    - `vault` - PathLike
        - Path to the vault directory.
    - `section` - str
        - Title of the section
    - `note_type` - ``trove.markdown.obsidian.personal.note_type.PersonalNoteTypeEnum`` or `None`
        - The type of the notes to include in the list. If `None`, then
        all note types are included. Defaults to `None`.
        
    **Returns**
    - list of ``markdown.obsidian.links.ObsidianLink`` objects
        - Each entry is the name of a notation note in the vault.
        
    **Raises**
    - AssertionError
        - If the note is not a standard information note
    """ 
    # TODO: delete these lines
    # info_path = note_path_by_name(info_note, vault)
    # info_note = VaultNote(vault, rel_path=info_path)
    assert_note_is_of_type(info_note, PersonalNoteTypeEnum.STANDARD_INFORMATION_NOTE)
    parsed = MarkdownFile.from_vault_note(info_note)
    # parsed = MarkdownFile.from_file(Path(vault) / info_path)
    heading_index = parsed.get_line_number_of_heading(title=section)
    
    list_of_note_names_of_type = []
    for part in parsed.parts[heading_index+1:]:
        if part['type'] == MarkdownLineEnum.HEADING:
            break
        line_text = part['line']
        link_text = line_text.strip('- \n\t\r')
        try:
            link_object = ObsidianLink.from_text(link_text)
        except LinkFormatError as e:
            continue
        note_name = link_object.file_name
        linked_note = VaultNote(vault, name=note_name)
        if note_is_of_type(linked_note, note_type):
            list_of_note_names_of_type.append(link_object)
        # if note_is_of_type(note_type, note_path_by_name(note_name, vault),
        #                    vault):
        #     list_of_note_names_of_type.append(link_object)
    return list_of_note_names_of_type

# %% ../../../../nbs/21_markdown.obsidian.personal.information_notes.ipynb 8
def links_to_common_terms_notes_in_see_also_section(
        info_note: VaultNote, vault: PathLike) -> list[str]:
    """Returns a list of names of common terms notes listed in the
    `See Also` section of the standard information note.
    
    **Parameters**
    - `info_note` - VaultNote
    - `vault` - Pathlike
        - Path to the vault directory.
        
    **Returns**
    - list[str]
        - Each entry is the name of a notation note in the vault.
    """
    return bulleted_links_of_type_in_section(
        info_note, vault, section="See Also",
        note_type=PersonalNoteTypeEnum.COMMON_TERMS_NOTE)

# %% ../../../../nbs/21_markdown.obsidian.personal.information_notes.ipynb 11
# TODO: reformat
def main_content(note: VaultNote) -> str:
    """The main content of the standard information note.
    
    This is the text not in the yaml frontmatter and not the `'#See Aslo'`
    section and below.
    
    **Parameters**
    - note: VaultNote
        - A standard information note.
        
    **Returns**
    - str
    """
    mf = MarkdownFile.from_vault_note(note)
    index = mf.get_line_number_of_heading('See Also')
    main_parts = mf.parts[:index]
    main_parts = [part for part in main_parts if part['type'] != MarkdownLineEnum.META]
    new_mf = MarkdownFile(main_parts)
    return(str(new_mf))
    

# %% ../../../../nbs/21_markdown.obsidian.personal.information_notes.ipynb 14
def reference_notes_in_references_section_of_information_note(note: VaultNote) -> list:
    """Returns a list of ``ObsidianLink`` objects corresponding to
    reference notes in the "References" section of the information note.
    
    **Parameters**
    - `note` - VaultNote
        - A standard information note
    
    **Returns**
    - list of ``ObsidianLink``
    """
    md_file = MarkdownFile.from_vault_note(note)
    # TODO incomplete
    line = md_file.get_line_number_of_heading(title="References")
    line += 1
    reference_links = []
    while md_file.parts[line]['type'] != MarkdownLineEnum.HEADING:
        reference_links += links_from_text(md_file.parts[line]['line'])
        line += 1
    return reference_links


def reference_of_information_note(note: VaultNote) -> VaultNote:
    """Returns the reference note that the information note probably comes from.
    
    TODO
    
    **Parameters**
    - `note` - VaultNote
        - A standard information note
        
    **Returns**
    - VaultNote
    """
    reference_links = reference_notes_in_references_section_of_information_note(note)
    md_file = MarkdownFile.from_vault_note(note)
    first_footnote = find_footnote_descriptions_in_markdown_text(str(md_file))[0]
    
    
    
    

# %% ../../../../nbs/21_markdown.obsidian.personal.information_notes.ipynb 19
def citation_location_string(
        citation_location: tuple[str, int]
        ):
    """Formats a pair specifying the Numbering label and page
    
    **Parameters**
    - `citation_location` - 2-tuple or empty tuple
        - Consists of a label str and a page number indicating where
        in the note's reference text the note's information originates from,
        e.g. the label might be the str 'Theorem 1.2.3' and the page number
        might be the int 85.
    """
    if citation_location:
        if citation_location[0]:
            return f'{citation_location[0]}, Page {citation_location[1]}'
        else:
            return f'Page {citation_location[1]}'
    else:
        return ''

# %% ../../../../nbs/21_markdown.obsidian.personal.information_notes.ipynb 20
def fill_info_note_with_template(
        vn: VaultNote,
        template: VaultNote, 
        citation_location: tuple[str, int] = (),
        content: str = '',
        tags_to_add: Union[str, list[str], tuple[str], None] = None
        ) -> None:
    """Fills in the note with a template with optionally tags.

    Current implementation adds content to line 5 of the note.

    **Parameters**
    - `vn` - ``VaultNote``
    - `template` - ``VaultNote``
    - `citation_location` - 2-tuple or empty tuple
        - Consists of a label str and a page number indicating where
        in the note's reference text the note's information originates from,
        e.g. the label might be the str 'Theorem 1.2.3' and the page number
        might be the int 85.
    - `content` - str
        - Content to add to the note. Defaults to the empty str.
    - `tags_to_add` - str or list of str or tuple of str or `None`
        - Each str is just the name of the tag without the leading hashtag.
        Defaults to `None`, in which case no tags are added.
    
    """
    mf = MarkdownFile.from_vault_note(template)
    if tags_to_add and isinstance(tags_to_add, str):
        tags_to_add = [tags_to_add]
    mf.add_tags(tags_to_add)
    # if tags_to_add:
    #     tags_to_add = [to_tag_str(tag) for tag in tags_to_add]
    #     full_tag_line = ' '.join(tags_to_add)
    #     tag_section_index = mf.get_line_number_of_heading(title="Tags")
    #     mf.insert_line(tag_section_index+1, 
    #                    {'line': f'{full_tag_line}\n', 'type': MarkdownLineEnum.DEFAULT})
    if citation_location:
        footnote = mf.pop_line()
        footnote['line'] += citation_location_string(citation_location)
        mf.add_line_to_end(footnote)
    if content:
        line_num = mf.get_line_number_of_heading("See Also")
        mf.insert_line(line_num-1, {'line': content, 'type': MarkdownLineEnum.DEFAULT})
    mf.write(vn)

# %% ../../../../nbs/21_markdown.obsidian.personal.information_notes.ipynb 21
# TODO: reformat
def link_info_notes_to_index(
        info_notes, index_note: VaultNote, citation_locations: tuple=(),
        insert_blank_line=False):
    """Links notes to an index_note.
    
    For now, just adds to the bottom of the thing
    # TODO Make it possible to add in specific sections
    
    **Parameters**
    - info_notes - ``VaultNote`` or list of ``VaultNote``
    - index_note - ``VaultNote``
    - insert_blank_line - bool
        - If `True`, then insert a blank line at the end of the
        index note before adding the links to the info notes.
    """
    if isinstance(info_notes, VaultNote):
        info_notes = [info_notes]
    
    index_mf = MarkdownFile.from_vault_note(index_note)
    if insert_blank_line:
        index_mf.add_blank_line_to_end()
    for vn, citation_location in zip(info_notes, citation_locations):
        vn_mf = MarkdownFile.from_vault_note(vn)
        link = ObsidianLink(is_embedded=False, file_name=vn.name,
                            anchor=0, custom_text=0, link_type=LinkType.WIKILINK)    
        index_mf.add_line_to_end(
            {'line': f'- [ ] {link.to_string()}, {citation_location_string(citation_location)}',
             'type': MarkdownLineEnum.UNORDERED_LIST})
    index_mf.write(index_note)

# %% ../../../../nbs/21_markdown.obsidian.personal.information_notes.ipynb 22
# TODO: reformat
def create_info_notes_and_link_to_index(
        to_create: list[VaultNote],
        template: VaultNote,
        index_note: VaultNote,
        citation_locations: list = [],
        content_to_add: list = [] ,
        tags_to_add: Union[str, list[str], tuple[str], None] = None):
    """Creates multiple notes, fills them in with a template,
    and links them to the appropriate index note.
    
    Current implementation adds content from `content_to_add` to line 5
    of the VaultNotes.
    
    **Parameters**
    - `to_create` - list of ``VaultNote``.
    - `template` - ``VaultNote``
    - `index_note` - ``VaultNote``
    - `citation_locations` - list of 2-tuples or empty tuples 
        - Each tuple consists of a label str and a page number indicating where
        in the note's reference text the note's information originates from,
        e.g. the label might be the str 'Theorem 1.2.3' and the page number
        might be the int 85. This list must be of the same length as `to_create`.
    - `content_to_add` - list of str
        - Each str is the content to be added for each note in `to_create`. 
        Defaults to the empty list, in which case no content is added.
    - `tags_to_add` - str or list of str or tuple of str or `None`
        - Each str is just the name of the tag without the leading hashtag.
        Defaults to `None`, in which case no tags are added.
    """
    if not citation_locations:
        citation_locations = [() for _ in to_create]
    if not content_to_add:
        content_to_add = ['' for _ in to_create]
    assert len(citation_locations) == len(to_create) and len(content_to_add) == len(to_create)
    for vn, citation_location, content in zip(to_create, citation_locations, content_to_add):
        Path(vn.path()).touch()
        fill_info_note_with_template(vn, template, citation_location, content, tags_to_add)
    link_info_notes_to_index(to_create, index_note, citation_locations, insert_blank_line=True)

# %% ../../../../nbs/21_markdown.obsidian.personal.information_notes.ipynb 23
# TODO: reformat
def create_generic_info_notes_and_link_to_index(
        reference:str, count:int, vault, subdirectory, 
        template: VaultNote, index_note: VaultNote, tags_to_add=None):
    """Creates generically named notes, fills them in with a template,
    and links them to the appropriate index note.
    
    The note will be named in the form `f'{reference}_{number}'`, where `number`
    starts with 0.
    
    **Parameters**
    - `reference` - str
        - The name of the reference. This will be part of the generic
        note names.
    - `count` - int
        - The number of generic info notes to create.
    - `vault` - Pathlike
    - `subdirectory` - Pathlike
        - The subdirectory in `vault` to create the notes in.
    - `template` - VaultNote
    - `index_note` - VaultNote
    - tags_to_add - str or list of str or tuple of str or `None`
        - Each str is just the name of the tag without the leading hashtag.
        Defaults to `None`, in which case no tags are added.
    """
    # Determine which numbers are used for existing notes and then
    # determine which numbers to use for new notes.
    existing_paths = Path(vault).glob(f'**/{reference}_[0-9]*.md')
    path_names = [path_name_no_ext(path) for path in existing_paths]
    path_names = [path_name for path_name in path_names if re.match(f'{reference}_[0-9]*$', path_name)]
    
    existing_numbers = {int(path_name[len(reference)+1:]) for path_name in path_names}
    total_numbers = len(existing_numbers) + count
    nonexisting = list(set(range(total_numbers)) - existing_numbers)
    new_to_make = nonexisting[:count]
    to_create = [VaultNote(vault, rel_path=Path(subdirectory) / f'{reference}_{number}.md')
                 for number in new_to_make]
    create_info_notes_and_link_to_index(to_create, template, index_note, 
                                        content_to_add = [], tags_to_add=tags_to_add)
        
    

# %% ../../../../nbs/21_markdown.obsidian.personal.information_notes.ipynb 25
def index_note_of_a_directory(
        vault: PathLike,
        directory: PathLike # Relative to `vault`
        ) -> Union[VaultNote, None]: # Either the index note in the directory if it exists or `None` 
    """Return the index note in a directory in an `Obsidian.md` vault, if it exists.

    Assumes that the directory has at most one index note.

    **Raises**

    - RuntimeError
        - If more than one index note exists in the directory.    
    """
    full_directory = Path(vault) / directory
    glob_results = glob.glob(
        str(full_directory /  "_index*.md"), recursive=False)
    # TODO
    if len(glob_results) > 1:
        raise RuntimeError(
            "Expected there to exist at most one index note in the"
            f" directory, but there are more than one:\n{glob_results}")
    elif len(glob_results) == 1:
        path = glob_results[0]
        rel_path = os.path.relpath(path, vault)
        return VaultNote(vault, rel_path)
    else:
        return None

# %% ../../../../nbs/21_markdown.obsidian.personal.information_notes.ipynb 29
def index_note_of_note(
        note: VaultNote # An information note or an index note
        ) -> Union[VaultNote, None]: # The index note which indexes `note`. If no such index note exists (in either the same directory as or the immediate parent directory of the note), then `None` is returned. In particular, `None` is returned if `note` is the root index note of the vault.
    """Return the index note indexing the specified note.

    `note` is assumed to either be an information note
    or itself an index note.

    Assumes that a note in indexed in at most one
    index note and that this index note is either in the same directory
    as the note or in the immediate parent directory of
    the note.

    **Raises**

    - UserWarning
        - If an index note that is supposed to index `note` 
        exists, but does not actually index `note`.
    
    """
    # If `note` is the top level index note, then return `None`
    note_is_index_note = note_is_of_type(
        note, PersonalNoteTypeEnum(PersonalNoteTypeEnum.INDEX_NOTE))
    if note_is_index_note and note.directory(relative=True) == Path('.'):
        return None

    index_note = _index_note_in_same_directory(note, note_is_index_note)
    index_note = _index_note_in_parent_directory(note, index_note)

    if _note_is_not_linked_in_index_note(index_note, note):
        UserWarning(
            f'The index note is expected to index the note, but this is'
            f' not actually the case:\n'
            f' index_note: {index_note.name}\nnote: {note.name}')

    return index_note


def _index_note_in_same_directory(
        note: VaultNote,
        note_is_index_note: bool
        ) -> Union[VaultNote, None]:
    """
    If the index note of `note` should be in the same directory as `note`,
    then return that index note assuming it exists; otherwise, return `None`.

    This is a helper function of `index_note_of_note`
    """
    # Determine if the index note is in the same directory as `note`
    search_index_note_in_same_directory = index_note_of_a_directory(
        note.vault, note.directory(relative=True))
    if not (note_is_index_note
            or search_index_note_in_same_directory is None):
        index_note = search_index_note_in_same_directory
    else:
        index_note = None
    return index_note


def _index_note_in_parent_directory(
        note: VaultNote,
        index_note: Union[VaultNote, None], # Output of `_index_note_in_same_directory`
        ) -> Union[VaultNote, None]:
    """
    If the index note of `note` should be in the immediate parent directory as
    `note`, then return that index note assuming it exists; otherwise, return
    `None`.

    This is a helper function of `index_note_of_note`
    """
    if index_note is not None:
        return index_note
    # Determine if the index note is in the parent directory of `note`
    search_index_note_in_parent_directory = index_note_of_a_directory(
        note.vault, note.directory(relative=True).parent)
    if (index_note is None
            and search_index_note_in_parent_directory is not None):
        index_note = search_index_note_in_parent_directory
    else:
        index_note = None
    return index_note



def _note_is_not_linked_in_index_note(
        index_note: Union[VaultNote, None],
        note: VaultNote) -> bool:
    """Return `True` if `index_note` is not `None` and `note` is not
    linked in `index_note`.
    
    This is a helper function of `index_note_of_note`.
    """
    if index_note is None:
        return False
    indexed_notes = notes_linked_in_note(index_note, as_dict=False)
    indexed_note_names = [vn.name for vn in indexed_notes]
    return note.name not in indexed_note_names
