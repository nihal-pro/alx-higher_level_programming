#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) != 0:
        for row in range(len(matrix)):
            for idx in range(len(matrix[row])):
                if idx != len(matrix[row]) - 1:
                    print("{:d}".format(matrix[row][idx]), end=' ')
                else:
                    print("{:d}".format(matrix[row][idx]), end='')
            print("".format())
    else:
        print("".format())
