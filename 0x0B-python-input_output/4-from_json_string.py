#!/usr/bin/python3
"""
from_json_string: a function that return
        object (Python data structure) represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Args:
        my_str (str): a json string.
    Return: The object (Python data structure) represented by a JSON string.
    """
    obj = json.loads(my_str)
    return obj
