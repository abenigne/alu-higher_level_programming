#!/usr/bin/python3
"""
This module provides a function to format text with newlines after specific characters.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text (str): The text string to format and print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = True
    for char in text:
        if skip_space and char == ' ':
            continue
        skip_space = False
        print(char, end="")
        if char in ['.', '?', ':']:
            print("\n")
            skip_space = True
