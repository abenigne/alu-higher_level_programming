#!/usr/bin/python3
"""This module defines the Base class, the parent of all other classes
in this project.
"""
import json


class Base:
    """Base class that manages the id attribute for all future classes
    and avoids duplicating the same code (and bugs).
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The identity of the new instance.
                If None, __nb_objects is incremented and used as id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: "[]" if list_dictionaries is None or empty, otherwise
                the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.

        Args:
            json_string (str): A JSON string representing a list of dicts.

        Returns:
            list: The Python list represented by json_string, or an
                empty list if json_string is None or empty.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.

        Args:
            dictionary (dict): Key/value pairs of attributes to set.

        Returns:
            An instance of cls with attributes set from dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <Class name>.json.

        Returns:
            list: A list of instances of cls, or an empty list if the
                file <Class name>.json does not exist.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
