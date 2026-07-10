#!/usr/bin/python3
"""Divide two lists element by element."""


def list_division(my_list_1, my_list_2, list_length):
    """Return a new list with element-wise division results."""
    new_list = []
    for i in range(list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            pass
    return new_list
