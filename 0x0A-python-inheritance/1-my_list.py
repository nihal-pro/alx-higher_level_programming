#!/usr/bin/python3
"""
Mylist is a class inherits_ list
"""


class MyList(list):
    """subclass of list"""

    def print_sorted(self):
        """public methods print sorted list"""
        print(sorted(self))
