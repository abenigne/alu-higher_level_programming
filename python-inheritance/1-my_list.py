#!/usr/bin/python3
"""Module that defines a class MyList which inherits from list."""


class MyList(list):
    """Class that inherits from list and adds sorted printing."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
