#!/usr/bin/python3
"""Defines a function that loads an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create a Python object from the content of a JSON file.

    Args:
        filename (str): The path of the JSON file to read.

    Returns:
        The Python data structure represented by the file's content.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
