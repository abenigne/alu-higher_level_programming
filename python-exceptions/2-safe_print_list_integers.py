#!/usr/bin/python3
"""Print and count integers from a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print first x integers found in my_list, return count printed."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
