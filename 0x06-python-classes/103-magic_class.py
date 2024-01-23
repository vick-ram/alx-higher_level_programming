#!/usr/bin/python3
"""This is 103-magic_class module"""
import math


class MagicClass:
    """
    This is the MagicClass.
    This class defines a circle by its radius.
    The radius is a private instance attribute.
    The class provides a getter and setter for the radius
    attribute to ensure that it is a number (float or integer)
    and is not less than 0. The class also provides
    methods to calculate the area and circumference of the circle.
    """

    def __init__(self, radius=0):
        """
        Initializes an instance of the MagicClass.
        Parameters:
        radius (number, optional): The radius of the circle. Defaults
        to 0. Radius must be a number (float or integer) and must be >= 0.
        Raises:
        TypeError: If the radius is not a number (float or integer).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.
        Returns:
        float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.
        Returns:
        float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
