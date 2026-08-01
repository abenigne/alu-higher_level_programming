#!/usr/bin/python3
"""Unittests for Base class."""
import unittest
from models.base import Base


class TestBaseInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)


class TestBaseToJsonString(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid_list(self):
        list_dicts = [{'id': 12}]
        self.assertEqual(Base.to_json_string(list_dicts), '[{"id": 12}]')

    def test_to_json_string_returns_string(self):
        list_dicts = [{'id': 12}]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual(type(json_str), str)


if __name__ == "__main__":
    unittest.main()
