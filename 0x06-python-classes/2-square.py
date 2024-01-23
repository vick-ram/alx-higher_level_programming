#!/usr/bin/python3
"""This module defines a class that privatizes an instance with error
"""

class Square:
    """Square class defines square"""
    def __init__(self, size=0):
        """initializes the Square class
        Args:
            size (int): Int type param
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
