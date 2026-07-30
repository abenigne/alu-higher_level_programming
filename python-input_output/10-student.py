#!/usr/bin/python3
"""Defines a Student class with a filterable JSON representation."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        Args:
            attrs (list): Optional list of attribute names to include.
                If not a list, all attributes are included.

        Returns:
            dict: The (optionally filtered) attributes of the Student.
        """
        if isinstance(attrs, list) and all(isinstance(a, str)
                                            for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
