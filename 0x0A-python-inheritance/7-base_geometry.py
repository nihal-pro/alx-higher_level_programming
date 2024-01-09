#!/usr/bin/python3
"""
This module contains a class that defines a rectangle.
"""


class BaseGeometry:
    """Defines a BaseGeometry"""

    def area(self):
        """Method: raises an Exception with the message
            area() is not implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validation value"""
        if not isinstance(value, int):
            str_err = "{:s} must be an integer".format(name)
            raise TypeError(str_err)
        if value <= 0:
            str_err = "{:s} must be greater than 0".format(name)
            raise ValueError(str_err)
