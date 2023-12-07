#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict()
    for key, item in a_dictionary.items():
        new[key] = item * 2
    return new
