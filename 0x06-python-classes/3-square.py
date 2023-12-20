#!/usr/bin/python3
""" This is Class squere """


class Square:
    """  This class allows you to create and manipulate square objects """

    def __init__(self, size=0):
        """ Initialize a new Square
            args:
                size (int): The size for new Saquare

            size should be an integer and greate than -1
            raises:
                TypeError: size must be an integer
                ValueError: size must be >= 0
        """
        self._Square__size = size

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """ Class Methode area: returns the current square area"""
        return self._Square__size * self._Square__size
