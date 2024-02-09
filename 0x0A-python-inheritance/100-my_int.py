#!/usr/bin/python3
"""Module"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __eq__(self, other):
        """change operator == to !="""
        return self.real != other

    def __ne__(self, other):
        """change operator != to =="""
        return self.real == other
