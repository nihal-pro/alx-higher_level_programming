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

    def to_json(self):
        """ Return dictionary of my class attribute"""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
