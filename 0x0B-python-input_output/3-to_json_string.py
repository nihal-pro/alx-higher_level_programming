#!/usr/bin/python3
"""
to_json_string: a function that return
                    JSON representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Args:
        my_obj (dict): a name of dict.
    Return: The JSON representation of an object (string).
    """
    str_json = json.dumps(my_obj)
    return str_json
