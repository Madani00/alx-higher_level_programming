#!/usr/bin/python3
"""defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation of rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """to retrieve width of the rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """to set width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """to retrieve height of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """to set height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
