#!/usr/bin/python3
"""pascal_triange module"""


def pascal_triangle(n):
    """
    Args:
        n (int): The number pascal triangle
    Return: a list od lists of integers
    """

    # check if n less or equal 0 return empty list
    if n <= 0:
        return []
    # add [1] at beggining
    lst = [[1]]
    while len(lst) != n:
        # tri == last list in lists
        tri = lst[-1]
        # start new list with 1
        _l = [1]
        # new element always == two element in last list
        for i in range(len(tri) - 1):
            _l.append(tri[i] + tri[i + 1])
        # end list with 1
        _l.append(1)
        # test print _l print("_l = ", _l)
        lst.append(_l)
        # test print lst print("list = ", lst)
    return lst
