#!/usr/bin/python3
"""defines a rectangle by: (based on 5-rectangle.py)"""


class Rectangle:
    """defines a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instantiation of rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """return the rectangle area: width * height"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.height)

    def __str__(self):
        """print the rectangle with the character # """
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return rec

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """print message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
