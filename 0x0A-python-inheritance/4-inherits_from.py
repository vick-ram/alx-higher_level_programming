#!/usr/bin/python3
"""4-inherits_from module"""

def inherits_from(obj, a_class):
    """
    Function to check if an object is an instance of a
    class that inherited (directly or indirectly)
    from the specified class.
    Args:
        obj: Any object.
        a_class: Any class.
    Returns:
        True if the object is an instance of a class that
        inherited from the specified class; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
