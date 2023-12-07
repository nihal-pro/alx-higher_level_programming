#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        new_i = []
        for j in i:
            new_i.append(j ** 2)
        new.append(new_i)
    return new
