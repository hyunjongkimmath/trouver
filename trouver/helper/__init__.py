"""Helper functions"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/00_helper.ipynb.

# %% ../../nbs/00_helper.ipynb 2
from __future__ import annotations



# %% auto 0
__all__ = ['substring_generator', 'sublist_generator']

# %% ../../nbs/00_helper.ipynb 4
def substring_generator(input_string: str):
    length = len(input_string)
    for i in range(length):
        for j in range(i + 1, length + 1):
            yield input_string[i:j]


def sublist_generator(input_list: list):
    length = len(input_list)
    for i in range(length):
        for j in range(i + 1, length + 1):
            yield input_list[i:j]
