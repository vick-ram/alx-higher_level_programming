#!/usr/bin/python3
"""
This is 100-square module.
This module defines a Square class that represents a square.
The Square class includes private instance attributes
for size and position, getters and setters for these attributes,
an __init__ method to initialize tha class, an area method to
calculate the area oof the square, and the my_print method to print
the square. Printing a Square instance
should have the same behavior as my_print.
"""


class Square:
    """
    This is the Square class.
    This class defines a square by its size and position.
    The size and position are private instance attributes.
    The class provides getters and setters for these attributes
    to ensure that they meet the necessary conditions.
    The class also provides methods to calculate the area of
    the square and print the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes an instance of the Square class.
        Parameters:
        size (int, optional): The size of the square.
        Defaults to 0. Size must be an integer and must be >= 0.
        position (tuple, optional): The position of the square.
        Defaults to (0, 0). Position must be a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

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
        Parameters:
        value (int): The size of the square.
        Must be an integer and must be >= 0.
        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.
        Returns:
        tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.
        Parameters:
        value (tuple): The position of the square.
        Must be a tuple of 2 positive integers.
        Raises:
        TypeError: If the value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.
        Returns:
        int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character #.
        If size is equal to 0, prints an empty line.
        Uses the position attribute to determine where to print the square.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of the Square that can be printed.
        Returns:
        str: A string representation of the Square.
        """
        if self.__size == 0:
            return ""
        else:
            return ("\n" * self.__position[1]
                    + "\n".join(" " * self.__position[0] + "#"
                    * self.__size for _ in range(self.__size)))
