#!/usr/bin/python3
"""This module only contains a single class that
defines a private instance variabble of a class
"""
class Square(object):
    """This class
    Square only defines a private instance variable
    """

    def __init__(self, size):
        """This init method
        The __init__ method fires first when the class is instantiated
 
        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Args:
            size (int): size param
 
          """
        self.__size = size
