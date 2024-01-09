#!/usr/bin/python3
"""MyInt module"""


class MyInt(int):
    """define MyInt"""

    def __init__(self, number):
        self.number = number

    def __eq__(self, number2):
        """MyInt has == and != operators inverted"""
        return self.number != number2

    def __ne__(self, number2):
        return self.number == number2
