#!/usr/bin/python3
import json
"""6-load_from_json_file module """


def load_from_json_file(filename):
    """Function creates an object from json file
    Parameters:
        filename: - name of file to read from
    """
    with open(filename, 'r', encoded='utf-8') as f:
        return json.load(f)
