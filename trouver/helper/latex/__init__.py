"""Helper functions for latex functionalities"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/47_helper.latex.ipynb.

# %% auto 0
__all__ = ['REGEX_PATTERN_DETECTIONS', 'temp_dict', 'extract_latex_commands', 'extract_commands_from_nodes',
           'detect_incorrect_latex_commands', 'detect_unbalanced_environments',
           'math_mode_string_is_syntactically_valid', 'reduce_unnecessary_spaces', 'fix_autogen_formatting',
           'correct_latex_syntax_error']

# %% ../../../nbs/47_helper.latex.ipynb 3
import re
from typing import Callable, Union

from Levenshtein import distance
from pylatexenc.latexwalker import LatexCharsNode, LatexEnvironmentNode, LatexNode, LatexWalker, LatexMacroNode

from .. import sublist_generator
from ..regex import latex_indices, replace_string_by_indices
from .macros_and_commands import regex_pattern_detecting_command

# %% ../../../nbs/47_helper.latex.ipynb 9
def _does_not_end_with_script(s):
    """
    This is a helper function to `math_mode_string_is_syntactically_valid`.
    `s` is not supposed to have math mode delimits
    """
    s = s.strip(' $')
    return not s.endswith('_') and not s.endswith('^')

# %% ../../../nbs/47_helper.latex.ipynb 11
def _is_balanced_braces(s):
    """
    This is a helper function to `math_mode_string_is_syntactically_valid`.

    Note that curly braces (`{`, `}`) that have 
    """
    stack = []
    escaped = False
    
    for _, char in enumerate(s):
        if char == '\\':
            escaped = True
        elif char == '{' and not escaped:
            stack.append(char)
        elif char == '}' and not escaped:
            if not stack:
                return False
            stack.pop()
        else:
            escaped = False
    
    return len(stack) == 0


# %% ../../../nbs/47_helper.latex.ipynb 13
def _detect_backslash_space_curly(
        text: str
        ) -> bool:
    """
    Return `True` if there is some backslash `\` followed
    by spaces and then followed by curly brackets `{`

    Note that the presence of such a combination of text
    will induce a syntax error in LaTeX math mode string.

    This is a helper function of `math_mode_string_is_syntactically_valid`
    """
    pattern = r'\\\s+[{}]'
    match = re.search(pattern, text)
    return bool(match)

# %% ../../../nbs/47_helper.latex.ipynb 15
def _is_left_right_balanced(
        latex_string: str
        ) -> bool:
    """
    Return `True` if occurrences of `\left` and `\right` are balanced. 

    This is a helper function of `math_mode_string_is_syntactically_valid`

    This function does not test whether occurrences of the
    appropriately corresponding braces are balanced. For instance,
    the function would return `True` on the input `\left . \right)`.
    Compare against `_is_semantically_left_right_balanced`, which
    is a similar function that tests whether left-right braces
    are "semantically" balanced.
    """
    # Remove all whitespace from the string
    latex_string = ''.join(latex_string.split())
    
    # Find all \left and \right commands
    left_commands = re.findall(r'\\left', latex_string)
    right_commands = re.findall(r'\\right', latex_string)
    
    # Check if the number of \left and \right commands are equal
    if len(left_commands) != len(right_commands):
        return False
    
    # Check if \left always comes before \right
    left_indices = [m.start() for m in re.finditer(r'\\left', latex_string)]
    right_indices = [m.start() for m in re.finditer(r'\\right', latex_string)]
    
    for left, right in zip(left_indices, right_indices):
        if left > right:
            return False
    
    return True



    # # Dictionary to store counts of left and right commands for each brace type
    # brace_counts = {
    #     '(': 0, ')': 0,
    #     '[': 0, ']': 0,
    #     '{': 0, '}': 0,
    #     '|': 0,
    #     '\\|': 0,
    #     '\\{': 0, '\\}': 0,
    #     '.': 0  # For \left. and \right.
    # }
    
    # # Regular expression to match \left and \right commands
    # pattern = r'\\(left|right)(\(|\)|\[|\]|{|}|\||\\\||\\{|\\}|\.)'
    
    # # Find all matches in the latex_string
    # matches = re.finditer(pattern, latex_string)
    
    # for match in matches:
    #     command, brace = match.groups()
    #     if command == 'left':
    #         brace_counts[brace] += 1
    #     elif command == 'right':
    #         brace_counts[brace] -= 1
    
    # # Check if all counts are zero (balanced)
    # return all(count == 0 for count in brace_counts.values()) 

# %% ../../../nbs/47_helper.latex.ipynb 17
def _is_semantically_left_right_balanced(
        latex_string: str
        ) -> bool:
    """
    Return `True` if occurrences of `\left` and `\right` macros
    preceding various braces are balanced.

    This is a helper function of `math_mode_string_is_syntactically_clean`

    Compare against `_is_left_right_balanced`, which
    is a similar function that only tests whether left-right
    macros are "syntactically" balanced, without regard to
    the types of braces actually used.
    """
    # Remove all whitespace from the string
    latex_string = ''.join(latex_string.split())
    
    # Define a stack to keep track of opening delimiters
    stack = []
    
    # Define a dictionary to match opening and closing delimiters
    delimiters = {
        '(': ')', '[': ']', '{': '}', '<': '>',
        r'\left(': r'\right)', r'\left[': r'\right]', 
        r'\left{': r'\right}', r'\left<': r'\right>',
        r'\left\{': r'\right\}', r'\left|': r'\right|',
        r'\left\|': r'\right\|', r'\left.': r'\right.',
        r'\left\langle': r'\right\rangle'
    }
    
    # Regular expression to match \left and \right commands with their delimiters
    pattern = r'(\\left[\(\[\{\<\|\.\|]|\\right[\)\]\}\>\|\.\|]|\(|\)|\[|\]|\{|\}|\<|\>)'
    
    # Find all delimiters and \left/\right commands
    tokens = re.findall(pattern, latex_string)
    
    for token in tokens:
        if token.startswith(r'\left') or token in '([{<':
            stack.append(token)
        elif token.startswith(r'\right') or token in ')]}>':
            if not stack:
                return False
            last_open = stack.pop()
            if token != delimiters.get(last_open):
                return False
    
    # If the stack is empty, all delimiters are balanced
    return len(stack) == 0


# %% ../../../nbs/47_helper.latex.ipynb 19
def _has_invalid_left_right_bracket(
        latex_string: str
        ) -> bool:
    """
    Return `True` is there is at least one invalid use of
    a `\left` or `\right` command.

    This is a helper function of `math_mode_string_is_syntactically_valid`
    """
    # Remove all whitespace from the string
    latex_string = ''.join(latex_string.split())
    
    # Define valid brackets for \left and \right
    valid_brackets = [
        r'(', r')',
        r'[', r']',
        r'\(', r'\)', r'\[', r'\]',  # Parentheses and square brackets
        r'\{', r'\}',                # Curly braces (escaped)
        r'<', r'>',                  # Angle brackets
        r'\|',                       # Vertical bar
        r'|',                       # Vertical bar
        r'\\\|',                     # Double vertical bar (escaped)
        r'\.',                       # Dot
        r'.',                       # Dot
        r'\\lfloor', r'\\rfloor',    # Floor brackets
        r'\\lceil', r'\\rceil',      # Ceiling brackets
        r'\\langle', r'\\rangle'     # Angle brackets (commands)
    ]
    
    # Escape special regex characters and join with |
    valid_brackets_pattern = '|'.join(re.escape(b) for b in valid_brackets)
    
    # Pattern to match \left or \right followed by a valid bracket
    valid_pattern = rf'\\(left|right)({valid_brackets_pattern})'
    
    # Find all \left and \right commands
    commands = list(re.finditer(r'\\(left|right)', latex_string))
    
    for command in commands:
        # Check if the command is followed by a valid bracket
        if not re.match(valid_pattern, latex_string[command.start():]):
            # If not, return True and the invalid command
            invalid_part = latex_string[command.start():command.start()+6]  # Adjust slice as needed
            # return True, invalid_part
            return True
    
    # return False, None
    return False

# %% ../../../nbs/47_helper.latex.ipynb 21
def _has_double_script(
        latex_string: str
        ) -> bool:
    """
    Return `True` if there is at least one double superscript
    or double subscript in `latex_string` 

    This function fails to give correct outputs for more
    nuanced texts, such as `r"x^{2}_{3}^{4}"`; while in
    principle, the function should return `True` on this
    input, the actual return value is `False`.

    This is a helper function of `math_mode_string_is_syntactically_valid`
    """
    # Remove all whitespace from the string
    latex_string = ''.join(latex_string.split())
    
    # Function to match balanced braces
    def match_braces(s, start):
        count = 0
        for i, char in enumerate(s[start:], start):
            if char == '{':
                count += 1
            elif char == '}':
                count -= 1
                if count == 0:
                    return i
        return len(s) - 1

    # Find all subscripts and superscripts
    i = 0
    last_script = None
    while i < len(latex_string):
        if latex_string[i] in '^_' and (i == 0 or latex_string[i-1] != '\\'):
            current_script = latex_string[i]
            i += 1
            if i < len(latex_string):
                if latex_string[i] == '{':
                    end = match_braces(latex_string, i)
                    script_content = latex_string[i:end+1]
                    i = end + 1
                else:
                    script_content = latex_string[i]
                    i += 1
                
                if last_script and last_script[0] == current_script:
                    return True
                last_script = (current_script, script_content)
        else:
            if latex_string[i] not in '^_':
                last_script = None
            i += 1

    return False

# %% ../../../nbs/47_helper.latex.ipynb 23
def _has_double_script_literal(
        latex_string: str
        ) -> bool:
    """
    Return `True` if there is at least one double superscript
    or double subscript in `latex_string` by virtue of having
    `__`, `_^`, `^_, `^^`

    This is a helper function of `math_mode_string_is_syntactically_valid`
    """
    for bad_text in ['__', '_^', '^_', '^^']:
        if bad_text in latex_string:
            return True
    return False

# %% ../../../nbs/47_helper.latex.ipynb 25
def _has_unescaped_dollar(s):
    # Pattern explanation:
    # (?<!\\) is a negative lookbehind assertion that ensures the dollar sign is not preceded by a backslash
    # \$ matches a literal dollar sign
    pattern = r'(?<!\\)(\\\\)*\$'
    match = re.search(pattern, s)
    return bool(match)

# %% ../../../nbs/47_helper.latex.ipynb 28
def extract_latex_commands(latex_string):
    # Create a LatexWalker instance
    walker = LatexWalker(latex_string)
    
    # Get the nodes from the LaTeX string
    try:
        nodelist, _, _ = walker.get_latex_nodes()
    except Exception as e:
        print(f"Error parsing LaTeX: {e}")
        return []  # Return an empty list if there's a parsing error
    # Extract commands
    commands = []
    extract_commands_from_nodes(commands, nodelist)
    return commands


def extract_commands_from_nodes(
        commands: list[str],
        nodes: list[LatexNode]
        ):
    """
    This is a helper function to `extract_latex_commands`.
    """
    for node in nodes:
        # If the node is a character node, we skip it
        if isinstance(node, LatexCharsNode):
            continue
        elif isinstance(node, LatexMacroNode):
            commands.append(node.macroname)
            # Check for arguments of the macro node
            for arg in node.nodeargs:
                if arg and not isinstance(arg, LatexCharsNode):
                    if hasattr(arg, 'nodelist'):  # Ensure the argument is not None
                        extract_commands_from_nodes(commands, arg.nodelist)  # Extract from argument nodes
                    elif isinstance(arg, LatexMacroNode):
                        commands.append(arg.macroname)
        # elif isinstance(node, LatexEnvironmentNode):

        elif isinstance(node, LatexEnvironmentNode):
            commands.extend(_detect_begin_and_end_environments(node.latex_verbatim()))
        # If the node has a nodelist, extract commands from it
        if hasattr(node, 'nodelist'):
            extract_commands_from_nodes(commands, node.nodelist)

def _detect_begin_and_end_environments(
        latex_string: str
        ) -> list[str]:
    """
    Return a list of at most two items containing 'begin' if there is a \begin and containing 'end' if there is an \end

    This is a helper function to `extract_latex_commands`.
    """
    # Regular expressions to match \begin and \end with optional spaces
    begin_pattern = r'\\\s*begin'
    end_pattern = r'\\\s*end'
    
    # Initialize an empty result list
    result = []
    
    # Check for \begin
    if re.search(begin_pattern, latex_string):
        result.append('begin')
    
    # Check for \end
    if re.search(end_pattern, latex_string):
        result.append('end')
    
    return result

# %% ../../../nbs/47_helper.latex.ipynb 31
# Some arguments that can be used towards `regex_pattern_detecting_command`
# for some basic latex arguments.
# Note that the last argument doesn't actually matter, because
# we just want to be able to detect uses of comands, see
# `regex_pattern_detecting_commands``
REGEX_PATTERN_DETECTIONS = [
    ('frac', 2, None, None),
    ('binom', 2, None, None),
    ('sqrt', 1, '2', None),
    ('overset', 2, None, None),
    ('underset', 2, None, None),
    ('stackrel', 2, None, None),
    ('dfrac', 2, None, None),
    ('cfrac', 2, None, None),
    ('sideset', 3, None, None),
    ('xrightarrow', 1, None, None),
    ('xleftarrow', 1, None, None),
    ('overline', 1, None, None),
    ('bar', 1, None, None),
    ('arccos', 1, None, None),
    ('arcsin', 1, None, None),
    ('arctan', 1, None, None),
    ('arg', 1, None, None),
    ('atop', 2, None, None),
    ('begin', 1, None, None),
    ('boldsymbol', 1, None, None),
    ('breve', 1, None, None),
    ('check', 1, None, None),
    ('cline', 1, None, None),
    ('cos', 1, None, None),
    ('cosh', 1, None, None),
    ('cot', 1, None, None),
    ('csc', 1, None, None),
    ('dddot', 1, None, None),
    ('ddot', 1, None, None),
    ('dot', 1, None, None),
    ('end', 1, None, None),
    ('exp', 1, None, None),
    ('gcd', 2, None, None),
    ('grave', 1, None, None),
    ('hat', 1, None, None),
    # ('int', '1', None, None),
    ('lcm', 2, None, None),
    # ('left', 1, None, None),
    ('lg', 1, None, None),
    ('lim', 1, None, None),
    ('liminf', 1, None, None),
    ('limsup', 1, None, None),
    ('ln', 1, None, None),
    ('log', 1, None, None),
    ('longdiv', 2, None, None),
    ('lvert', 1, None, None),
    ('mapsto', 1, None, None),
    ('mathbb', 1, None, None),
    ('mathbf', 1, None, None),
    ('mathcal', 1, None, None),
    ('mathfrak', 1, None, None),
    ('mathop', 1, None, None),
    ('mathrm', 1, None, None),
    ('mathscr', 1, None, None),
    ('max', 1, None, None),
    ('min', 1, None, None),
    ('multicolumn', 3, 'center', None),
    ('multirow', 3, None, None),
    ('not', 1, None, None),
    ('oint', 1, None, None),
    ('overbrace', 1, None, None),
    ('overleftarrow', 1, None, None),
    ('overleftrightarrow', 1, None, None),
    ('overrightarrow', 1, None, None),
    # ('prod', 1, None, None),
    # ('right', 1, None, None),
    ('rvert', 1, None, None),
    ('sec', 1, None, None),
    ('section', 1, None, None),
    ('sin', 1, None, None),
    ('sinh', 1, None, None),
    ('stackrel', 2, None, None),
    ('subsection', 2, None, None),
    ('substack', 2, None, None),
    ('subsubsection', 2, None, None),
    # ('sum', 1, None, None),
    ('sup', 1, None, None),
    ('tag', 1, None, None),
    ('tan', 1, None, None),
    ('tanh', 1, None, None),
    ('text', 1, None, None),
    ('textbf', 1, None, None),
    ('textrm', 1, None, None),
    ('tilde', 1, None, None),
    ('underbrace', 1, None, None),
    ('underline', 1, None, None),
    ('underset', 2, None, None),
    ('varliminf', 1, None, None),
    ('varlimsup', 1, None, None),
    ('vec', 1, None, None),
    ('widehat', 1, None, None),
    ('widetilde', 1, None, None),
    ('xrightarrow', 1, None, None),
]
temp_dict = {}
for entry in REGEX_PATTERN_DETECTIONS:
    temp_dict[entry[0]] = entry
REGEX_PATTERN_DETECTIONS = temp_dict



# %% ../../../nbs/47_helper.latex.ipynb 32
def detect_incorrect_latex_commands(
        latex_string: str,
        ) -> bool:
    """
    Return `True` if there is at least one syntactically
    incorrect use of a latex command detected in `latex_string`.

    This is a helper function to `math_mode_string_is_syntactically_valid`.
    """
    commands_in_string = set(extract_latex_commands(latex_string))
    for command in commands_in_string:
        if command not in temp_dict:
            continue
        tuppy = temp_dict[command]
        pattern = regex_pattern_detecting_command(tuppy)
        # Look at each invocation of the command to see if 
        # each invocation is properly used.
        simp_pattern = rf"\\\s*{command}"
        simp_matches = re.finditer(simp_pattern, latex_string)
        # simp_matches = re.findall(simp_pattern, latex_string)
        for match in simp_matches:
            trailing_substring = latex_string[match.start():]
            alt_match = pattern.search(trailing_substring)
            if not alt_match or alt_match.span()[0] != 0:
                return True

        # if not matches and not simp_matches:
        #     continue
        # if len(matches) != len(simp_matches):
        #     return True
    return False

# %% ../../../nbs/47_helper.latex.ipynb 34
def detect_unbalanced_environments(
        latex_string: str) -> list[str]:
    # Define a regex pattern to match \begin{...} and \end{...}
    pattern = r'\\(begin|end)\{([^}]+)\}'
    
    # Stack to keep track of opened environments
    stack = []
    # List to store errors
    errors = []

    # Find all matches in the LaTeX string
    for match in re.finditer(pattern, latex_string):
        command, env_name = match.groups()
        
        if command == 'begin':
            # Push the environment name onto the stack
            stack.append(env_name)
        elif command == 'end':
            # Check if there is a matching begin for this end
            if stack and stack[-1] == env_name:
                stack.pop()  # Match found, pop from stack
            else:
                # Mismatch found, record the error
                errors.append(f"Mismatched \\end{{{env_name}}} at position {match.start()}")

    # If there are any unmatched begin commands left in the stack, report them
    while stack:
        unmatched_env = stack.pop()
        errors.append(f"Unmatched \\begin{{{unmatched_env}}}")

    return errors

# %% ../../../nbs/47_helper.latex.ipynb 36
def math_mode_string_is_syntactically_valid(
        text: str,
        ) -> bool:
    """
    Return `True` if `text` is determined to be syntactically valid
    as a latex str.

    There may be TeX syntax rules beyond the scope of this function.

    Some caveats:

    `text` is allowed to have dollar signs `$` and is also allowed to not have
    dollar signs. Even if `text` does not have dollar signs, this function
    may return `True`. Even if `text` has dollar signs, this function may return
    `False` if the entire string is not a singular math mode string or if the
    dollar signs are not used in a math-mode-valid way.
    """
    # 
    text = text.strip()
    math_mode_indices = latex_indices(text)
    if _has_unescaped_dollar(text):
        if len(math_mode_indices) != 1:
            return False
        if (math_mode_indices[0][0] != 0 or math_mode_indices[0][1] != len(text)):
            return False
    if not _does_not_end_with_script(text):
        return False
    if _detect_backslash_space_curly(text):
        return False
    if not _is_balanced_braces(text):
        return False
    if _has_invalid_left_right_bracket(text):
        return False
    if not _is_left_right_balanced(text):
        return False
    if _has_double_script(text):
        return False
    if _has_double_script_literal(text):
        return False
    if detect_incorrect_latex_commands(text):
        return False
    if bool(detect_unbalanced_environments(text)):
        return False
    return True



# %% ../../../nbs/47_helper.latex.ipynb 51
# def math_mode_string_is_syntactically_clean(
#         text: str,
#         ) -> bool:
#     """
#     Return `True` if `text` is syntactically "clean" as a LaTeX math mode str.
    
#     While the precise meaning of this may be subjective, here we will
#     consider `text` to be clean, assuming that it is syntactically valid, if

#     - It does not have double blackslashes
#     """
#     if r'\\' in text:
#         return False

# %% ../../../nbs/47_helper.latex.ipynb 54
def reduce_unnecessary_spaces(
        text: str,

        ) -> str:
    """
    Return a string modifying `text` by removing spaces which are
    unnecessary for the purposes of considering the string as a 
    LaTeX string.
    """
    pattern = r'([{_^\\()])\s+'
    text = re.sub(pattern, r'\1', text)
    pattern = r'\s+([}_^()])'
    text = re.sub(pattern, r'\1', text)
    return text
    # for char in ['{', '_', '^', '}', '\\']:
    #     text = re.sub(fr'\s*{chr}\s*', chr, text)

# %% ../../../nbs/47_helper.latex.ipynb 57
def fix_autogen_formatting(
        text: str
        ) -> str:
    """Fix some latex formatting issues in an autogenerated text
    """
    text = text.replace(r'\ ', '\\')
    text = text.replace(r'{ ', r'{')
    text = text.replace(r' }', r'}')
    text, _ = re.subn(r'\$\s*([^\$]+?)\s*\$', r'$\1$', text)
    # TODO: do $ <latex_string> $ into $<latex_stinrg>$
    # TODO: if the replacement of r'\ ' by '\\' happesn to
    # make `\` stick to the previous chunk of things
    # (e.g. r'd\in\mathbb{Z}_{\geq 0}`, then give it some
    # space, e.g. r'd \in \mathbb{Z}_{\geq 0}'.
    text = reduce_unnecessary_spaces(text)
    text = _insert_newline_or_spaces_around_latex(text)
    return text


def _insert_newline_or_spaces_around_latex(
        text:  str
        ) -> str:
    """
    Insert spaces or newlines around latex math mode strings inside `text`
    if necessary.
    """
    math_mode_indices = latex_indices(text)
    replacements = []
    for start, end in math_mode_indices:
        math_mode = text[start:end]
        spaces_potentially_added = math_mode
        if not math_mode.startswith('$$'): #starts with exactly one $
            if start != 0 and text[start-1] != ' ':
                spaces_potentially_added = f' {spaces_potentially_added}'
            if end != len(text) and text[end] != ' ':
                spaces_potentially_added = f'{spaces_potentially_added} '
            replacements.append(spaces_potentially_added)
            continue
        if start != 0 and text[start-1] != '\n':
            front_newline_count = 2
        elif start > 1 and text[start-2] != '\n':
            front_newline_count = 1
        else:
            front_newline_count = 0
        spaces_potentially_added = front_newline_count * '\n' + spaces_potentially_added

        if end != len(text) and text[end] != '\n':
            back_newline_count = 2
        elif end < len(text) - 1 and text[end-1] != '\n':
            back_newline_count = 1
        else:
            back_newline_count = 0
        spaces_potentially_added = spaces_potentially_added + '\n'*back_newline_count
        replacements.append(spaces_potentially_added)
    text = replace_string_by_indices(text, math_mode_indices, replacements)
    text = text.replace('$  $', '$ $')
    text = text.replace('$$\n\n\n\n$$', '$$\n\n$$')
    text = text.replace('$$\n\n\n$$', '$$\n\n$$')
    return text

# %% ../../../nbs/47_helper.latex.ipynb 64
def _tokenize_latex_math(
        latex_string: str
        ) -> list[str]:
    """
    Tokenize `latex_string` by the following principles:

    1. A latex command/macro invoked (but not the inputs) is a token.
    2. the special characters ^ { } _ are tokens.
    3. groups of consecutive whitespaces are tokens.
    4. afterwards, all "words" (one or more consecutive non-whitespace non-special characters) are tokens.
    """
    # Define the regex pattern for tokenization
    pattern = r"""
        (\\[a-zA-Z]+)        # Match LaTeX commands (e.g., \alpha, \sum)
        | ([^\\\s^{}_]+)     # Match words (consecutive non-whitespace, non-special characters)
        | ([^\\\s])          # Match special characters (including ^, {, }, _, etc.)
        | (\s+)              # Match groups of consecutive whitespace
    """
    # Use re.findall to find all matches based on the pattern
    tokens = re.findall(pattern, latex_string, re.VERBOSE)
    # Extract the matched groups, filtering out empty strings
    token_list = [token for group in tokens for token in group if token]
    return token_list


# %% ../../../nbs/47_helper.latex.ipynb 66
def _list_of_candidates_from_math_mode_strings(
        main_content: str, # A text of LaTeX code. In practice, this should be the `main content` of an information note, cf. `summarize_notation`.`
        syntax_validation: Callable[str, bool] = math_mode_string_is_syntactically_valid # A test to tell whether a math mode string is syntactically  valid.
        ) -> set[str]:
    """
    Return a substrings from latex math mode strings in `main_content`
    that are syntactically valid .

    None of the elements in the output have delimiters (`$`, `$$`)
    """
    syntactically_valid_substrings = [] 
    math_mode_indices = latex_indices(main_content)
    for start, end in math_mode_indices:
        latex_str = main_content[start:end]
        latex_str = latex_str.strip('$')
        tokenization = _tokenize_latex_math(latex_str)
        for sublist in sublist_generator(tokenization):
            substring = ''.join(sublist)
            if syntax_validation(substring):
                syntactically_valid_substrings.append(substring.strip())
    return set(syntactically_valid_substrings)

# %% ../../../nbs/47_helper.latex.ipynb 69
def _find_closest_match(
        math_mode_text: str,
        replacement_candidates: list[str]
        ) -> Union[str, None]:
    """This is a helper function to `correct_latex_syntax_error`."""
    if not replacement_candidates:
        return None
    # Calculate Levenshtein distance for each candidate
    distances = [(candidate, distance(math_mode_text, candidate)) for candidate in replacement_candidates]
    # Find the candidate with the minimum distance
    closest_match = min(distances, key=lambda x: x[1])
    return closest_match[0]

# %% ../../../nbs/47_helper.latex.ipynb 71
def correct_latex_syntax_error(
        summary: str, # The autogenerated summary
        replacement_candidates: list[str], # A list of candidates to replace. This is expected to be an output of `_list_of_candidates_from_math_mode_strings`
        # min_length_to_replace_math_mode_string: int = 5, # The minimum length that a math mode string needs to be (exclusing delimiting dollar signs `$`, `$$`) in summary in order to be considered for replacement.
        syntax_validation: Callable[str, bool] = math_mode_string_is_syntactically_valid # A test to tell whether a math mode string is syntactically  valid.
        ) -> str:
    """
    Attempt to replace within `summary` a modified version in which
    the syntactically incorrect latex math mode strings are replaced
    with the most closely resembling element of `replacement_candidates`. 
     
    with a modified version in which the
    latex math mode strings within `summary` that are syntactically
    incorrect 

    TODO: consider the possibility that not all math mode str delimiters
    are formatted correctly.
    """
    math_mode_indices = latex_indices(summary)
    replacements = []
    for start, end in math_mode_indices:
        math_mode_text = summary[start:end]
        if syntax_validation(math_mode_text) or not replacement_candidates:
            replacements.append(math_mode_text)
            continue
        delimiter = '$$' if math_mode_text.startswith('$$') else '$'
        replacement = _find_closest_match(math_mode_text, replacement_candidates)
        replacement = f'{delimiter}{replacement}{delimiter}'
        replacements.append(replacement)
    return replace_string_by_indices(summary, math_mode_indices, replacements)


