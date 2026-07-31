#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raise an exception because area() is not implemented."""
        raise Exception("area() is not implemented")
