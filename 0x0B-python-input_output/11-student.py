#!/usr/bin/python3
"""11-student module"""


class Student:
    """
    Class that defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first name,
        last name, and age.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        Args:
            attrs (list of str, optional): A list of attribute
                names to retrieve.
                If specified, only attributes in this
                list will be included in the
                dictionary representation. If None, all attributes
                will be included.
        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            # If attrs is None, include all attributes
            return self.__dict__
        else:
            # If attrs is specified, include only those attributes
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }

    def reload_from_json(self, json_data):
        """
        Replaces all attributes of the Student instance
        with values from a dictionary.
        Args:
            json_data (dict): Dictionary containing attribute values.

        """
        for attr, value in json_data.items():
            setattr(self, attr, value)
