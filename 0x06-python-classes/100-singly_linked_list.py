#!/usr/bin/python3
"""
This is 100-singly_linked_list.

This module defines a Node class of a singly linked list. It has private instance attribute data, and property attribute method data, and also has private instance next_node with method also defined
"""

class Node:
    """
    This is the Node class.

    This class defines a node of a singly linked list. The node has a private instance attribute for data and next_node. The class provides getters and setters for these attributes to ensure that they meet the necessary conditions.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes an instance of the Node class.

        Parameters:
        data (int): The data stored in the node. Must be an integer.
        next_node (Node, optional): The next node in the linked list. Defaults to None. Can be None or must be a Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data of the node.

        Returns:
        int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node.

        Parameters:
        value (int): The data of the node. Must be an integer.

        Raises:
        TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node of the current node.

        Returns:
        Node: The next node of the current node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node of the current node.

        Parameters:
        value (Node): The next node of the current node. Can be None or must be a Node.

        Raises:
        TypeError: If the value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This is the SinglyLinkedList class.

    This class defines a singly linked list. The linked list has a private instance attribute for the head of the list. The class provides a method to insert a new Node into the correct sorted position in the list and a method to print the entire list.
    """

    def __init__(self):
        """
        Initializes an instance of the SinglyLinkedList class.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.

        Parameters:
        value (int): The data of the new Node. Must be an integer.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the SinglyLinkedList.

        Returns:
        str: A string representation of the SinglyLinkedList.
        """
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return "\n".join(values)

