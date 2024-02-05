#!/usr/bin/python3
"""1-my_list module"""


class MyList(list):
    """
    Class MyList that inherits from list.
    """

    def print_sorted(self):
        """
        Method that prints the list in ascending order.
        """
        print(sorted(self))
