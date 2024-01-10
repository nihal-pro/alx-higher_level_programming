#!/usr/bin/python3
"""
Student module
"""


class Student:
    """class id Student"""

    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name (str) : first name
            last_name (str): last name
            age (int): age in integer
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return dictionary of my class attribute"""
        if attrs is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        dct = {}
        for attr in attrs:
            if attr in ("first_name", "last_name", "age"):
                dct[attr] = getattr(self, attr)
        return dct
