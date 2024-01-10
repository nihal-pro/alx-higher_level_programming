#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Function add two integer or float otherwise print error in TypeError
    Args:
        a (int or float): first number.
        b (int or float): second number.
    Return: The Addition of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    else:
        try:
            a = int(a)
        except Exception:
            raise TypeError('a must be an integer')

    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    else:
        try:
            b = int(b)
        except Exception:
            raise TypeError('b must be an integer')
    return a + b
