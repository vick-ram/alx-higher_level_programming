#!/usr/bin/python3
"""5-save_to_json_file module"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file,
    using JSON representation
    Parameters:
        my_obj: - an object to write from
        filename: text file to write into
    """
    with open(filename, 'w') as jf:
        return json.dump(my_obj, jf)
