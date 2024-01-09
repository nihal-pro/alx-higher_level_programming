#!/usr/bin/python3
""" a function that ckeck same class """


def is_same_class(obj, a_class):
    """
    Args:
        obj (object): an object.
        a_class : name of class
    Return: True if had same type, otherwise False.
    """
    return type(obj) is a_class
