#!/usr/bin/python3
"""
This module contains the definition of the Square class, which represents a square and defines its properties and behavior.
"""

class Square:
    """
    This class represents a square and defines its properties and behavior.

    Attributes:
        size (int): The size of the square.

    Methods:
        area(self): Returns the area of the square.
        my_print(self): Prints the square with the character '#'.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with an optional size.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#'.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
