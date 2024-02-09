#!/usr/bin/python3
"""Module"""


def is_kind_of_class(obj, a_class):
    """
    If obj is an instance or inherited instance of a_class - True.
    Otherwise - False.
    """

    return isinstance(obj, a_class)
