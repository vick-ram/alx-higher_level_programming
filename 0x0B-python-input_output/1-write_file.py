#!/usr/bin/python3
"""1-write_file module"""


def write_file(filename="", text=""):
    """Function writes a string to a text file and
    returns the number of characters written
    Parameters:
        filename (str): - file name
        text (str): - text being written
    """
    with open(filename, 'w', encoding='utf-8') as wf:
        write_file = wf.write(text)
        return write_file
