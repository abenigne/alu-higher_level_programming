#!/usr/bin/python3
"""Safely print an integer."""


def safe_print_integer(value):
    """Print value as an integer if possible, return True/False."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
