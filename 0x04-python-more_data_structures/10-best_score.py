#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) != 0:
        big, key = int(0), ""
        for k, i in a_dictionary.items():
            if big < i:
                big, key = i, k
        return key
