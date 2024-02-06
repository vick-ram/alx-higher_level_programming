#!/usr/bin/python3
"""6-load_from_json_file module """
import json


def load_from_json_file(filename):
    """Function creates an object from json file
    Parameters:
        filename: - name of file to read from
    """
    with open(filename, 'r') as f:
        return json.load(f)
