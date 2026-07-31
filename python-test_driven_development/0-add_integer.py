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
        TypeError: if a or b is not an int or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("a must be an integer") if isinstance(a, bool) \
            else TypeError("b must be an integer")
    return int(a) + int(b)
