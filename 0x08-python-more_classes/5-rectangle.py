#!/usr/bin/python3
"""
This module defines a Rectangle class for representing rectangles.
"""


class Rectangle:
    """
    A class to represent a rectangle.
    Attributes
    ----------
    width : int
        the width of the rectangle (private)
    height : int
        the height of the rectangle (private)

    Methods
    -------
    area():
        Returns the area of the rectangle.
    perimeter():
        Returns the perimeter of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Constructs a new Rectangle with the given width and height.
        Parameters
        ----------
        width : int, optional
            The width of the rectangle (default is 0)
        height : int, optional
            The height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle.
        Returns
        -------
        int
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        Returns
        -------
        int
            The perimeter of the rectangle,
            or 0 if either the width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the
        rectangle using the '#' character.
        Returns
        -------
        str
            The string representation of the rectangle,
            or an empty string if either the width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join("#" * self.__width for _ in range(self.__height))

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        that can be used to recreate the object using eval().
        Returns
        -------
        str
            The string representation of the rectangle in the
            format 'Rectangle(width, height)'.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """deletes by freeing the garbage"""
        print("Bye rectangle...")
