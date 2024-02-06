#!/usr/bin/python3
import json
""""""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.
    Args:
        my_obj: The object to be serialized to JSON.
    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
