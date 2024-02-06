#!/usr/bin/python3
import json
"""4-from_json_string module"""


def from_json_string(my_str):
    """Function that returns an object(python data
    structure) represented by JSON string
    Parameters:
        my_str (str): - string
    """
    return json.loads(my_str)
