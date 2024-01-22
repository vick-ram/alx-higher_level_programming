#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if x > 0:
                print(i, end='')
                x -= 1
                count += 1
        print()
    except TypeError:
        pass
    return count
