"""Adjust formatting for text from LaTeX files to be more usable by Markdown files for `Obsidian.md`"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/31_latex.formatting.ipynb.

# %% auto 0
__all__ = ['DEFAULT_NUMBERED_ENVIRONMENTS', 'MATH_MODE_DELIMITERS', 'BEGIN_END_EQUATIONLIKE_ENV',
           'REPLACE_BACKTICK_AND_APOSTROPHE_QUOTES', 'REMOVE_COMMENTS', 'INLINE_MATHMODE_TO_OWN_PARAGRAPH',
           'MERGE_MULTILINE_PARAGRAPH', 'is_number', 'custom_commands', 'regex_pattern_detecting_command',
           'replace_command_in_text', 'replace_commands_in_text', 'replace_commands_in_latex_document',
           'adjust_common_syntax_to_markdown']

# %% ../../nbs/31_latex.formatting.ipynb 2
import re
from typing import Union

import regex

from trouver.helper.files_and_folders import (
    text_from_file
)
from ..helper.regex import inline_latex_indices, separate_indices_from_str
from .comments import remove_comments
from .preamble import divide_preamble 


# %% ../../nbs/31_latex.formatting.ipynb 4
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

# %% ../../nbs/31_latex.formatting.ipynb 6
DEFAULT_NUMBERED_ENVIRONMENTS = ['theorem', 'corollary', 'lemma', 'proposition',
                                 'definition', 'conjecture', 'remark', 'example',
                                 'question']

# %% ../../nbs/31_latex.formatting.ipynb 11
def _argument_detection(group_num: int) -> str:
    """
    Helper function to `regex_pattern_detecting_command`, and `_commands_from_def`

    This basically helps detect balanced curly braces for invocations of commands.
    """
    return "\{((?>[^{}]+|\{(?1)\})*)\}".replace("1", str(group_num))

# %% ../../nbs/31_latex.formatting.ipynb 12
def custom_commands(
        preamble: str, # The preamble of a LaTeX document.
        ) -> list[tuple[str, int, Union[str, None], str]]: # Each tuple consists of 1. the name of the custom command 2. the number of parameters 3. The default argument if specified or `None` otherwise, and 4. the display text of the command.
    """
    Return a dict mapping commands (and math operators) defined in `preamble` to
    the number of arguments display text of the commands.

    Assumes that the newcommands only have at most one default parameter (newcommands with
    multiple default parameters are not valid in LaTeX).

    Ignores all comented newcommands.
    """
    preamble = remove_comments(preamble)
    latex_commands = _commands_from_newcommand_and_declaremathoperator(preamble)
    tex_commands = _commands_from_def(preamble)
    return latex_commands + tex_commands


def _commands_from_newcommand_and_declaremathoperator(
        preamble: str, # The preamble of a LaTeX document
        ) -> list[tuple[str, int, Union[str, None], str]]: # Each tuple consists of 1. the name of the custom command 2. the number of parameters 3. The default argument if specified or `None` otherwise, and 4. the display text of the command.
    """
    Get custom commands from invocations of `\newcommand` and `DeclareMathOperator`
    in the preamble.

    Helper function to `custom_commands`
    """
    # newcommand_regex = regex.compile(
    #     r'(?<!%)\s*\\(?:(?:re)?newcommand|DeclareMathOperator)\s*\{\\\s*(\w+)\s*\}\s*(?:\[(\d+)\]\s*(?:\[(\w+)\])?)?\s*\{((?>[^{}]+|\{(?4)\})*)\}', re.MULTILINE)
    newcommand_regex = regex.compile(
        r'(?<!%)\s*\\(?:(?:re)?newcommand|DeclareMathOperator)\s*(?:\{\\\s*(\w+)\s*\}|\\\s*(\w+))\s*(?:\[(\d+)\]\s*(?:\[(\w+)\])?)?\s*\{((?>[^{}]+|\{(?5)\})*)\}', re.MULTILINE)

    commands = []
    for match in newcommand_regex.finditer(preamble):
        name_surrounded_in_parentheses = match.group(1) # e.g. \newcommand{\A}
        name_without_parentheses = match.group(2) # e.g. \newcommand\A
        num_args = match.group(3)
        optional_default_arg = match.group(4)
        definition = match.group(5)

        if name_surrounded_in_parentheses is not None:
            name = name_surrounded_in_parentheses
        else:
            name = name_without_parentheses

        # Convert the number of arguments to an integer, if it was specified
        if num_args is not None:
            num_args = int(num_args)
        else:
            num_args = 0

        commands.append((name, num_args, optional_default_arg, definition))
    return commands


def _commands_from_def(
        preamble: str
        ) -> list[tuple[str, int, Union[str, None], str]]: # Each tuple consists of 1. the name of the custom command 2. the number of parameters 3. The default argument if specified or `None` otherwise, and 4. the display text of the command.
    """
    """
    def_command_identifying = r'(?<!%)\s*\\def\s*'
    command_name_identifying = r'\\\s*(\w+)\s*'
    command_def = _argument_detection(2)
    def_regex = regex.compile(
        f"{def_command_identifying}{command_name_identifying}{command_def}"
    )
    return [(match.group(1), 0, None, match.group(2))
            for match in def_regex.finditer(preamble)]


# %% ../../nbs/31_latex.formatting.ipynb 15
def regex_pattern_detecting_command(
        command_tuple: tuple[str, int, Union[None, str], str], # Consists of 1. the name of the custom command 2. the number of parameters 3. The default argument if specified or `None` otherwise, and 4. the display text of the command.
        ) -> regex.Pattern:
    """Return a `regex.pattern` object (not a `re.pattern` object) detecting
    the command with the specified number of parameters, optional argument,
    and display text.

    Assumes that the curly braces used to write the invocations of the commands
    are balanced and properly nested. Assumes that there are no two commands
    of the same name.
    """
    command_name, num_parameters, optional_arg, _ = command_tuple
    backslash_name = fr"\\{command_name}"
    optional_argument_detection = fr"(?:\[(.*?)\])?" if optional_arg is not None else ""
    if optional_arg is not None:
        trailing_arguments = [_argument_detection(i) for i in range(2, 1+num_parameters)]
        trailing_args_pattern = "\\s*".join(trailing_arguments)
        pattern = (f"{backslash_name}\\s*{optional_argument_detection}\\s*{trailing_args_pattern}")
    elif num_parameters > 0:
        arguments = [_argument_detection(i) for i in range(1, 1+num_parameters)]
        args_pattern = "\\s*".join(arguments)
        pattern = f"{backslash_name}\\s*{args_pattern}"
    else:
        # Match the command name exactly without letters immediately following
        # (but underscores following are okay).
        pattern = f"{backslash_name}(?![^\W_])"
    return regex.compile(pattern)

    

# %% ../../nbs/31_latex.formatting.ipynb 17
def replace_command_in_text(
        text: str,
        command_tuple: tuple[str, int, Union[None, str], str], # Consists of 1. the name of the custom command 2. the number of parameters 3. The default argument if specified or `None` otherwise, and 4. the display text of the command.
    ):
    """
    Replaces all invocations of the specified command in `text` with the display text
    with the arguments used in the display text.

    Assumes that '\1', '\2', '\3', etc. are not part of the display text. 
    """
    command_name, num_parameters, optional_arg, display_text = command_tuple
    command_pattern = regex_pattern_detecting_command(command_tuple)
    replace_pattern = display_text.replace('\\', r'\\')
    # if optional_arg is not None:
    #     replace_pattern = replace_pattern.replace('#1', optional_arg)
    replace_pattern = re.sub(r'#(\d)\b', r'\\\1', replace_pattern)
    text = regex.sub(
        command_pattern,
        lambda match: _replace_command(match, command_tuple, command_pattern, replace_pattern),
        text)
    return text


def _replace_command(
        match: regex.match,
        command_tuple: tuple[str, int, Union[None, str], str],
        command_pattern: regex.Pattern,
        replace_pattern: re.Pattern) -> str:
    """
    Replace the matched command with the display text
    
    This is a helper function to `replace_command_in_text`.
    """
    command_name, num_parameters, optional_arg, display_text = command_tuple
    start, end = match.span()
    matched_string_to_replace = match.string[start:end]
    if len(match.groups()) > 0 and match.group(1) is None:
        replace_pattern = replace_pattern.replace(r'\1', optional_arg)
        replaced_string = regex.sub(command_pattern, replace_pattern, matched_string_to_replace)
        return replaced_string
    else:
        return regex.sub(command_pattern, replace_pattern, matched_string_to_replace)


# def _replace_nonexplicit_instances_of_command(
#         text: str,
#         command_tuple: tuple[str, int, Union[None, str], str], # Consists of 1. the name of the custom command 2. the number of parameters 3. The default argument if specified or `None` otherwise, and 4. the display text of the command.
#     ) -> str:
#     """
#     Replace the nonexplicitly instances of a custom command. 

#     Sometimes, a LaTeX command is used nonexplicitly, i.e. the arguments are not
#     explicitly typed with surrounding curly braces `{}`.  An example of this phenomenon
#     is a command named `\til` defined by `\newcommand{\til}[1]{{\widetilde{#1}}}`
#     that is later invoked using `$\til \calh_g$`.

#     This function is only a workaround.

#     This is a helper function to `replace_command_in_text`.
#     """



# %% ../../nbs/31_latex.formatting.ipynb 20
def replace_commands_in_text(
        text: str, # The text in which to replace the commands. This should not include the preamble of a latex document.
        command_tuples: tuple[str, int, Union[None, str], str], # An output of `custom_commands`. Each tuple Consists of 1. the name of the custom command 2. the number of parameters 3. The default argument if specified or `None` otherwise, and 4. the display text of the command.
        repeat: int = 1 # The number of times to repeat replacing the commands throughout the text; note that some custom commands could be "nested", i.e. the custom commands are defined in terms of other custom commands. Defaults to `1`, in which custom commands are replaced throughout the entire document once. If set to -1, then this function attempts to replace custom commands until no commands to replace are found. 
    ) -> str:
    """
    Replaces all invocations of the specified commands in `text` with the
    display text with the arguments used in the display text.

    Assumes that '\1', '\2', '\3', etc. are not part of the display text. 

    If `repeat` is set to `-1`, then this function attempts to replace
    custom commands until no commands to replace are found. However, this
    might cause infinite loops for some documents.

    """
    while repeat != 0:
        old_text = text
        for command_tuple in command_tuples:
            text = replace_command_in_text(text, command_tuple)
        repeat -= 1
        if old_text == text:
            break
    return text

# %% ../../nbs/31_latex.formatting.ipynb 25
def replace_commands_in_latex_document(
        document: str,
        repeat: int = 1 # The number of times to repeat replacing the commands throughout the text; note that some custom commands could be "nested", i.e. the custom commands are defined in terms of other custom commands. Defaults to `1`, in which custom commands are replaced throughout the entire document once. If set to -1, then this function attempts to replace custom commands until no commands to replace are found.  See also `replace_commands_in_text`
        ) -> str:
    """Return the latex document (with the preamble) with invocations
    of custom commands/operators replaced with their display text.

    Assumes that all custom commands and operators are defined in the
    preamble.

    Assumes that, if commands with the same name are defined multiple times,
    only the finally defined command is used. 

    Even replaces these invocations incommented out text.
    """
    preamble, document = divide_preamble(document)
    commands = custom_commands(preamble)
    # Note that `command_tuple[0]` is the name of the command.
    # print(commands)
    unique_commands = {command_tuple[0]: command_tuple for command_tuple in commands} 
    document = replace_commands_in_text(document, list(unique_commands.values()), repeat)
    # for _, command_tuple in unique_commands.items():
    #     document = replace_command_in_text(document, command_tuple)
    return document
    

# %% ../../nbs/31_latex.formatting.ipynb 29
def _replace_math_mode_delimiters(text: str):
    """Helper function to `adjust_common_syntax_to_markdown."""
    text = re.sub(r'\\\(|\\\)', '$', text)
    text = re.sub(r'\\\[|\\]', '$$', text)
    return text


def _replace_equationlike_envs(text: str):
    """Helper function to `adjust_common_syntax_to_markdown."""
    text = re.sub(r'(\\begin\{(?:align|displaymath|equation|eqnarray)\*?\})', r'$$\1', text)
    text = re.sub(r'(\\end\{(?:align|displaymath|equation|eqnarray)\*?\})', r'\1$$', text)
    return text


def _replace_backtick_and_apostrophe_quotes(text: str):
    """Helper function to `adjust_common_syntax_to_markdown."""
    text = re.sub(r"``(.*?)''", r'"\1"', text, flags=re.DOTALL)
    return text



# %% ../../nbs/31_latex.formatting.ipynb 30
def _inline_mathmode_to_own_paragraph(text: str):
    """Add newlines before and after inline mathmode strings in `text`
    if necessary so that each inline mathmode string has at least one
    blank line before and after.

    Also delete one blank space character `' '` from the text immediately
    before and after the in-line math mode string if they exist.

    Helper function to `adjust_common_syntax_to_markdown.
    """
    parts = _separate_inline_latex(text)
    for i in range(len(parts)-1):
        part, next_part = parts[i], parts[i+1]
        if part.endswith('$$') and _starts_with_less_than_two_newlines(next_part):
            next_part = _remove_one_blank_space_if_exists(next_part, 'start')
            parts[i+1] = _make_start_with_two_newlines(next_part)
        if next_part.startswith('$$') and _ends_with_less_than_two_newlines(part):
            part = _remove_one_blank_space_if_exists(part, 'end')
            parts[i] = _make_end_with_two_newlines(part)
    return ''.join(parts)


def _separate_inline_latex(
        text: str
        ) -> list[str]: # Each str is a substring of `text`, either an inline mathmode string or a substring in between the inline mathmode strings.
    """Divide `text` into parts along the inline mathmode strings
    along the inline mathmode strings.

    Invoking `"".join(output)` where `output` is an output to this
    function should recover `text`.

    If `text` starts with an inline-mathmode string, then the
    outputted list starts with the empty string `''`.

    Helper function to `_inline_mathmode_to_own_paragraph.
    """
    indices = inline_latex_indices(text)
    return separate_indices_from_str(text, indices)


def _starts_with_less_than_two_newlines(text: str):
    """Helper function to `_inline_mathmode_to_own_paragraph`."""
    return bool(re.match('(?!\n\n)', text))


def _ends_with_less_than_two_newlines(text: str):
    """Helper function to `_inline_mathmode_to_own_paragraph`."""
    return not text.endswith('\n\n')

def _make_start_with_two_newlines(text: str):
    """Helper function to `_inline_mathmode_to_own_paragraph`."""
    if text.startswith('\n'):
        return f'\n{text}'
    else:
        return f'\n\n{text}'


def _make_end_with_two_newlines(text: str):
    """Helper function to `_inline_mathmode_to_own_paragraph`."""
    if text.endswith('\n'):
        return f'{text}\n'
    else:
        return f'{text}\n\n'


def _remove_one_blank_space_if_exists(
        text: str,
        start_or_end: str #'start' or 'end'
        ):
    """Remove one blank space character `' '` from either the start or
    end of `text` if such a character exists.

    Helper function to `_inline_mathmode_to_own_paragraph`.
    """
    if start_or_end == 'start':
        if text.startswith(' '):
            return text[1:]
    else:
        if text.endswith(' '):
            return text[:-1]
    return text


# %% ../../nbs/31_latex.formatting.ipynb 33
def _merge_multilines(text: str):
    """Helper function to `adjust_common_syntax_to_markdown."""
    # TODO: account for enumerate and itemizes
    parts = _separate_inline_latex(text)
    modified_parts = [_merge_multilines_for_non_mathmode_part(part) for part in parts]
    return ''.join(modified_parts)


def _merge_multilines_for_non_mathmode_part(text: str):
    """Merge multiple lines (semantically making up a paragraph)
    in `text` into a single line.
    
    Does not merge inline-mathmode strings into single-lines,
    but rather leaves such strings unaffected.
    
    Helper function to `_merge_multilines`.
    """
    if text.startswith('$$'):
        return text
    leading_whitespaces, stripped, trailing_whitespaces = _strip_and_return_whitespaces(text)
    lines = stripped.splitlines()
    new_lines = [[]]
    # new_lines = []
    for line in lines:
        if _is_special_line(line) or line.strip() == '':
            new_lines.append([]) 
        new_lines[-1].append(line)
    new_lines = [(' '.join(group).strip()) for group in new_lines]
    # new_lines = [line for line in new_lines if line.strip() != '']
    main = "\n\n".join(new_lines)
    return f'{leading_whitespaces}{main.strip()}{trailing_whitespaces}'


def _is_special_line(line: str):
    """Helper function to `_merge_multilines."""
    stripped = line.strip()
    return (stripped.startswith('\\begin')
            or stripped.startswith('\\section') 
            or stripped.startswith('\\subsection')
            or stripped.startswith('\\subsubsection')
            or stripped.startswith('\\item')
            # or line.strip().startswith('$$')
            )

def _strip_and_return_whitespaces(
        text: str) -> tuple[str, str, str]: # The leading whitespaces, the sripped string, and the trailing whitespaces 
    """
    Strip `text` and return the leading and trailing whitespaces as well.

    Helper function to `_merge_multilines.
    """
    lstripped = text.lstrip()
    leading_whitespaces = text[:-len(lstripped)]
    rstripped = text.rstrip()
    trailing_whitespaces = text[len(rstripped):]
    return leading_whitespaces, text.strip(), trailing_whitespaces

# %% ../../nbs/31_latex.formatting.ipynb 35
# TODO: give the option to replace emph with `****`, e.g. ``\emph{special}``.
# TODO: get everything that is tabbed to the left.
# TODO: merge multi-line text into singular lines.
# TODO: replace enumerated environments with markdown enumerated lists
# TODO: replace \ref's with links and numbers if in mathmode.
# and itemizes with markdown bulleted lists

MATH_MODE_DELIMITERS = 'math_mode_delimiters'
BEGIN_END_EQUATIONLIKE_ENV = 'begin_end_equationlike_env'
REPLACE_BACKTICK_AND_APOSTROPHE_QUOTES = 'replace_backtick_and_apostrophe_quotes'
REMOVE_COMMENTS = 'remove_comments'
INLINE_MATHMODE_TO_OWN_PARAGRAPH = 'inline_mathmode_to_own_paragraph'
MERGE_MULTILINE_PARAGRAPH = 'merge_multiline_paragraph'
def adjust_common_syntax_to_markdown(
        text: str,  # The LaTeX code to adjust to Markdown.
        options: list[str] = [
            MATH_MODE_DELIMITERS,
            BEGIN_END_EQUATIONLIKE_ENV,
            REPLACE_BACKTICK_AND_APOSTROPHE_QUOTES,
            REMOVE_COMMENTS,
            INLINE_MATHMODE_TO_OWN_PARAGRAPH,
            MERGE_MULTILINE_PARAGRAPH,
            ],  # Each `str` specifies what formatting should be done.
        ) -> str:
    """
    Adjust some common syntax, such as math mode delimiters and equation/align
    environments, for Markdown.

    Assumes that the tokens for math mode delimiters (e.g. `\( \)` and `\[ \]`)
    are not used otherwise.

    The following lists admissible parameters in the `options` parameter and
    the effects that including them have:

    - `"math_mode_delimiters"`
        - Replace `\( \)` as math mode delimiters with `$ $`.
        - Replace `\[ \]` as math mode delimiters with `$$ $$`.
    - `"begin_end_equationlike_env"`
        - Replace `\\begin{...} \end{...}` with `$$\\begin{...} \end{...}$$`
          and `\\begin{...*} \end{...*}` with `$$\\begin{...*} \end{...*}$$` for
          the following environments:
            - `align`
            - `displaymath`
            - `equation`
            - `eqnarray`
    - `"replace_backtick_and_apostrophe_quotes"`
        - replace ` `` ''` as quotation delimiters with `" "`.
    - `"remove_comments"`
        - remove LaTeX comments.
    - `"inline_mathmode_to_own_paragraph"`
        - Make it so that each inline-math mode string (of the form `$$...$$`)
          has at least one newline before and after it. Also delete one blank
          space character `' '` from the text immediately before and after the
          in-line math mode string if they exist.
    - `"merge_multiline_paragraph"`
        - Some writers will type paragraphs in multiple lines, likely because
          their LaTeX editor of choice does not wrap text within a single
          line. Including this option merges "normal" paragraphs into a single
          line. 
            - Inline-mathmode text are not affected by this option.
    """
    if MATH_MODE_DELIMITERS in options:
        text = _replace_math_mode_delimiters(text)
    if BEGIN_END_EQUATIONLIKE_ENV in options:
        text = _replace_equationlike_envs(text)
    if REPLACE_BACKTICK_AND_APOSTROPHE_QUOTES in options:
        text = _replace_backtick_and_apostrophe_quotes(text)
    if REMOVE_COMMENTS in options:
        text = remove_comments(text)
    if INLINE_MATHMODE_TO_OWN_PARAGRAPH in options:
        text = _inline_mathmode_to_own_paragraph(text)
    if MERGE_MULTILINE_PARAGRAPH in options:
        text = _merge_multilines(text)
    return text
