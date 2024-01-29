#!/usr/bin/python3
"""a function that adds 2 integers."""


def add_integer(a, b=98):
    """return an int: addition of a ans b"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
