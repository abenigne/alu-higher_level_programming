#!/usr/bin/python3
"""Defines a Square class with a custom string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square, validated against BaseGeometry rules."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size (width and height) of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the printable representation of the Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
