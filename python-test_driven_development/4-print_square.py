#!/usr/bin/python3
"""Module that defines a function to print a square.

This module provides print_square, which prints a square made
of the '#' character with the given side length.
"""


def print_square(size):
    """Print a square of '#' characters of the given size.

    Args:
        size (int): the side length of the square.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is a negative integer.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
