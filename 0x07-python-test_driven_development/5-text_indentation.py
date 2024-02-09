#!/usr/bin/python3
"""
prints text with 2 new lines after each ".", "?", and ":"
"""


def text_indentation(text):
    """
    text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    rvs = "\n".join(list_lines)
    print(rvz, end="")
