#!/usr/bin/python3
"""Defines a function that converts an object's attributes to a dict."""


def class_to_json(obj):
    """Return the dictionary description of an object for serialization.

    Args:
        obj: An instance of a class whose attributes are all
            JSON-serializable (list, dict, str, int, bool).

    Returns:
        dict: The attribute dictionary of obj.
    """
    return obj.__dict__
