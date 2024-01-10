#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    say_my_name is function that print string
    Args:
        first_name (str): The first name
        last_name (str): The Last name
    Return: My name is <first_name> <last_name>
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print("My name is {:s} {:s}".format(first_name, last_name))
