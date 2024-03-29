#!/usr/bin/python3

"""This module only contains a single class that defines
a private instance variabble of a class.
"""


class Square:
    """This class Square only defines a private instance variable."""

    def __init__(self, size):
        """This init method, the __init__ method fires first when
        the class is instantiated

        Args:
            size (int): size param
          """
        self.__size = size
