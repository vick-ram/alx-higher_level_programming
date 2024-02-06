#!/usr/bin/python3
"""8-class_to_json module"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple
    data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization
    of an object.
    Args:
        obj: An instance of a class.
    Returns:
        dict: Dictionary representation of the
        object's serializable attributes.
    """
    serializable_attributes = {}

    for attr, value in obj.__dict__.items():
        # Check if the attribute value is serializable
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_attributes[attr] = value

    return serializable_attributes
