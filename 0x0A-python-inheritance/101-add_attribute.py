#!/usr/bin/python3
"""101-add_attribute module"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible.
    Args:
        obj: The object to which the attribute will be added.
        attribute (str): The name of the attribute.
        value: The value to assign to the attribute.
    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
