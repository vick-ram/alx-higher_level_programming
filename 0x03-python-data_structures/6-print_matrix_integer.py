#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_str = ""
        for i in range(len(row)):
            row_str += "{:d}".format(row[i])
            if i < len(row) - 1:
                row_str += " "
        print(row_str)
