#!/usr/bin/python3
"""3-is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """
    Function to check if an object is an instance of the
    specified class or an instance of a class that inherited
    from the specified class.
    Args:
        obj: Any object.
        a_class: Any class.
    Returns:
        True if the object is an instance of the specified
        class or an instance of a class that inherited from the
        specified class; otherwise False.
    """
    return isinstance(obj, a_class)
