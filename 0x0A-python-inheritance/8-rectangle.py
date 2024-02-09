#!/usr/bin/python3
"""Module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""

    def __init__(self, width, height):
        """validate and initialize width and height
        Args:
            width (int): private
            height (int): private
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
