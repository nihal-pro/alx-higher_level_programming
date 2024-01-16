#!/usr/bin/python3
"""Create Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Create class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Create object of the class Rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        """Getter and setter for Width"""
        @property
        def width(self):
            """retrieve The width of Rectangle.
            Return: an integer of the width."""
            return self.__width
        
        @width.setter
        def width(self, value):
            self.__width = value

        """Getter and setter for height"""
        @property
        def height(self):
            """retrieve The height of Rectangle.
            Return: an integer of the height."""
            return self.__height
        
        @height.setter
        def height(self, value):
            self.__height = value

        """Getter and setter for x"""
        @property
        def x(self):
            """retrieve The x of Rectangle.
            Return: an integer of the x."""
            return self.__x
        
        @x.setter
        def x(self, value):
            self.__x = value
        
        """Getter and setter for y"""
        @property
        def y(self):
            """retrieve The y of Rectangle.
            Return: an integer of the y."""
            return self.__y
        
        @y.setter
        def y(self, value):
            self.__y = value
