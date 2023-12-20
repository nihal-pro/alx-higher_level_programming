#!/usr/bin/python3
""" This is Class squere """


class Square:
    """  This class allows you to create and manipulate square objects """

    def __init__(self, size=0):
        """ Initialize a new Square
            args:
                size (int): The size for new Saquare
        """
        self._Square__size = size

    def area(self):
        """ Class Methode area: returns the current square area"""
        return self._Square__size * self._Square__size

    @property
    def size(self):
        """ retrieve the size of sauare
            Return: an integer of the size
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        """ Set new size for Sauare

            args:
                value (int): The new size for new Square

            raises:
                TypeError: size must be an integer
                ValueError: size must be >= 0
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self._Square__size = value

    def my_print(self):
        """Class Methode my_print: to print an square of # """
        if self.size == 0:
            print()
        for i in range(self.size):
            print("#" * self.size)
