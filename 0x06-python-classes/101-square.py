#!/usr/bin/python3
"""class Square that defines a square by: (based on 6-square.py)"""


class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """to retrieve current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """to set size of square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """return position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """to set position"""
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """return the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """should have the same behavior as my_print()"""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        pieces = []
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
        return "\n".join(pieces)
