#!/usr/bin/python3
def print_square(size):
    """
    print_square a function that print square from '#'
    Args:
        size (int): a size of square
    Return: Square of # or None
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for row in range(size):
        print("#" * size)
