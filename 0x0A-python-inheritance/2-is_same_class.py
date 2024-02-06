#!/usr/bin/python3
"""Module"""


def is_same_class(obj, a_class):
    """
    Function Doc

    Args:
        obj (obj): object 1
        a_class (obj): object 2

    Return:
        True if obj is exactly an instance of the specified class
    """

    return type(obj) is a_class
