#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a Square instance"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Square is a Rectangle with the same width and height
        that is why we assigned them to the same value 'size'
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieves the size of the square object"""
        return self.width

    @size.setter
    def size(self, value):
        """sets width and height as size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of a Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Updates attributes with provided arguments and keyword arguments"""
        if args:
            attrs = ["id", "size", "x", "y"]
            i = 0
            for arg in args:
                setattr(self, attrs[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
