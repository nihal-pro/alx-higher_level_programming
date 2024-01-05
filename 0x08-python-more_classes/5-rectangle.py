#!/usr/bin/python3
"""
This module contains a class that defines a rectangle.
"""


class Rectangle:
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Sets the necessary attributes for the Rectangle object.
        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return: Rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return: Rectangle area"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return: The print behavior of the Rectangle object."""
        res = ""
        if self.__width == 0 or self.__height == 0:
            return res
        for _ in range(self.__height):
            res += "#" * self.__width + "\n"
        return res[:-1]

    def __repr__(self):
        """Return: The repr behavior of the Rectangle object."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """the del behavior of the Rectangle object."""
        print('Bye rectangle...')
