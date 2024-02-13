#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the Square class instances"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the values for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """prints well formatted string of an object"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """a class that assigns attributes"""
        if args:
            attr = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
