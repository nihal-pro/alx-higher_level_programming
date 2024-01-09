#!/usr/bin/python3
""" a function that ckeck subclasses """


def inherits_from(obj, a_class):
    """
    Args:
        obj (object): an object.
        a_class : name of class
    Return: True if it inherited, otherwise False.
    """
    return isinstance(obj, a_class) and not type(obj) is a_class
