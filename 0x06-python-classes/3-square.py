#!/usr/bin/python3
"""class Square that defines a square by:(based on 2-square.py)"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """Instantiation with size"""
        self.__size = size

        if int(size) < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size * self.__size
