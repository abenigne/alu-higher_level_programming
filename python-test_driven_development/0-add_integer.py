#!/usr/bin/python3
"""Module that defines a function to add two integers.

This module provides add_integer, a function that adds two
numbers together after validating and casting them appropriately.
"""


def add_integer(a, b=98):
    """Add two integers or floats together.

    Args:
        a (int/float): the first number.
        b (int/float): the second number, defaults to 98.

    Returns:
        int: the sum of a and b, cast to integers.

    Raises:
        TypeError: if a or b is not an int or float, or if either
            cannot be converted to an integer (e.g. NaN, infinity).
    """
    if type(a) not in (int, float) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    try:
        a = int(a)
    except (ValueError, OverflowError):
        raise TypeError("a must be an integer")
    try:
        b = int(b)
    except (ValueError, OverflowError):
        raise TypeError("b must be an integer")
    return a + b
