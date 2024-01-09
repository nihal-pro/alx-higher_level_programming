#!/usr/bin/python3
""" a function that ckeck same class """


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj (object): an object.
        a_class : name of class
    Return: True if had same object or inherited, otherwise False.
    """
    return isinstance(obj, a_class)
