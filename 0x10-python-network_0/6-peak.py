#!/usr/bin/python3
"""function that found peak"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers.
        i use binary search algorithm, recursive.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            # Move towards the right (larger neighbor)
            left = mid + 1
        else:
            # Move towards the left (larger neighbor)
            right = mid

    return list_of_integers[left]
