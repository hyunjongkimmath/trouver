"""Deal with the preamble of a LaTeX document"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/32_latex.preamble.ipynb.

# %% auto 0
__all__ = ['divide_preamble', 'replace_inclusion_of_style_file_with_code']

# %% ../../nbs/32_latex.preamble.ipynb 2
import re
from os import PathLike
from pathlib import Path
import warnings

# %% ../../nbs/32_latex.preamble.ipynb 6
def divide_preamble(
        text: str, # LaTeX document
        document_environment_name: str = "document"
        ) -> tuple[str, str]:
    """Divide the preamble from the rest of a LaTeX document.
    """
    begin_environment_str = rf'\begin{{{document_environment_name}}}'
    pattern = re.compile(re.escape(begin_environment_str))
    match = re.search(pattern, text) 
    start_match, end_match = match.span()
    return text[:start_match], text[start_match:]

    

# %% ../../nbs/32_latex.preamble.ipynb 10
def replace_inclusion_of_style_file_with_code(
        document: str,
        dir: PathLike # The directory containing the style file.
        ) -> str: # The modified document with style file inclusions replaced by their contents.
    r"""
    Replace style file inclusions in `document` with the code of the style files.

    This function searches for occurrences of `\usepackage{...}`, `\input{...}`, 
    `\import{...}{...}`, `\includefrom{...}{...}`, and `\subincludefrom{...}{...}`
    and replaces them with the actual contents of the corresponding `.sty` files, if available.

    """
    def replace_style_file(match):
        command = match.group(1)  # Command type
        if command in ['import', 'includefrom', 'subincludefrom']:
            path = match.group(2)
            filename = match.group(3)
            file_path = Path(dir) / path / filename
        else:
            filename = match.group(2)
            file_path = Path(dir) / filename
        # Ensure we are only processing .sty files
        if not file_path.suffix:
            file_path = file_path.with_suffix('.sty')
        
        if file_path.suffix != '.sty':
            # If it's not a .sty file, return the original command
            return match.group(0)
        # # Add .sty extension if not already present
        # if not file_path.suffix:
        #     file_path = file_path.with_suffix('.sty')
        try:
            # Read and return the contents of the style file
            with open(file_path, 'r', encoding='utf-8') as file:
                return f"% Start of included style file: {file_path.name}\n" + file.read() + f"\n% End of included style file: {file_path.name}"
        except FileNotFoundError:
            # If the file is not found, keep the original command and issue a warning
            # if file_path.suffix == '.sty':
            #     warnings.warn(f"Style file {file_path} not found. Keeping original command.", UserWarning)
            return match.group(0)

    # Regex pattern to match all relevant commands for style files
    pattern = r'\\(usepackage|input)\{([^}]+)\}|\\(import|includefrom|subincludefrom)\{([^}]+)\}\{([^}]+)\}'
    
    # Replace all matches in the document
    return re.sub(pattern, replace_style_file, document)
