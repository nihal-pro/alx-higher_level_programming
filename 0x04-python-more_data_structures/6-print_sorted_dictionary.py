#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # for a in sorted(a_dictionary.items()):
    #     for i in a:
    #         print(i, end=" ")
    #     print()
    for key, item in dict(sorted(a_dictionary.items())).items():
        print("{}: {}".format(key, item))
