#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes the Square class instances"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints well formatted string of an object"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))
