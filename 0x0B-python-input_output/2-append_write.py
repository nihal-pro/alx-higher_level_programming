#!/usr/bin/python3
"""
append_write : a function that appends
                    at end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """
    Args:
        filename (str): a name of file or path.
        text (str): a text we want to write in file or appends.
    Return: The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as file:
        len_text = file.write(text)
    return len_text
