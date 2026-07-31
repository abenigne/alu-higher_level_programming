#!/usr/bin/python3
"""Module that defines a function to divide all elements of a matrix.

This module provides matrix_divided, which returns a new matrix
whose elements are all divided by a given number, rounded to
2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list): a list of lists of integers or floats.
        div (int/float): the number to divide each element by.

    Returns:
        list: a new matrix with each element divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: if matrix is not a list of lists of int/float,
            if the rows are not all the same size, or if div is
            not a number.
        ZeroDivisionError: if div is equal to 0.
    """
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_matrix)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_matrix)
        for elem in row:
            if type(elem) not in (int, float) or isinstance(elem, bool):
                raise TypeError(err_matrix)
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]
