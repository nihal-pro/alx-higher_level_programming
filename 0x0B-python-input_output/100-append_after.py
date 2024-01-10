#!/usr/bin/python3
"""
append_after:  a function that inserts a line of text to a file,
                after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Argv:
        filename (str): a name of file
        search_string (str): a string that want to search for.
        new_string (str): a new string.
    """
    # add new empty string
    NewText = ""
    # open file with read and write
    with open(filename, "r") as file:
        # divided line
        for line in file:
            # add line
            NewText += line
            # if search_string in line add new string
            if search_string in line:
                NewText += new_string
    # close file and open with write to overwrite file
    with open(filename, "w") as file:
        file.write(NewText)
