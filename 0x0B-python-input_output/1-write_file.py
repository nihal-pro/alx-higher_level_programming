#!/usr/bin/python3
"""
write_file : a function that write text in file (UTF8)
"""


def write_file(filename="", text=""):
    """
    Args:
        filename (str): a name of file or path.
        text (str): a text we want to write in file
    Return: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        len_text = file.write(text)
    return len_text
