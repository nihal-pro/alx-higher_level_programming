#!/usr/bin/python3
"""Create Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Create class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Create object of the class Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieve The width of Rectangle.
        Return: an integer of the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """retrieve The width of Rectangle.
        Return: an integer of the width."""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """retrieve The height of Rectangle.
        Return: an integer of the height."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """retrieve The x of Rectangle.
        Return: an integer of the x."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """retrieve The y of Rectangle.
        Return: an integer of the y."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''return area'''
        return self.__width * self.__height

    def display(self):
        '''display #'''
        for _ in range(self.__height):
            print("#" * self.__width)
