#!/usr/bin/python3
"""Create base module"""

import json
import csv
import turtle


class Base:
    """Create class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Create object of the class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): List of dictionaries.

        If list_dictionaries is None or  an empty list return '[]'.
        Overwrite json string.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        str_dict = json.dumps(list_dictionaries)
        return str_dict

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances to be saved.

        If list_objs is None, save an empty list.
        Overwrite the file if it already exists.
        """
        _list = []
        if list_objs is not None:
            for obj in list_objs:
                _list.append(obj.to_dictionary())

        filename = f"{cls.__name__}.json"
        json_str = cls.to_json_string(_list)

        with open(filename, "w") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        Args:
            json_string (str): string representing a list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set based on
            the provided dictionary.
        Args:
            **dictionary: a double pointer to a dictionary

        Return:
            Instance of the class with attributes set.
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        load from file.
        Return:
            a list of instances.
        """
        filename = f"{cls.__name__}.json"
        _list = []
        try:
            with open(filename, "r") as file:
                read_json_str = file.read()
                _list2 = cls.from_json_string(read_json_str)
                for _l in _list2:
                    _list.append(cls.create(**_l))
                return _list
        except FileNotFoundError:
            return _list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        That serializes in CSV.

        Agrs:
            list_objs (list) : a list of object.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w") as file:
            writer = csv.writer(file)
            if list_objs is not None or len(list_objs) > 0:
                if cls.__name__ is "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ is "Square":
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(file, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
            else:
                file.write('[]')

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, 'r') as file:
                if cls.__name__ is "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ is "Square":
                    fields = ['id', 'size', 'x', 'y']
                reader = csv.DictReader(file, fieldnames=fields)
                dcts = [dict([k, int(v)] for k, v in _l.items())
                        for _l in reader]
                return [cls.create(**dct) for dct in dcts]
        except FileNotFoundError:
            return []

    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares.
        Args:
            list_rectangles (list): a list of rectangle instances.
            list_squares (list): a list of square instances.
        """
        t = turtle.Turtle()
        t.screen.bgcolor('#000000')
        t.shape('turtle')
        t.color('#ffffff')
        t.penup()
        t.goto(-200, 200)
        for rect in list_rectangles:
            t.goto(t.xcor() + (rect.width + 20), t.ycor() - (rect.height + 20))
            t.up()
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.penup()

        t.goto(-200, -20)
        for squ in list_squares:
            t.goto(t.xcor() + (squ.width + 20), t.ycor() - (squ.height + 20))
            t.up()
            t.down()
            for i in range(2):
                t.forward(squ.width)
                t.left(90)
                t.forward(squ.height)
                t.left(90)
            t.penup()
        t.Screen().exitonclick()
