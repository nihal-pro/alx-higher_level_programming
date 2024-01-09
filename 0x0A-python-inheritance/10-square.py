#!/usr/bin/python3
""" Square module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define Square"""

    def __init__(self, size):
        """initialized atribute"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
