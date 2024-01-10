#!/usr/bin/python3
"""
import:
    sys and function that save and load list
script:
    This script adds all arguments to a Python list,
        and then save them to a file:
    Name file fix : `add_item.json`.
    If the file doesn t exist, it should be created.

"""
import json
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

if (len(argv) > 1):
    try:
        # if file exit.
        obj = load_from_json_file(filename)
    except Exception:
        # else create it empty list.
        obj = []
    # add all argument start with 1
    for i in range(1, len(argv)):
        obj.append(argv[i])
    # update list in json file
    save_to_json_file(obj, filename)
