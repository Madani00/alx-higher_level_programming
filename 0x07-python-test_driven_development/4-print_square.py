#!/usr/bin/python3
"""function that prints a square with the character #"""


def print_square(size):
    """size is the size length of the square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("{}".format("#"), end="")
        print()
