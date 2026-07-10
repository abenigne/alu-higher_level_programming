#!/usr/bin/python3
"""Safely print x elements of a list."""


def safe_print_list(my_list=[], x=0):
    """Print x elements of my_list, return number actually printed."""
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print()
    return count
