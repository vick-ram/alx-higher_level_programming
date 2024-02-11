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
        self.__width = value

    @property
    def height(self):
        """defines height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        self.__height = value

    @property
    def x(self):
        """defines private x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        self.__x = value

    @property
    def y(self):
        """defines private y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of the y"""
        self.__y = value
