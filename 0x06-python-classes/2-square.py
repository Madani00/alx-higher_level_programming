#!/usr/bin/python3
"""class that defines a square by:(based on 1-square.py)"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """Instantiation with optional size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
