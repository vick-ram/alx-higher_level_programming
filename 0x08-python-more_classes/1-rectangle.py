#!/usr/bin/python3


"""This 1-rectangle module"""
class Rectangle:
    """This defines Rectangle that uses getters and setters"""
    def __init__(self, width=0, height=0):
        """This init defines two instances of the class
        width and height and gives them initial value of 0
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
