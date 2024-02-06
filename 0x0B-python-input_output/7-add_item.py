#!/usr/bin/python3
"""7-add_item module"""
import sys
from os import path

if __name__ == "__main__":
    save_to_json_file = \
        __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    filename = 'add_item.json'
    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []
    for arg in sys.argv[1:]:
        my_list.append(arg)
    save_to_json_file(my_list, filename)
