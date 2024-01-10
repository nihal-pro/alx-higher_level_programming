#!/usr/bin/python3
"""
save_to_json_file: a function that writes an Object to a text file,
        using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj (str): a json string.
        filename (str): a name of file or path
    """
    with open(filename, "w", encoding="utf-8") as file:
        js = json.dumps(my_obj)
        file.write(js)
