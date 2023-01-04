# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb.

# %% auto 0
__all__ = ['index_note_for_reference', 'reference_directory', 'copy_obsidian_vault_configs', 'get_obsidian_vault_plugin_configs',
           'modify_obsidian_vault_plugin_configs', 'copy_obsidian_vault_configs_with_nice_modifications',
           'setup_folder_for_new_reference']

# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 2
import glob
import json
import os
from os import PathLike
from pathlib import Path
import re
import shutil
from typing import Union, Optional
import warnings

from trouver.helper import (
    path_name_no_ext, alphabet_to_alphabet_group
)
from trouver.markdown.markdown.file import (
    MarkdownFile, MarkdownLineEnum
)
from trouver.markdown.markdown.heading import (
    heading_title
)
from trouver.markdown.obsidian.links import (
    ObsidianLink, LinkType, links_from_text
)
from .authors import find_author_file
from trouver.markdown.obsidian.personal.index_notes import ( 
    convert_title_to_folder_name
)
from trouver.markdown.obsidian.personal.notes import (
    notes_linked_in_note
)
from trouver.markdown.obsidian.personal.note_type import (
    type_of_note, PersonalNoteTypeEnum
)
from trouver.markdown.obsidian.vault import(
    VaultNote, all_note_paths_by_name, note_path_by_name,
    NoteDoesNotExistError, NoteNotUniqueError
)

# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 5
def index_note_for_reference(
        vault: PathLike, # The vault in which the reference folder resides.
        reference: Union[str, Path] # - The reference. Is either - a str, in which case the reference folder will be the folder containing the (unique) note of the name `_index_{reference}.md`, - or a `Path` object (not just a pathlike!) relative to `vault`, in which case the path will be the path to the reference folder. 
        ) -> VaultNote:
    """
    Returns the index note of the specified reference in the vault.
    
    Assumes that the reference folder has an index note named
    `_index_{reference_name}.md` and this note is the unique note in the vault
    with this filename.
    
    **Raises**

    - TypeError
        - If `reference` is not a str or PathLike.
    - NoteDoesNotExistError
        - If a note of the name `_index_{reference_name}.md` does not exist
        in the vault.
    """
    if (not isinstance(reference, str)
            and not isinstance(reference, PathLike)):
        raise TypeError(
            "Expected `reference` to be a str or a PathLike, but got"
            f" {type(reference)} instead.")
    if isinstance(reference, str):
        reference_name = reference
        index_note = VaultNote(vault, name=f'_index_{reference_name}')
    elif isinstance(reference, PathLike):
        reference_name = Path(reference).name
        index_note = VaultNote(
            vault, rel_path=Path(reference) / f'_index_{reference_name}.md')
    return index_note



# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 8
def reference_directory(
        vault: PathLike, # The vault in which the reference folder resides.
        reference: Union[str, Path] # - The reference. Is either - a str, in which case the reference folder will be the folder containing the (unique) note of the name `_index_{reference}.md`, - or a `Path` object (not just a pathlike!) relative to `vault`, in which case the path will be the path to the reference folder. 
        ) -> Path: # Relative to `vault`.
    """
    Returns the path to the reference directory in a vault.
    
    Assumes that the reference folder has an index note named
    `_index_{reference_name}.md`, this note is the unique note in the vault
    with this filename, and the cache in the `VaultNote` class for `vault` is
    updated.

    **Raises**

    - TypeError
        - If `reference` is not a str or PathLike.
    - 
    
    """
    index_note = index_note_for_reference(vault, reference)
    if index_note.exists(update_cache=False):
        return Path(index_note.path(relative=True)).parent
    else:
        raise NoteDoesNotExistError.from_note_name(index_note.name)

# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 18
def _make_reference_folder(
        vault: Path, location: PathLike, reference_name: str,
        reference_directory: PathLike, overwrite: Union[str, None], verbose: bool) -> None:
    """Makes a folder of a specified name in the specified directory.
    
    If `overwrite` is `'w'`, then the reference folder is assumed to not
    exist.

    This method is Intended for making a reference folder for an Obsidian
    vault.
    
    **Parameters**
    - vault - PathLike
        - The path to the Obsidian vault in which to make the reference folder.
    - location - PathLike
        - The directory of the parent of the new folder to be made, relative
        to `vault`. 
    - reference_name - str
        - The name of the reference to be created; the folder's name will be
        this string.
    - reference_directory - PathLike
        - Is `location / reference_name`; in particular, this is a path
        relative to `vault`.
    - overwrite - `'w'`, `'a'`, or `None`.
        - Specifies if and how to overwrite the reference folder if it already
        exists.
            - If `'w'`, then the reference folder is assumed to not exist, and
            the reference folder is created.
            - If `'a'`, then the reference folder may or may not exist, and the
            reference folder is created if it does not exist.
            - If `None`, then the reference folder may or may not exist. If the
            reference folder exists, then a `FileExistsError` is raised. If the
            reference folder does not exist, then it is created.
    - verbose - bool
        - If `True`, print messages.
        
    **Raises**
    - FileNotFoundError
        - If `location` does not exist as a path relative to `vault`.
    - FileExistsError
        - If the reference folder already exists and 1. overwrite is `'w'` or
        2. overwrite is `'None'`. The former case is expected to not happen.
    """
    if verbose:
        print(f"Attempting to create a the folder '{reference_directory}'"
              f" in the directory '{vault / location}.'")

    if not os.path.exists(vault / location):
        raise FileNotFoundError(
            f"Attempted to create a reference folder at {vault / reference_directory}"
            f", but the parent directory {vault / location} does not" 
            " exist.")
    if os.path.exists(vault / reference_directory):
        if overwrite in ['w', None]:
            raise FileExistsError(
                "Attempted to create a reference folder at"
                f" {reference_directory}, but this directory already exists.")
    else:
        os.mkdir(vault / reference_directory)


# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 20
def _chapter_titles(chapters: list[Union[str, list[str]]]) -> list[str]:
    """
    Return the list of chapters of a reference from a formatted list of chapters
    and sections.

    **Parameters**
    - chapters - list[Union[str, list[str]]]
        - A list whose items are str or list of str. If an item is a string, then the
        item is the title of a chapter of the reference. If an item is a list of string,
        then the item contains the title of the chapter of the reference as its index-0
        item, and the titles of the sections for the chapter.

    **Returns**
     - list[str]
    """
    return [chapter if isinstance(chapter, str) else chapter[0] for chapter in chapters]

# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 22
def _make_index_file(
        vault: PathLike, reference_directory: PathLike, reference_name: str,
        chapters: list[Union[str, list[str]]]) -> None:
    """
    Create the index file for the reference folder.

    The newly created index file will have a bulleted list of Obsidian links to the
    index files of the chapters/sections of the reference.

    **Parameters**
    - vault - PathLike
    - reference_directory - PathLike
    - reference_name - str
    - chapters - list[Union[str, list[str]]]
        - A list whose items are str or list of str. If an item is a string, then the
        item is the title of a chapter of the reference. If an item is a list of string,
        then the item contains the title of the chapter of the reference as its index-0
        item, and the titles of the sections for the chapter.
    """
    index_note = VaultNote(vault, rel_path = reference_directory / f'_index_{reference_name}.md')
    index_note.create()
    chapter_titles = _chapter_titles(chapters)

    chapter_bullets = [f'- [[_index_{convert_title_to_folder_name(chapter_title)}]]'
                        for chapter_title in chapter_titles]
    mf = MarkdownFile.from_list(chapter_bullets)
    mf.write(index_note)

# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 24
def _make_chapter_folders_and_indices(
        chapters: list[Union[str, list[str]]],
        vault: PathLike,
        reference_directory: PathLike) -> None:
    chapter_titles = _chapter_titles(chapters)
    for chapter_title, chapter_sections in zip(chapter_titles, chapters):
        _make_single_chapter_folders(chapter_sections, chapter_title, vault, reference_directory)
        _make_single_chapter_index(chapter_sections, chapter_title, vault, reference_directory)

def _make_single_chapter_folders(
        chapter_sections: Union[str, list[str]],
        chapter_title: str,
        vault: Path,
        reference_directory: PathLike):
    chapter_title = convert_title_to_folder_name(chapter_title)
    os.mkdir(vault / reference_directory / chapter_title)

    if not isinstance(chapter_sections, list):  # i.e. chapter does not have sections
        return
    subchapter_titles = chapter_sections[1:]
    for subchapter_title in subchapter_titles:
        os.mkdir(vault / reference_directory / chapter_title /\
                    convert_title_to_folder_name(subchapter_title))


def _make_single_chapter_index(
        chapter_sections: Union[str, list[str]],
        chapter_title: str,
        vault: Path,
        reference_directory: PathLike):
    chapter_title = convert_title_to_folder_name(chapter_title)
    chapter_index_note = VaultNote(
        vault, rel_path=reference_directory / chapter_title\
        / f"_index_{chapter_title}.md")
    chapter_index_note.create()

    subchapter_titles = chapter_sections[1:]
    headings = [f'# {subchapter_title}\n\n\n'
                for subchapter_title in subchapter_titles]
    mf = MarkdownFile.from_list(headings)
    mf.write(chapter_index_note)

# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 26
def _make_reference_file(
        reference_name, references_folder,
        vault,
        authors, author_files) -> None:
    """
    The references folder has subfolders 'A-E', 'F-J', etc. each of which contains
    subfolders for each letter in the English alphabet, each of which in turn contains
    reference notes
    """
    if not os.path.exists(vault / references_folder):
        raise FileNotFoundError(
            f"References folder does not exist: {vault / references_folder}")

    if reference_name[0].isalpha():
        alphabet_group = alphabet_to_alphabet_group(reference_name[0])
        folder_to_make_reference_file = Path(references_folder)\
            / alphabet_group / reference_name[0].upper()
    else:
        folder_to_make_reference_file = Path(references_folder)
    reference_file_path = folder_to_make_reference_file\
        / f'_reference_{reference_name}.md'
    VaultNote(vault, rel_path=reference_file_path).create()
    # TODO author stuff

# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 28
def _manifest_template_file(
        template_file_name: str,
        reference_name: str,
        vault: PathLike,
        authors: Union[str, list[str]])\
        -> MarkdownFile:
    """
    Return a `MarkdownFile` object based on a specified template file
    with some information about the reference added.

    **Parameters**
    - template_file_name: str
        - The template file's name. This is assumed to be unique in
        the vault.
    - reference_name: str
    - vault: PathLike
    - authors: Union[str, list[str]]

    **Returns**
    - MarkdownFile

    **Raises**
    - NoteNotUniqueError
        - If the template file's name is not unique in the vault.
    - NoteDoesNotExistError
        - If a note with the template file's name does not exist in the
        vault.
    """
    # TODO: sort authors by alphabetical order
    if isinstance(authors, str):
        authors = [authors]
    # TODO: get MarkdownFile by VaultNote
    # template_file_path = note_path_by_name(template_file_name, vault)
    # template_file = MarkdownFile.from_file(
    #     Path(vault) / template_file_path)
    template_file = MarkdownFile.from_vault_note(
        VaultNote(vault, name=template_file_name))
    embedding_link = ObsidianLink(is_embedded=True,
        file_name=f'_reference_{reference_name}',
        anchor=0, custom_text=0, link_type = LinkType.WIKILINK)
    template_file.add_line_in_section(
        title="References",
        line_dict={'type': MarkdownLineEnum.DEFAULT,
                   'line': f'{embedding_link.to_string()}\n'})

    last_line = template_file.pop_line()
    last_line['line'] = f'[^1]: {", ".join(authors)}, '
    template_file.add_line_to_end(last_line)

    # TODO: delete the below
    # ref_line_index = template_file.get_line_number_of_heading(
    #     title="References")
    # embedding_link = ObsidianLink(is_embedded=True,
    #     file_name=f'_reference_{reference_name}',
    #     anchor=0, custom_text=0, link_type = LinkType.WIKILINK)
    # template_file.insert_line(
    #     ref_line_index+1, {'type': MarkdownLineEnum.DEFAULT,
    #                        'line': f'{embedding_link.to_string()}\n'})

    # TODO: make sure the above line works and delete the below line
    # template_file.parts.insert(ref_line_index+1, {'type': MarkdownLineEnum.DEFAULT,
    #                        'line': f'{embedding_link.to_string()}\n'})
    template_file.add_tags([f'#_reference/{reference_name}'])
    return template_file

# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 30
def _make_template_file(
        template_file_name,
        reference_name,
        vault,
        templates_folder,
        authors: Union[str, list[str]],
        make_second_template_file_in_reference_directory: bool,
        reference_directory: Path
        ) -> None:
    template_file = _manifest_template_file(
        template_file_name, reference_name, vault, authors)

    # TODO factor out; this repeats with code in _make_reference_file above.
    if not os.path.exists(vault / templates_folder):
        raise FileNotFoundError(
            f"References folder does not exist: {vault / templates_folder}")
    if reference_name[0].isalpha():
        alphabet_group = alphabet_to_alphabet_group(reference_name[0])
        folder_to_make_template_file = Path(templates_folder)\
            / alphabet_group / reference_name[0].upper()
    else:
        folder_to_make_template_file = Path(templates_folder)

    template_file_path = folder_to_make_template_file\
        / f'_template_{reference_name}.md'
    _create_template_note_at(vault, template_file_path, template_file)

    if make_second_template_file_in_reference_directory:
        second_template_file_path = reference_directory / f'_template_{reference_name}_2.md'
        _create_template_note_at(vault, second_template_file_path, template_file)


def _create_template_note_at(
        vault: Path,
        note_path: Path, # Relative to `vault`
        template_file: MarkdownFile):
    template_note = VaultNote(vault, rel_path=note_path)
    template_note.create()
    template_file.write(template_note)

# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 32
def _make_notation_index_file(
        reference_directory: PathLike,
        reference_name: str,
        vault: PathLike,
        notation_index_template_file_name: str,
        authors: list[str]) -> None:
    """Create the notation index file for the reference.

    The notation index file is named `_notation_{reference_name}.md`, and is
    located in the main directory of the new reference.

    **Parameters**
    - reference_directory - PathLike
        - The main directory of the reference. Relative to `vault`.
    - reference_name - str
    - vault - PathLike
    - notation_index_template_file_name - str
        - The template file whose contents will fill the newly created notation
        index file.
    
    **Raises**
    - NoteNotUniqueError
        - If the template file's name is not unique in the vault.
    - NoteDoesNotExistError
        - If a note with the template file's name does not exist in the
        vault.
    """
    template_file = _manifest_template_file(
        notation_index_template_file_name, reference_name, vault, authors)
    notation_index_file_path = Path(reference_directory)\
        / f'_notation_{reference_name}.md'
    notation_index_note = VaultNote(vault, rel_path=notation_index_file_path)
    notation_index_note.create()
    template_file.write(notation_index_note)

# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 34
# TODO: change "file" in these helper methods and their respective doccstrings to "note"
def _make_glossary_file(
        reference_directory: PathLike, reference_name: str, vault: PathLike,
        glossary_template_file_name: str) -> None:
    """Create the glossary file for the reference.

    The notation index file is named `_glossary_{reference_name}.md`, and is
    located in the main directory of the new reference.

    **Parameters**
    - reference_directory - PathLike
        - The main directory of the reference.
    - reference_name - str
    - vault - PathLike
    - glossary_template_file_name - str
        - The template file whose contents will fill the newly created
        glossary file.
    
    """
    template_note = VaultNote(vault, name=glossary_template_file_name)
    template_file = MarkdownFile.from_vault_note(template_note)
    glossary_file_path = reference_directory / f'_glossary_{reference_name}.md'
    glossary_note = VaultNote(vault, rel_path=glossary_file_path)
    glossary_note.create()
    template_file.write(glossary_note)

# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 36
def _make_temp_folder(
        reference_directory: PathLike, reference_name: str,
        vault: PathLike) -> None:
    """
    Make a folder for temporarily holding notes and a corresponding index file.

    **Parameters**
    - reference_directory - PathLike
    - reference_name - str
    - vault - PathLike

    """

    temp_directory = vault / reference_directory / '_temp'
    os.mkdir(temp_directory)
    # TODO: use vaultnote.create and markdownfile.write
    temp_file_path = reference_directory / '_temp' / f'_index_temp_{reference_name}.md'
    temp_note = VaultNote(vault, rel_path = temp_file_path)
    temp_note.create()

# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 40
def copy_obsidian_vault_configs(
        vault: PathLike,
        reference_directory: PathLike, # The folder into which to copy the Obsidian configs. Relative to `vault`.
        configs_folder: PathLike # The folder containing the Obsidian configs. This is either an absolute path or relative to the current working directory.
        ) -> None:
    """
    Copy the vault's Obsidian config files into the reference directory.
    """
    shutil.copytree(configs_folder, vault / reference_directory / '.obsidian')

# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 43
def _obsidian_vault_plugin_configs_file(
        vault: PathLike,
        plugin_name: str, # The folder name of the Obsidian plugin. This can be found either in the `.obsidian` directory or in the `.obsidian/plugins` directory in the vault .
        plugin_is_core: bool #`True` if the plugin is a core Obsidian.md plugin. `False` if the plugin is a community plugin.
        ) -> Path:
    if plugin_is_core:
        return Path(vault) / '.obsidian' / f'{plugin_name}.json'
    else:
        return Path(vault) / '.obsidian' / plugin_name / 'data.json'

# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 45
def get_obsidian_vault_plugin_configs(
        vault: PathLike,
        plugin_name: str, # The folder name of the Obsidian plugin. This can be found in the `.obsidian` directory in the vault.
        plugin_is_core: bool #`True` if the plugin is a core Obsidian.md plugin. `False` if the plugin is a community plugin.
        ) -> dict[str, Union[str, int, float, bool, None, list, dict]]: # A json dict. 
    """Obtain the JSON object representing the `data.json` file of
    an Obsidian plugin.
    
    This function assumes that the the Obsidian plugin exists in `vault` in that the plugin
    has a `data.json` file.
    """
    with open(_obsidian_vault_plugin_configs_file(vault, plugin_name, plugin_is_core), 'r') as file:
        return json.load(file)
    

# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 47
def modify_obsidian_vault_plugin_configs(
        vault: PathLike,
        plugin_name: str, # The folder name of the Obsidian plugin. This can be found in the `.obsidian` directory in the vault.
        plugin_is_core: bool, #`True` if the plugin is a core Obsidian.md plugin. `False` if the plugin is a community plugin.
        field: str, # The field to modify
        value: Union[str, int, float, bool, None, list, dict], # The JSON value to set the field as
        ) -> None:
    """Modify/set a top level field in an Obsidian vault plugin configs file.
    
    Assumes that the Obsidian vault plugins configs are indented by 2 spaces.

    Note that only top level values can be directly set by this function.

    """
    configs = get_obsidian_vault_plugin_configs(vault, plugin_name, plugin_is_core)
    configs[field] = value
    with open(_obsidian_vault_plugin_configs_file(vault, plugin_name, plugin_is_core), 'w') as file:
        json.dump(configs, file, indent=2)

# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 49
def _modify_fast_link_edit_and_templates(
        vault: PathLike,
        reference_name: str, # The value to change the `referenceName` field in the `fast-link-edit` plugin into.
        template_location: str = '.' # The value to change the `folder` field in the `templates` plugin into.
    ) -> None:
    """Modify the `fast-link-edit` and `templates` Obsidian plugins for a vault if
    each exists."""
    try:
        modify_obsidian_vault_plugin_configs(
            vault, 'fast-link-edit', False, 'referenceName', reference_name)
    except FileNotFoundError:
        warnings.warn(
            "Attempted to modify the the new reference folder's configuration file"
            " for the `fast-link-edit` plugin, but the file does not exist.",
            UserWarning)

    try:
        modify_obsidian_vault_plugin_configs(
            vault, 'templates', True, 'folder', template_location)
    except FileNotFoundError:
        warnings.warn(
            "Attempted to modify the the new reference folder's configuration file"
            " for the `templates` plugin, but the file does not exist.",
            UserWarning)

# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 51
def copy_obsidian_vault_configs_with_nice_modifications(
        vault: PathLike,
        reference_directory: PathLike, # The folder into which to copy the Obsidian configs. Relative to `vault`.
        configs_folder: PathLike, # The folder containing the Obsidian configs. This is either an absolute path or relative to the current working directory.
        reference_name: str = None, # The name of the reference and the value to change the `referenceName` field in the `fast-link-edit` plugin into. If `None`, then the reference name should be obtained as the name of `reference_directory`
        template_location: str = '.' # The location of the template file(s) and the value to change the `folder` field in the `templates` plugin into.
        ) -> None:
    """
    Copy the vault's Obsidian config files into the reference directory and make some nice moodifications
    """
    copy_obsidian_vault_configs(vault, reference_directory, configs_folder)
    if reference_name is None:
        reference_name = path_name_no_ext(reference_directory)
    # Note that the config file that is being modified belongs to the "subvault",
    # i.e. the reference folder.
    _modify_fast_link_edit_and_templates(vault / reference_directory, reference_name, template_location)

# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 55
# TODO: add reference link in index note of parent folder
# TODO: Make another template file in the reference folder
# TODO: When copying over configs, change some things.
# TODO: add verbose option. 
#     Done: Verbose in _make_reference_folder
# TODO: add type hinting in hidden methods and docstrings.
# TODO: make a method for deleting reference.
# TODO: enable overwrite existing 
# TODO: make a function to detect connections between references.
# TODO: Implement overwrite existing files/overwrite entire folder option.
# TODO: for some reason, glossary isn't being added.
# TODO: test add obsidian config folder
# TODO: make TODO file


def setup_folder_for_new_reference(
        reference_name: str, # The name of the reference to be created; the folder's name will be this string.
        location: PathLike, # The directory of the parent of the new folder to be made, relative to `vault`.
        authors: Union[str, list[str]], # Each str is the family name of each author.
        vault: PathLike, # The path to the Obsidian vault in which to make the reference folder.
        author_folder: PathLike = '_mathematicians', # The directory where the author files are stored in.  Relative to `vault`. 
        references_folder: PathLike = '_references', # The directory where the references files are stored in.  Relative to `vault`.
        templates_folder: PathLike = '_templates', # The directory where the template files are stored in.  Relative to `vault`.
        template_file_name: str = '_template_common', # The template file from which to base the template file of the new reference.
        notation_index_template_file_name: str = '_template_notation_index', # The template file from which to base the notation index file of the new reference.
        glossary_template_file_name: str = '_template_glossary', # The template file from which to base the glossary file of the new reference. Defaults to `'_template_glossary'`.
        chapters: Optional[list[Union[str, list[str]]]] = None, # A list where each item is either a str or a list of str.  If the item is a str, then it should be the title of a chapter named in the format `"1. {title}"`, `"2. {title}"`, or `"I. {title}"`, `"II. {title}"` etc. If the item is a list of str, then the 0th item should be the title of the chapter, formatted as in the previous sentence, and the other items should be titles of subchapters/subsections, also formatted in the same manner (e.g. if the subchapter is 7.2 of a book, then it should be `"2. {title}"`).  Defaults to `None`, in which case no chapters are specified and hence no chapter folders and indices are created.
        setup_temp_folder: bool = True, # If `True`, creates a `_temp` folder with an index file. This folder serves to house notes auto-created from LaTeX text files before moving them to their correct directories. Defaults to `True`.
        make_second_template_file_in_reference_directory: bool = True, # If `True`, creates a copy of the template note within the directory for the reference.
        copy_obsidian_configs: Optional[PathLike] = '.obsidian', # The folder relative to `vault` from which to copy obsidian configs.  If `None`, then no obsidian configs are copied to the reference folder. Defaults to `.obsidian`. 
        overwrite: Union[str, None] = None, # Specifies if and how to overwrite the reference folder if it already exists.  - If `'w'`, then deletes the contents of the existing reference folder, as well as the template and reference file before setting up the reference folder before creating the new reference folder.  - If `'a'`, then overwrites the contents of the reference folder, but does not remove existing files/folders.  - If `None`, then does not modify the existing reference folder and raises a `FileExistsError`.
        confirm_overwrite: bool = True, # Specifies whether or not to confirm the deletion of the reference folder if it already exists and if `overwrite` is `'w'`. Defaults to `True`.
        verbose: bool = False
        ) -> None:
    """Creates and sets up a new folder for a new reference.
    
    More specifically, the following are set up:
    
    1. The folder
    2. An index file
    3. Chapter folders and indices
    4. Files in the `Mathematicians` folder, if applicable.
    5. A reference file
        - For embedding in the standard information notes for the reference
    6. A template file
    7. A glossary file
    8. A `#_meta/reference` tag for the new reference
    9. A notation index file
    10. Optionally, a `_temp` directory
    11. Optionally, the `./obsidian` config folder from the vault is
    copied.
    
    After they are setup, the user should
    1. Add content in the reference file.
    2. Modify the last line of the template file.
        
    **Raises**
    - FileExistsError
        - If `overwrite` is `None` and a folder of the name `reference_name`
        exists at `Path(vault) / location`.
    """
    if verbose:
        print("Setting up a new folder for a reference.")
        print(f"\tReference name: {reference_name}")
        print(f"\tVault: {vault}")
        print(f"\tLocation of new folder (relative to vault): {location}")
    vault = Path(vault)
    if not chapters:
        chapters = []
    reference_directory = Path(location) / reference_name

    if overwrite == 'w' and os.path.exists(vault / reference_directory):
        delete_reference_folder(
            vault, reference_directory, verbose=verbose,
            confirm=confirm_overwrite)

    _make_reference_folder(
        vault, location, reference_name, reference_directory,
        overwrite=overwrite, verbose=verbose)
    _make_index_file(vault, reference_directory, reference_name, chapters)
    _make_chapter_folders_and_indices(chapters, vault, reference_directory)

    # Look for/make mathematician files

    # TODO: `author_files` ultimately does not really do anything. Change this
    author_files = []
    # for author in authors:
    #     author_file = find_author_file(vault, author, author_folder)
    #     if author_file is None:
    #         print('')  # TODO
    #     author_files.append(author_file)

    _make_reference_file(
        reference_name, references_folder, vault,
        authors, author_files)
    _make_template_file(
        template_file_name, reference_name, vault,
        templates_folder, authors, make_second_template_file_in_reference_directory,
        reference_directory)
    _make_notation_index_file(
        reference_directory, reference_name, vault,
        notation_index_template_file_name, authors)
    _make_glossary_file(
        reference_directory, reference_name, vault,
        glossary_template_file_name)
    if setup_temp_folder:
        _make_temp_folder(reference_directory, reference_name, vault)
    if copy_obsidian_configs is not None:
        configs_folder = vault / copy_obsidian_configs
        # copy_obsidian_vault_configs(vault, reference_directory, configs_folder)
        copy_obsidian_vault_configs_with_nice_modifications(
            vault, reference_directory, configs_folder)
        # Modify 
    if verbose:
        print(f'Created a new reference folder at {location}.'\
            ' Make sure to update the reference file and'\
            ' The files for new mathematicians!')
