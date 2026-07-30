#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Represent a list with an additional sorted-print method."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
