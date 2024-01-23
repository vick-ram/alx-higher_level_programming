#!/usr/bin/python3
"""
This is the 3-square module.

This module defines a Square class that represents a square. The Square class includes private instance attributes for size, an __init__ method to initialize the square, an area method to calculate the area of the square, and a my_print method to print the square.
"""

class Square:
    """
    This class represents a square and defines its properties and behavior.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance with an optional size.
        area(self): Returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with an optional size.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
