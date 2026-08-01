#!/usr/bin/python3
"""This module defines the Square class, which inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle.

    A square is a special rectangle where width and height are equal.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size (width and height) of the square.
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
            id (int): The identity of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """int: The size of the square (its width and height)."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes via no-keyword or keyword arguments.

        Args:
            *args: New attribute values in order: id, size, x, y.
            **kwargs: New attribute values by key/value pair. Skipped
                if args is not empty.
        """
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
