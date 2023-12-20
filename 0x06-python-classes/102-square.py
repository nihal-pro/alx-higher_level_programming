#!/usr/bin/python3
""" This is Class squere """


class Square:
    """  This class allows you to create and manipulate square objects """

    def __init__(self, size=0):
        """ Initialize a new Square
            args:
                size (int): The size for new Saquare
        """
        self.size = size

    def area(self):
        """ Class Methode area: returns the current square area"""
        return self._size * self._size

    @property
    def size(self):
        """ retrieve the size of sauare
            Return: an integer of the size
        """
        return self._size

    @size.setter
    def size(self, value):
        """ Set new size for Sauare

            args:
                value (int): The new size for new Square

            raises:
                TypeError: size must be an integer
                ValueError: size must be >= 0
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self._size = value

    def __eq__(self, compare):
        return self._size == compare._size

    def __lt__(self, compare):
        return self._size < compare._size

    def __le__(self, compare):
        return self._size <= compare._size

    def __gt__(self, compare):
        return self._size > compare._size

    def __ge__(self, compare):
        return self._size >= compare._size
