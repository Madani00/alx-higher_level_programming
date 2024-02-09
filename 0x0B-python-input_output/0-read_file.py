#!/usr/bin/python3
"""Module"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it out"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
