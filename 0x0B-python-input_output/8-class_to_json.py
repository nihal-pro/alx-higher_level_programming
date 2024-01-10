#!/usr/bin/python3
"""
class_to_json: a function that returns the dictionary
    description with simple data structure (list, dictionary,
    string, integer and boolean) for JSON serialization of an object:
"""


def class_to_json(obj):
    """
    Args:
        obj (class): The name and number.
    Return:  the dictionary description
    """
    new_dict = {}
    # start loop of all attribute in this object.
    for attr in dir(obj):
        # to show attr => print(attr)
        if not callable(getattr(obj, attr)) and not attr.startswith("__"):
            # void all attr start with  __ => print("---> ", attr)
            new_dict[attr] = getattr(obj, attr)
    return new_dict
