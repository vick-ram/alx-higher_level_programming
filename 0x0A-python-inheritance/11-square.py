#!/usr/bin/python3
"""11-square module"""


class BaseGeometry:
    """
    A class representing the base geometry.
    Methods:
        area(self): Raises an Exception with the
        message "area() is not implemented".
        integer_validator(self, name, value): Validates
        the value as an integer.
    """
    def area(self):
        """
        Raises:
            Exception: Always raises an Exception with the
            message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer.
        Args:
            name (str): The name of the value.
            value (int): The value to be validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.
    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    Methods:
        __init__(self, width, height): Initializes a
        rectangle with a given width and height.
        area(self): Calculates the area of the rectangle.
        __str__(self): Returns a string representation of the rectangle.

    """
    def __init__(self, width, height):
        """
        Initializes a rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        Returns:
            str: A string representation of the rectangle.

        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Calculates the area of the rectangle.
        Returns:
            int: The area of the rectangle.

        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    A class representing a square, which is a special case of a rectangle.
    Attributes:
        __size (int): The size of the square.
    Methods:
        __init__(self, size): Initializes a square with a given size.

    """
    def __init__(self, size):
        """
        Initializes a square with a given size.
        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.
        Returns:
            str: A string representation of the square.

        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
