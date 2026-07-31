#!/usr/bin/python3
"""Module that defines a function to check exact class matching."""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class.

    Args:
        obj: the object to check.
        a_class: the class to compare against.

    Returns:
        True if type(obj) is exactly a_class, otherwise False.
    """
    return type(obj) == a_class
