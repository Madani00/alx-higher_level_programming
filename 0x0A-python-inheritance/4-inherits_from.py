#!/usr/bin/python3
"""Module"""


def inherits_from(obj, a_class):
    """
    If obj is an inherited instance of a_class - True.
    Otherwise - False.
    """

    return isinstance(obj, a_class) and type(obj) != a_class
