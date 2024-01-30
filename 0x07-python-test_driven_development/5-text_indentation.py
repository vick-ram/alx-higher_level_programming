#!/usr/bin/python3
"""
This module 5-text_indentation
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for char in ".:?":
            text = (char + "\n\n").join(
                [i.strip() for i in text.split(char)]
            )
        print(text)
