#!/usr/bin/python3
"""4-from_json_string module"""
import json


def from_json_string(my_str):
    """
    Function that returns an object(python data
    structure) represented by JSON string
    Parameters:
        my_str (str): - string
    Returns:
        object: returns an object(Python data structure)
    """
    return json.loads(my_str)
