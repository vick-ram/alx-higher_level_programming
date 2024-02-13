#!/usr/bin/python3
"""base module"""
import json
import csv
import turtle


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

    @staticmethod
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
        else:
            return None
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                data = file.read()
                if data:
                    objects_data = cls.from_json_string(data)
                    return ([cls.create(**obj_data)
                            for obj_data in objects_data])
                else:
                    return []
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
            )
            file.write(json_string)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of Rectangle objects to CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of Rectangle objects from CSV file"""
        filename = cls.__name__ + ".csv"
        rectangles = []
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    id, width, height, x, y = map(int, row)
                    rectangles.append(cls(width, height, x, y, id))
        except FileNotFoundError:
            pass
        return rectangles

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws all the rectangles and squares using Turtle graphics"""
        turtle.speed(0)
        turtle.bgcolor("white")
        turtle.title("Rectangles and Squares")

        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.color("blue")
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.left(90)
                turtle.forward(rectangle.height)
                turtle.left(90)
            turtle.end_fill()

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.color("red")
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)
            turtle.end_fill()

        turtle.done()
