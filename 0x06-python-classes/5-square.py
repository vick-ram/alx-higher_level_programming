"""
This is the 5-square module.

This module defines a Square class that represents a square. The Square class includes a private instance attribute for size, a getter and setter for size, an __init__ method to initialize the square, an area method to calculate the area of the square, and a my_print method to print the square.
"""

class Square:
    """
    This is the Square class.

    This class defines a square by its size. The size is a private instance attribute. The class provides a getter and setter for the size attribute to ensure that it is an integer and is not less than 0. The class also provides methods to calculate the area of the square and print the square.
    """

    def __init__(self, size=0):
        """
        Initializes an instance of the Square class.

        Parameters:
        size (int, optional): The size of the square. Defaults to 0. Size must be an integer and must be >= 0.
        """
        self.size = size

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
        value (int): The size of the square. Must be an integer and must be >= 0.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

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
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

