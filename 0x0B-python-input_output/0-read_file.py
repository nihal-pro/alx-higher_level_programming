#!/usr/bin/python3
"""
read_file : a function that reads file (UTF8)
    and print it to stdout.
"""


def read_file(filename=""):
    """Args:
        filename (str): a file name or path of file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
