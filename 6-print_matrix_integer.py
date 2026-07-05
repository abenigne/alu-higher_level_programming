#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        elements = ["{:d}".format(number) for number in row]
        print(" ".join(elements))
