#!/usr/bin/python3
"""Module"""


def write_file(filename="", text=""):
    """ writes a string to a text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        num = f.write(text)
    return num
