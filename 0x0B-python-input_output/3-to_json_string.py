#!/usr/bin/python3
import json
"""3-to_json_string module"""


def to_json_string(my_obj):
    """Function that returns JSON representation
    of an object string
    Parameters:
        my_obj (str): object
    """
    return json.dumps(my_obj)
