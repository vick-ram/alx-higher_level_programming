#!/usr/bin/python3
"""100-my_int module"""


class MyInt(int):
    """
    A class representing an integer with
    inverted equality operators.

    """
    def __eq__(self, other):
        """
        Inverted equality operator (==).
        Args:
            other: The object to compare with.
        Returns:
            bool: True if not equal; False otherwise.

        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverted inequality operator (!=).
        Args:
            other: The object to compare with.
        Returns:
            bool: True if equal; False otherwise.

        """
        return super().__eq__(other)
