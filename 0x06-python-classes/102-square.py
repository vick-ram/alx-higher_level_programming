#!/usr/bin/python3
"""
This is 102-square module.
This module defines a Square class that represents a square.
The Square class includes private instance attributes
for size and position, getters and setters for these
attributes, an __init__ method to initialize the square,
an area method to calculate the area of the square.
Also includes a checker to ensure that the size is a
number(float or integer) and is not less than 0.
"""


class Square:
    """
    This is the Square class.
    This class defines a square by its size.
    The size is a private instance attribute.
    The class provides a getter and setter for the size
    attribute to ensure that it is a number (float or integer)
    and is not less than 0. The class also provides a method to
    calculate the area of the square. The Square instance can answer
    to comparators: ==, !=, >, >=, < and <= based on the square area.
    """

    def __init__(self, size=0):
        """
        Initializes an instance of the Square class.
        Parameters:
        size (number, optional): The size of the square.
        Defaults to 0. Size must be a number (float or integer)
        and must be >= 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        Returns:
        number: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        Parameters:
        value (number): The size of the square.
        Must be a number (float or integer) and must be >= 0.
        Raises:
        TypeError: If the value is not a number (float or integer).
        ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.
        Returns:
        number: The area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() != other.area()

    def __lt__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()

    def __gt__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()
