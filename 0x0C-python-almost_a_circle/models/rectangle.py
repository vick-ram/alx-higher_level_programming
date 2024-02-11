#!/usr/bin/python3
from models.base import Base
"""rectangle module"""


class Rectangle(Base):
    """Rectangle class that defines private width
    and height and public ones, also same to x and y
    cordinates
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the private instance attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    """defines the width"""
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """defines height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """defines private x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """defines private y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of the y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def area(self):
        """computes the area and returns result"""
        return self.__width * self.__height

    @property
    def display(self):
        """prints in stdout the Rectangle instance
        with the character
        """
        for _ in range(self.height):
            print('#' * self.width)
