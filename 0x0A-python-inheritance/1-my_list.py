#!/usr/bin/python3
"""module 1-my_list"""


class MyList(list):
    """a class MyList that inherits from list"""

    def print_sorted(self):
        """Print a list in sorted ascending sort"""
        print(sorted(self))
