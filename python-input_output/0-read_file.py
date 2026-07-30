#!/usr/bin/python3
"""Defines a function that reads and prints a text file's content."""


def read_file(filename=""):
    """Read a UTF8 text file and print its content to stdout.

    Args:
        filename (str): The path of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
