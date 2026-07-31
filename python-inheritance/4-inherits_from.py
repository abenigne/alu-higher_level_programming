#!/usr/bin/python3
"""Module that defines a function to check inheritance only."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherited from a_class.

    Args:
        obj: the object to check.
        a_class: the class to compare against.

    Returns:
        True if obj is an instance of a class that inherited
        (directly or indirectly) from a_class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
