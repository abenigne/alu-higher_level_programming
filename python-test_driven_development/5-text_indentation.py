#!/usr/bin/python3
"""Module that defines a function to print indented text.

This module provides text_indentation, which prints text with
two new lines added after each '.', '?' and ':' character.
"""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'.

    Args:
        text (str): the text to print.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special = (".", "?", ":")
    result = ""
    for char in text:
        if char == " " and (len(result) == 0 or result[-1] == "\n"):
            continue
        result += char
        if char in special:
            result += "\n\n"
    print(result.strip())
