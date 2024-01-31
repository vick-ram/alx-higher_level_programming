#!/usr/bin/python3
"""9-rectangle.py module"""


class Rectangle:
    """Rectangle function adds functionality of static
    methods
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes class objects width and height and instance
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width self property retriever"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height self property retriever"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """formats a string"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (str(self.print_symbol) * self.__width + "\n") * self.__height

    def __repr__(self):
        """string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """frees python arbage"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares two rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        return rect_1 if area_1 >= area_2 else rect_2

    @classmethod
    def square(cls, size=0):
        """returns the square of the sizes provided"""
        return cls(size, size)
