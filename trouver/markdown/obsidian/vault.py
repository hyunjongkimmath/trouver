"""Functions for inspecting and modifying Obsidian.md vaults and their files and folders"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/03_markdown.obsidian.vault.ipynb.

# %% auto 0
__all__ = ['NoteNotUniqueError', 'NoteDoesNotExistError', 'NotePathIsNotIdentifiedError', 'path_to_obs_id',
           'all_paths_to_notes_in_vault', 'all_note_paths_by_name', 'note_path_by_name', 'note_name_unique',
           'note_name_from_path', 'VaultNote']

# %% ../../../nbs/03_markdown.obsidian.vault.ipynb 3
from pathlib import Path
import os
from os import PathLike
from trouver.helper.files_and_folders import (
    path_no_ext, path_name_no_ext
)
from typing import Optional, Union

# %% ../../../nbs/03_markdown.obsidian.vault.ipynb 7
class NoteNotUniqueError(FileNotFoundError):
    """
    A `NoteNotUniqueError` is raised when a `VaultNote` is specified
    by name and not by relative path in the vault, but
    the vault is found to have multiple notes of the name.

    **Attributes**

    - `note_name` - str
        - The name of the note which is not unique in the vault.
    - `notes` - list[str]
        - The paths of the notes whose names are `note_name`.
    """
    def __init__(self, /, *args, **kwargs):
        super().__init__(*args, **kwargs)
            
    @classmethod
    def from_note_names(cls, note_name: str, notes: list[str]):
        """Construct a `NoteNotUniqueError` object from note names"""
        return cls(
            f'The note of the following name is not unique: {note_name}\n'\
            f'The name points to the following files: {notes}')



# %% ../../../nbs/03_markdown.obsidian.vault.ipynb 9
class NoteDoesNotExistError(FileNotFoundError):
    """
    A `NoteDoesNotExistError` is raised when a `VaultNote` is specified
    by either name and or by relative path in the vault, but
    the vault is found to have no notes of the name.
    """
    def __init__(self, /, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def from_note_name(cls, note_name: str):
        """Construct a `NoteDoesNotExistError` object from note name"""
        return cls(
            f'The note of the following name does not exist: {note_name}.'
            f' Make sure that the argument passed to `note_name` does not'
            f' erroneously end with `.md`, e.g. pass `this_is_a_note`'
            f' instead of `this_is_a_note.md`.')

# %% ../../../nbs/03_markdown.obsidian.vault.ipynb 11
class NotePathIsNotIdentifiedError(RuntimeError):
    """
    A `NotePathIsNotIdentifiedError` is raised when the `rel_path` attribute of a
    `VaultNote` object is expected to be identified (i.e. a path and not `None`) but
    this expectation is not fulfilled.
    """
    def __init__(self, /, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def from_note(
            cls,
            note):
        """Construct a `NotePatahIsNotIdentifiedErrro` object from a `VaultNote`."""
        return cls(f'The `rel_path` attribute of the `VaultNote` object is expected'
                   f' to be identified, and yet it is not. The vault of the'
                   f' `VaultNote` object is {note.vault} and the name of the object'
                   f' is {note.name}.')

# %% ../../../nbs/03_markdown.obsidian.vault.ipynb 14
def path_to_obs_id(
        rel_path: PathLike # A path representation the path of an Obsidian note relative to its vault. This does not have to be an existing path.
        ) -> str: # The obsidian url of the hypothetical note within its vault. Note that this does not end with the file extension `.md`.
    """Convert a relative path of an Obsidian note to the Obsidian identifying
    str.
    
    This identification is for a vault-internal Wikilink.

    Note that this function does not have a vault as a parameter.
    """
    path_without_extension = path_no_ext(rel_path)
    return path_without_extension.replace('\\', '/')

# %% ../../../nbs/03_markdown.obsidian.vault.ipynb 21
def all_paths_to_notes_in_vault(
        vault: PathLike, as_dict: bool = False)\
        -> Union[list[str], dict[str, list[str]]]:
    """Return the paths, relative to the Obsidian vault, of notes 
    in the Obsidian vault.
       
    This may not actually return all of the paths to the notes, see
    the parameter `as_dict`.

    **Parameters**

    - `vault` - `PathLike`
        - The path to the Obsidian vault directory
    - `as_dict` - `bool`
        - If `True`, then returns a dict. If `False`, then returns
        a list. Defaults to `False`. If there are multiple notes with the same
        name in the vault, and `as_dict` is set to `True`, then the dictionary
        will contain only one of the (relative) paths to those notes among its
        values. If `as_dict` is set to `False`, then the list will contain
        all the paths to the notes even when notes with non-unique names exist.
        
    **Returns**

    - Union[list[str], dict[str, str]]
        - Each str represents the path relative to `vault`. If `as_dict` is
        True, then returns a dict whose keys are str, which are (unique) names
        of the notes in the vault, and the values are the paths.
    """
    vault = Path(vault)
    paths =  [os.path.relpath(path, vault) for path in vault.glob(f'**/*.md')]
    if as_dict:
        dicty = {path_name_no_ext(path): [] for path in paths}
        for path in paths:
            dicty[path_name_no_ext(path)].append(path)
        return dicty
    else:
        return paths


# %% ../../../nbs/03_markdown.obsidian.vault.ipynb 27
def all_note_paths_by_name(
        name: str,  # Name of the note(s) to find
        vault: PathLike,  # The path to the Obsidian vault directory
        subdirectory: Union[PathLike, None] = None # The path to a subdirectory in the Obsidian vault, relative to `vault`. If `None`, then denotes the root of the vault.
        ) -> list[Path]: # Each item is a path to a note of the given name, relative to `vault`.
    """Return the relative paths to all notes in the Obsidian vault 
    with the specified name in the specified subdirectory.
    
    This function does not assume that the specified subdirectory in the vault
    has at most one note of the specified name.
    
    """
    vault = vault if vault != None else ''
    vault = Path(vault)
    subdirectory = subdirectory if subdirectory != None else ''
    directory_path = vault / subdirectory
    all_notes_of_name = directory_path.glob(f'**/{name}.md')
    all_notes_of_name = list(all_notes_of_name)
    return [note_path.relative_to(vault) for note_path in all_notes_of_name]

# %% ../../../nbs/03_markdown.obsidian.vault.ipynb 32
# TODO: include examples of `hints` parameter.
def note_path_by_name(
        name: str, # The path to the Obsidian vault directory.
        vault: PathLike, # The path to a subdirectory in the Obsidian vault. If `None`, then denotes the root of the vault.
        subdirectory: Union[PathLike, None] = None, # The path to a subdirectory in the Obsidian vault. If `None`, then denotes the root of the vault.
        hints: Union[list[PathLike], None] = None # Hints of which directories, relative to `subdirectory` that the note may likely be in. This is for speedup. The directories will be searched in the order listed.
        ) -> Path: # The note of the specified name in the specified subdirectory of the vault.
    """Return the path, relative to a subdirectory in the vault, 
    of the note of the specified name.

    **Raises**

    - NoteNotUniqueError
        - If the note of the specified name is not unique in the subdirectory.
    - NoteDoesNotExistError
        - If the note of the specified name does not exist in the subdirectory.

    **See Also**

    - The constructor of the `VaultNote` class
        - passing an argument to the `name` parameter of this constructor
        method essentially does the same thing as this function, except the
        constructor method uses a cache.
    """
    if not subdirectory:
        subdirectory = ''
    if not hints:
        hints = []
    vault = Path(vault)
    subdirectory = Path(subdirectory)
    # absolute_subdirectory = vault / subdirectory
    hints.append('')  # Search in subdirectory if all else fails
    for hint in hints:
        search_results = all_note_paths_by_name(name, vault, subdirectory / hint)
        if len(search_results) > 1:
            raise NoteNotUniqueError.from_note_names(name, search_results)
        elif len(search_results) == 1:
            return search_results[0]
    raise NoteDoesNotExistError.from_note_name(name)

# %% ../../../nbs/03_markdown.obsidian.vault.ipynb 42
def note_name_unique(
        name: str, # Name of the note.
        vault: PathLike # Path to the vault.
        ) -> bool: 
    """Return `True` if a note of the specified name exists and 
    is unique in the Obsidian vault.
    """
    return len(all_note_paths_by_name(name, vault)) == 1

# %% ../../../nbs/03_markdown.obsidian.vault.ipynb 46
def note_name_from_path(
        note_path: str # The path of the note. The note does not need to exist.
        ) -> str: # The name of the note.
    """Return the name of a note from its path.
    """
    return path_name_no_ext(note_path)

# %% ../../../nbs/03_markdown.obsidian.vault.ipynb 49
# TODO: change NoteDoesNotExistError to NoteNotFoundError if not found in Cache.
# TODO: when making NoteNotFoundError, add it to
# markdown.obsidian.personal.reference.delete_reference_folder

# TODO: modify the constructor so that it does not need the note of the specified name to exist
# TODO: look at parts where the cache is accessed/modified. Factor them out into getter/setter methods
# taking in the vault and name as inputs.
# TODO: look at how NoteDoesNotExistError is used and make modifications to account for the modification
# of the constructor.
# TODO: test hidden methods
class VaultNote:
    """Represents a note in an Obsidian vault, without regards to the contents.
    
    The note does not have to exist, except in circumstances stating 
    otherwise.

    TODO go through the methods of this class to see which methods assume that
    the note exists and which do not.

    TODO finish the sentence below.
    A `VaultNote` can be specified by either the `rel_path` or the `name` argument
    in its constructor. If `name` is specified, then the 
    
    TODO implement subdirectory hint
    
    **Attributes**

    - vault - Path
        - The (relative or absolute) path of the Obsidian vault
        that the note is located in.
    - name - str
        - The name of the note in the vault.
    - rel_path - str
        - The note's path relative to the vault. If 
    - cache - dict[str, dict[str, list[str]]], class attribute
        - The keys are string, which are paths to vaults. The
        corresponding values are dict whose keys are string, which are
        names in the vault of the (unique) note of that name, and whose
        values are list of string, which are paths to the note relative to the
        vault. The cache is not automatically updated when notes are
        moved.
    
    **Parameters**

    - vault - PathLike
    - rel_path - PathLike
    - name - str
        - The name of the note in the vault. Defaults to the empty str.
            - If `None`, then the `rel_path` parameter should be used 
            to determine `self.name` instead. 
            - If not `None`, then the note must uniquely exist in the
            vault.
    - `subdirectory` - Union[PathLike, None]
    - `hints` - list[PathLike]

    **Raises**
    
    - ValueError
        - if `rel_path` and `name` are both `None`.
    """
    
    cache = {}
    
    # TODO: make the constructor take an optional update_cache parameter.
    def __init__(
            self,
            vault: PathLike, # The (relative or absolute) path of the Obsidian vault that the note is located in.
            rel_path: PathLike = None, # The note's path relative to the vault. If `None`, then the `name` parameter is used to determine the note instead. Defaults to `None`.
            name: str = None, # The name of the note. If `None`, then the `rel_path` parameter is used to determine the note instead. Defaults to `None` 
            subdirectory: Union[PathLike, None] = '', # The relative path to a subdirectory in the Obsidian vault. If `None`, then denotes the root of the vault. Defaults to the empty str. 
            hints: list[PathLike] = [], # Paths, relative to `subdirectory`, to directories where the note file may be found. This is for speedup. Defaults to the empty list, in which case the vault note is searched in all of `subdirectory`.
            update_cache: Optional[bool] = True # If `True` and if `rel_path` is not specified (and hence `name` is specified), update the cache
            ):
        self.vault = Path(vault)
        if rel_path is None and name is None:
            raise ValueError(
                "In constructing a `VaultNote` object, the parameters `rel_path`"
                " and `name` parameters were expected to be given arguments, but"
                " both parameters are given `None` as arguments.")
        if rel_path is not None:
            self.rel_path = str(rel_path)
            self.name = note_name_from_path(self.rel_path)
        else:
            self.name = name
            self.rel_path = None
            self.identify_rel_path(update_cache=update_cache)

    def obsidian_identifier(self) -> str:
        """Return the Obsidian identifier of the `VaultNote` object.
        
        This is the note's unqiue Obsidian id in the vault. This is like a
        path str with forward slashes `/` (as opposed to backwards `\` slashes)
        and without a file extension (`.md`).
        """
        return path_to_obs_id(self.rel_path)

    def rel_path_identified(self) -> bool:
        """Return `True` if `self.rel_path` is identified, i.e. is a path
        that is not `None`."""
        return self.rel_path is not None

    def _identify_rel_path(self) -> Union[Path, None]:
        """Returns the Path to the note that this object represents.

        More precisely, if `rel_path` is specified at construction or
        if `self.rel_path` is already identified, then this method
        returns that path. Otherwise, this method looks into the cache to
        check if a note of the `name` specified at construction is in the
        vault and returns the first note in the list of the `name` in the
        cache. If no such note exists, then this method reutrns `None`.
        """
        if self.rel_path is not None:
            return self.rel_path
        cache_search = self.__class__._get_from_cache(self.vault, self.name)
        if cache_search:  # `cache_search` could be `None` or an empty list.
            return cache_search[0]
        return None

    def identify_rel_path(
            self,
            update_cache=False # If `True`, if the cache is searched, and if a note of the specified name is not found in the cache, then the cache is updated and searched again. Defaults to `False`.
            ) -> None:
        """Sets `self.rel_path` to a path, if not already done so.

        If `self.rel_path` is not already set as a path, then the cache
        is searched to find a note whose name is `self.name` (which is
        necessarily specified).
        """
        rel_path = self._identify_rel_path()
        if rel_path is not None:
            self.rel_path = rel_path
        elif update_cache:
            self.__class__.update_cache(self.vault)
            self.identify_rel_path(update_cache=False)

    @classmethod
    def _get_from_cache(
            cls,
            vault: PathLike,
            name: str) -> Union[list[str], None]:
        """Return the
        cache's list of notes of the specified name in the
        specified vault.

        If no such list exists in the cache, then return `None`.
        """
        vault = str(vault)
        if vault not in cls.cache:
            return None
        vault_dict = cls.cache[vault]
        if not name in vault_dict:
            return None
        return vault_dict[name]
                        
    def exists(
            self,
            update_cache=False # If `True`, then update the cache and try to identify `self.rel_path` before verifying whether the note exists in the vault.
            ) -> bool:
        """Returns `True` if `self.rel_path` is identified and
        if the note exists in the vault.
        
        Setting `update_cache` to `True` updates the cache before verifying
        whether the `VaultNote` object exists if the `VaultNote` object is
        specified by `name` and not `rel_path`. Doing so guarantees that the
        output is correct at the possible cost of runtime.
        """
        if self.rel_path is None:
            if update_cache:
                self.identify_rel_path(update_cache=True)
            else:
                return False
        try:
            abs_path = self.path()        
        except NotePathIsNotIdentifiedError as e:
            return False
        return os.path.exists(abs_path)
            
    def path(self,
             relative=False # If `True`, then return the path relative to the vault. Otherwise, return the absolute path.
             ) -> Union[Path, None]: # Path to the note if self.rel_path is deterined. `None` otherwise.
        """Returns the path to the note.

        **Raises**
        - NotePathIsNotIdentifiedError
            - If the relative path of `self` is not identified.
        """
        if not self.rel_path_identified():
            raise NotePathIsNotIdentifiedError.from_note(self)
        return Path(self.rel_path) if relative\
            else self.vault / self.rel_path
    
    def directory(self,
                  relative=False # If `True`, then return the path of the directory relative to the vault.
                  ) -> Path: # The path of the directory that the note is in.
        """Return the directory that the note is in.
        """
        rel_dir = Path(os.path.dirname(self.rel_path))
        return rel_dir if relative else self.vault / rel_dir
    
    def create(self):
        """Create the note if it does not exist.
        
        The directory of the file needs to be created separately
        beforehand.

        If the file exists, then a FileExistsError is raised and
        the file modification time is not changed.
        
        **Raises**

        - FileExistsError
            - If the file already exists.
        - FileNotFoundError
            - If the directory of the file does not already exist.
        """
        Path(self.path()).touch(exist_ok=False)
        self.__class__._add_single_entry_to_cache(
            self.vault, self.rel_path)

    def delete(self):
        """Delete the note if it exists.
        
        This updates the cache if necessary
        """
        if self.exists(update_cache=True):
            os.remove(self.path())
            self.__class__._remove_single_entry_from_cache(self.vault, self.rel_path)
        
    def move_to(self,
                rel_path: PathLike # The path in which to rename the path to `self` as, relative to `self.vault`.
                ) -> None:
        """Move/rename the note to the specified location in the vault,
        assuming that it exists.
        """
        if not self.exists():
            return
        os.rename(self.path(), Path(self.vault) / rel_path)
        self.__class__._remove_single_entry_from_cache(
            self.vault, Path(self.rel_path))
        self.__class__._add_single_entry_to_cache(
            self.vault, Path(rel_path))
        self.rel_path = str(rel_path)
        self.name = note_name_from_path(self.rel_path)
        
    def move_to_folder(self,
                       rel_dir: PathLike # The path of the directory in which to move `self` to, relative to `self.vault`.
                       ) -> None:
        """Move the note to the specified folder in the vault, assuming that
        if exists.
        """
        self.move_to(Path(rel_dir) / f'{self.name}.md')
        
    def text(self
            ) -> str: # Text contained in the note, assuming that the note exists.
        """Returns the text contained in the note.
        
        **Raises**

        - NoteDoesNotExistError
            - If `self` does not point to an existing note.
        """
        if not self.exists():
            raise NoteDoesNotExistError.from_note_name(self.name)
        with open(self.vault / self.rel_path, 
                  'r', encoding='utf-8') as reader:
            text = reader.read()
            reader.close()
        return text

    @classmethod
    def update_cache(cls,
                     vault: PathLike # The vault.
                     ) -> None:
        """Class method to update cache for `vault` by inspecting all files
        in subdirectories of `vault`."""
        VaultNote.cache[str(vault)] = all_paths_to_notes_in_vault(
            vault, as_dict=True)
        
    @classmethod
    def clear_cache(cls):
        """Class method to clear out the entire cache for all vaults."""
        VaultNote.cache = {}
        
    @classmethod
    def _check_name_exists_and_unique_in_vault_cache(
            cls,
            vault: PathLike, # The vault
            name: str # The name
            ) -> None:
        """
        Raise `NoteNotUniqueError` or `NoteDoesNotExistError` if the note of
        the specified name is not unique or does not exist in the cache.
        
        **Parameters**
        - vault - PathLike
        - name - str

        **Raises**
        - `NoteNotUniqueError`
        - `NoteDoesNotExistError`.
        """
        vault_dict = cls.cache[str(vault)]
        if not name in vault_dict or len(vault_dict[name]) == 0:
            raise NoteDoesNotExistError.from_note_name(name)
        elif len(vault_dict[name]) > 1:
            raise NoteNotUniqueError.from_note_names(
                name, vault_dict[name])

    @classmethod
    def _check_if_cache_needs_to_update(
            cls, vault: PathLike, name: str) -> bool:
        """Returns `True` if the cache needs to update by virtue of not finding
        notes of the specified `name` in the `vault`.
        """
        return not bool(cls._get_from_cache(vault, name))

    @classmethod
    def _add_single_entry_to_cache(
            cls, vault: PathLike, rel_path: PathLike) -> None:
        """Adds a single entry for a note to the cache.
        
        Does nothing if the entry already exists.

        **Parameters**
        - vault - PathLike
        - rel_path - PathLike
            - The path to the note, relative to `vault`.
        """
        vault_str = str(vault)
        if vault_str not in cls.cache:
            cls.cache[vault_str] = {}
        name = note_name_from_path(rel_path)
        if name not in cls.cache[vault_str]:
            cls.cache[vault_str][name] = []
        if rel_path not in cls.cache[vault_str][name]:
            cls.cache[vault_str][name].append(str(rel_path))
    
    @classmethod
    def _remove_single_entry_from_cache(
            cls, vault: PathLike, rel_path: PathLike) -> None:
        """Removes a single entry for a note from the cache.

        Does nothing if the entry is not already there.

        **Parameters**
        - vault - PathLike
        - rel_path - PathLike
            - The path to the note, relative to `vault`.
        """
        vault_str = str(vault)
        if vault_str not in cls.cache:
            return
        name = note_name_from_path(rel_path)
        if name not in cls.cache[vault_str]:
            return
        rel_path = Path(rel_path)
        cls.cache[vault_str][name] = [
            cache_path for cache_path in cls.cache[vault_str][name]
            if Path(cache_path) != rel_path]

    @classmethod
    def unique_name(
            cls,
            name: str, # The base name for the note.
            vault: PathLike # The vault
            ) -> str: # A str obtained by appending `_{some number}` to the end of `name`.
        """A class method to return a name for a note that is unique in
        the vault based on a specified name.
        """
        if not str(vault) in VaultNote.cache:
            cls.update_cache(vault)
        if not name in VaultNote.cache[str(vault)]:
            return name
        i = 1
        while f'{name}_{i}' in VaultNote.cache[str(vault)]:
            i += 1
        return f'{name}_{i}'
