#!/usr/bin/python3
"""Unit tests for the Base class."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unit tests for the Base class."""

    def test_id_is_public(self):
        """Test that id is a public attribute."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none_increments(self):
        """Test that id is auto-assigned when None."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """Test to_json_string with a list of dictionaries."""
        list_input = [{"id": 1}, {"id": 2}]
        result = Base.to_json_string(list_input)
        self.assertEqual(type(result), str)

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        """Test from_json_string with a valid JSON string."""
        json_str = '[{"id": 1}]'
        self.assertEqual(Base.from_json_string(json_str), [{"id": 1}])

    def test_save_and_load_rectangle(self):
        """Test save_to_file and load_from_file for Rectangle."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        list_output = Rectangle.load_from_file()
        self.assertEqual(len(list_output), 2)
        os.remove("Rectangle.json")

    def test_save_to_file_none(self):
        """Test save_to_file with None saves an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_load_from_file_no_file(self):
        """Test load_from_file when the file doesn't exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_create_rectangle(self):
        """Test create returns an instance with correct attributes."""
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertIsNot(r1, r2)
        self.assertEqual(str(r1), str(r2))

    def test_create_square(self):
        """Test create returns a Square instance with correct attrs."""
        s1 = Square(5, 2, 3, 10)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertIsNot(s1, s2)
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()
