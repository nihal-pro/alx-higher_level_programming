#!/usr/bin/python3
"""
load_from_json_file: a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Args:
        filename (str): a name of file or path
    """
    with open(filename, "r", encoding="utf-8") as file:
        new_obj = json.load(file)
    return new_obj
