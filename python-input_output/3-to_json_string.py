#!/usr/bin/python3
"""Defines a function that converts an object to a JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object.

    Args:
        my_obj: The Python object to serialize.

    Returns:
        str: The JSON representation of my_obj.
    """
    return json.dumps(my_obj)
