#!/usr/bin/python3
"""
Module for add_integer function.
This module contains a function that adds two integers.
If they are not integers or float
"""
def add_integer(a, b=98):
    """
    This function adds two numbers together.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
