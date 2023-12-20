#!/usr/bin/python3
""" This is Class squere """


class Square:
    """  This class allows you to create and manipulate square objects """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize a new Square
            args:
                size (int): The size for new Saquare
                position (tuple) : position of new square
        """
        self.size = size
        self.position = position

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

            Args:
                value (int): The new size for new Square

            Raises:
                TypeError: size must be an integer
                ValueError: size must be >= 0
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self._Square__size = value

    @property
    def position(self):
        """ retrieve the position of position """
        return self._Square__pos

    @position.setter
    def position(self, value):
        """ Set new position for print #

            Args:
                value (Tuple): The new position for print #

            Raises:
                TypeError: position must be a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(elem, int) for elem in value) or
                not all(elem >= 0 for elem in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self._Square__pos = value

    def my_print(self):
        """Class Methode my_print: to print an square of # """
        if self._Square__size == 0:
            print()
            return
        for char in range(self._Square__pos[1]):
            print()
        for char in range(self._Square__size):
            print(" " * self._Square__pos[0], end="")
            print("#" * self._Square__size)

    def __str__(self):
        result = ""
        if self._Square__size == 0:
            return (result)
        for char in range(self._Square__pos[1]):
            result += "\n"
        for char in range(self.size):
            result += " " * self._Square__pos[0] + \
                "#" * self._Square__size + "\n"
        return result[:-1]
