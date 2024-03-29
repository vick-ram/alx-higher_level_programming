#!/usr/bin/python3
"""2-is_same_class module"""


def is_same_class(obj, a_class):
    """
    Function to check if an object is exactly
    an instance of the specified class.
    Args:
        obj: Any object.
        a_class: Any class.
    Returns:
        True if the object is exactly an instance of
        the specified class; otherwise False.
    """
    return type(obj) is a_class
