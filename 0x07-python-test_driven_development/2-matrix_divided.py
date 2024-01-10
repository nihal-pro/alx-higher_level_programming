#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    matrix_divided is a function print a matrix divied by div
    Args:
        matrix (list): matrix of int or float
        div (int or float): the divider
    Return: list of listes dvivied by div
    """
    mx_type_err = 'matrix must be a matrix (list of lists) of integers/floats'
    mx_len_err = 'Each row of the matrix must have the same size'
    NewList = []
    len_row = 0

    if type(matrix) is not list or type(matrix) is str:
        raise TypeError(mx_type_err)
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(div) not in (int, float):
        raise TypeError('div must be a number')

    for row in matrix:
        if type(row) is not list:
            raise TypeError(mx_type_err)
        if len(row) is not len_row and len_row != 0:
            raise TypeError(mx_len_err)
        New_row = []
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError(mx_type_err)
            New_row.append(round((elem / div), 2))
        NewList.append(New_row)
        len_row = len(row)
    return NewList
