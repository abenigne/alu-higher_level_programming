#!/usr/bin/python3
"""Defines a function that writes text to a file."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file, creating or overwriting it.

    Args:
        filename (str): The path of the file to write to.
        text (str): The text to write into the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
