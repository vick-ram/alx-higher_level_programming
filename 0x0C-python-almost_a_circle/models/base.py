#!/usr/bin/python3
"""base module"""
import json


class Base:
    """This is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize the class instances"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation
        list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            json.dumps(list_dictionaries)

    @classmethod
    def from_json_string(cls, json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                return ([cls.create(**obj)
                        for obj in cls.from_json_string(file.read())])
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
            )
            file.write(json_string)
