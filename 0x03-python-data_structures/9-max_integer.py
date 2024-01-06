#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    for i in my_list:
        if i > len(my_list[0:-1]):
            return i
