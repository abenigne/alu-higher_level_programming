#!/usr/bin/python3
"""Divide two integers safely."""


def safe_print_division(a, b):
    """Divide a by b, print result inside finally, return result."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
