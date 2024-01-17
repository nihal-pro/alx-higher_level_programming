#!/usr/bin/python3
"""Create square that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Create class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Create object of the class square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """return integer size of square"""
        return self.height

    @size.setter
    def size(self, value):
        """set value to the size"""
        self.width = value
        self.height = value

    def __str__(self):
        '''return string'''
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.size)
