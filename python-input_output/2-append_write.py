#!/usr/bin/python3
"""Defines a function that appends text to a file."""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF8 text file.

    Args:
        filename (str): The path of the file to append to.
        text (str): The text to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
