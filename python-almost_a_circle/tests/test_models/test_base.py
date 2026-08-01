#!/usr/bin/python3
"""
Unittest module for testing the Base class.
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def setUp(self):
        """
        Resets the __nb_objects counter before each test.
        """
        Base._Base__nb_objects = 0

    def test_id_auto_increment(self):
        """
        Tests automatic incrementing of id when not provided.
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_explicit(self):
        """
        Tests passing a specific id value.
        """
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """
        Tests converting None to JSON string representation.
        """
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """
        Tests converting empty list to JSON string representation.
        """
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid(self):
        """
        Tests converting list of dicts to JSON string.
        """
        d = [{'id': 1, 'width': 2, 'height': 3, 'x': 0, 'y': 0}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"id": 1, "width": 2, "height": 3, "x": 0, "y": 0}]')

    def test_from_json_string_none(self):
        """
        Tests parsing None from JSON string.
        """
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """
        Tests parsing empty string from JSON string.
        """
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        """
        Tests parsing valid JSON string to list.
        """
        s = '[{"id": 1, "width": 2}]'
        self.assertEqual(Base.from_json_string(s), [{'id': 1, 'width': 2}])


if __name__ == "__main__":
    unittest.main()
