#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        i = 0
        while True:
            if x > 0:
                try:
                    if isinstance(my_list[i], int):
                        print("{:d}".format(my_list[i]), end='')
                        count += 1
                    i += 1
                except IndexError:
                    break
                x -= 1
            else: 
                break
        print()
    except TypeError:
        pass
    return count
