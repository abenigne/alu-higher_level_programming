#!/usr/bin/python3
"""Module that defines a function to check instance or inheritance."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or a subclass of it.

    Args:
        obj: the object to check.
        a_class: the class to compare against.

    Returns:
        True if obj is an instance of a_class or any class that
        inherited from a_class, otherwise False.
    """
    return isinstance(obj, a_class)
