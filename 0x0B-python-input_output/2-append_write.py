#!/usr/bin/python3
"""Module"""


def append_write(filename="", text=""):
    """a function that appends """
    with open(filename, "a", encoding="utf-8") as f:
        num = f.write(text)
    return num
