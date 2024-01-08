#!/usr/bin/python3
""" function lookup """


def lookup(obj):
    """
    a function that returns the list of available
        attributes and methods of an object
    """
    return list(dir(obj))
