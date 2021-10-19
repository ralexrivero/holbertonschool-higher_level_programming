#!/usr/bin/python3
"""Contains a class `Base`"""


import json
import csv
import os


# 1
class Base:
    """
        define empty class Base

        Attributes:
            id (int): instance attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initializes class and object

            Args:
                id (int): input at object creation
        """
        if type(id) != int and id is not None:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

# 15. Dictionary to JSON string
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

# 16. JSON string to file
    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            data = []
        else:
            data = [i.to_dictionary() for i in list_objs]
        string = cls.to_json_string(data)
        filename = "{}.json".format(cls.__name__)

        with open(filename, encoding="utf-8", mode="w") as f:
            f.write(string)

# 17. JSON string to dictionary
    @staticmethod
    def from_json_string(json_string):
        """Changes json string to a list
        Returns:
            list of dictionaries
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

# 18. Dictionary to Instance
    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

# 19. File to instances
    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        """
        filename = "{}.json".format(cls.__name__)

        try:
            with open(filename, encoding="utf-8") as f:
                string = f.read()
        except FileNotFoundError:
            return []

        json = cls.from_json_string(string)
        instances = [cls.create(**instance) for instance in json]
        return instances

# 21. Let's draw it
    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares
        """

        import time as x
        from random import randrange as r
        import turtle as t

        t.color("white")
        t.bgcolor("white")
        t.shape("circle")
        t.pensize(4)

        for i in (list_rectangles + list_squares):
            t.penup()
            t.setpos(0, 0)
            t.Screen().colormode(255)
            t.pencolor((r(255), r(255), r(255)))
            Base.drawer(t, i)
            x.sleep(1)
        x.sleep(5)

    @staticmethod
    def drawer(t, rect):
        """drawer method
        """

        t.penup()
        t.setpos(rect.x, rect.y)
        t.pendown()
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
