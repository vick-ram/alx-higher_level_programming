#!/usr/bin/python3
"""2-append_write module"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file
    Parameters:
        filename (str): - file name
        text (str): - text file
    """
    with open(filename, 'a', encoding='utf-8') as af:
        append_file = af.write(text)
        return append_file
