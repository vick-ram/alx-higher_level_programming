#!/usr/bin/python3
"""0-read_file module"""


def read_file(filename=""):
    """function that reads a text file and prints to
    stdout
    Parameters:
        filename (str): - file name
    """
    with open(filename, 'r', encoding='utf-8') as f:
        read_data = f.read()
        print(read_data, end='')
