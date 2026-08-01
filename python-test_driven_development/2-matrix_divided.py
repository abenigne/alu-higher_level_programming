#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
All elements are divided by a given divisor and rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The divisor to divide elements by.

    Returns:
        list: A new matrix with divided and rounded values.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats,
                   or if rows are not of equal size, or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_msg)
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(err_msg)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
