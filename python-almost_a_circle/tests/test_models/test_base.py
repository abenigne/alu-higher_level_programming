#!/usr/bin/python3
"""Unit tests for the Base class."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for the Base class id-management logic."""

    def test_id_auto_assigned(self):
        """Test that id is auto-assigned when none is given."""
        b1 = Base()
        b2 = Base()
        self.assertIsInstance(b1.id, int)
        self.assertIsInstance(b2.id, int)

    def test_id_auto_assigned_incremented(self):
        """Test that consecutive auto ids increment by one."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_passed_in(self):
        """Test that a passed-in id is saved as-is."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_module_docstring(self):
        """Test that the base module has a docstring."""
        mod = __import__("models.base", fromlist=["base"])
        self.assertIsNotNone(mod.__doc__)

    def test_class_docstring(self):
        """Test that the Base class has a docstring."""
        self.assertIsNotNone(Base.__doc__)

    def test_init_docstring(self):
        """Test that __init__ has a docstring."""
        self.assertIsNotNone(Base.__init__.__doc__)


class TestBaseToJSONString(unittest.TestCase):
    """Tests for Base.to_json_string."""

    def test_to_json_string_none(self):
        """Test to_json_string with None returns '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """Test to_json_string with an empty list returns '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list_of_dicts(self):
        """Test to_json_string with a list containing one dict."""
        result = Base.to_json_string([{'id': 12}])
        self.assertEqual(json.loads(result), [{'id': 12}])

    def test_to_json_string_returns_string(self):
        """Test to_json_string returns a str instance."""
        result = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(result, str)

    def test_to_json_string_docstring(self):
        """Test to_json_string has a docstring."""
        self.assertIsNotNone(Base.to_json_string.__doc__)


class TestBaseFromJSONString(unittest.TestCase):
    """Tests for Base.from_json_string."""

    def test_from_json_string_none(self):
        """Test from_json_string with None returns an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_string(self):
        """Test from_json_string with '[]' returns an empty list."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_valid(self):
        """Test from_json_string with a valid JSON string."""
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(result, [{"id": 89}])

    def test_from_json_string_returns_list(self):
        """Test from_json_string returns a list instance."""
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertIsInstance(result, list)

    def test_from_json_string_docstring(self):
        """Test from_json_string has a docstring."""
        self.assertIsNotNone(Base.from_json_string.__doc__)


class TestBaseSaveToFile(unittest.TestCase):
    """Tests for Base.save_to_file."""

    def tearDown(self):
        """Remove any files created during the tests."""
        for fname in ("Rectangle.json", "Square.json"):
            if os.path.exists(fname):
                os.remove(fname)

    def test_save_to_file_none(self):
        """Test save_to_file(None) writes an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test save_to_file([]) writes an empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_list(self):
        """Test save_to_file with a list of one Rectangle."""
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(content, [r.to_dictionary()])

    def test_save_to_file_square(self):
        """Test save_to_file with a list of one Square."""
        s = Square(1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(content, [s.to_dictionary()])

    def test_save_to_file_docstring(self):
        """Test save_to_file has a docstring."""
        self.assertIsNotNone(Base.save_to_file.__doc__)


class TestBaseCreate(unittest.TestCase):
    """Tests for Base.create."""

    def test_create_rectangle(self):
        """Test Rectangle.create with a full dictionary."""
        d = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r = Rectangle.create(**d)
        self.assertEqual(r.to_dictionary(), d)

    def test_create_square(self):
        """Test Square.create with a full dictionary."""
        d = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s = Square.create(**d)
        self.assertEqual(s.to_dictionary(), d)

    def test_create_docstring(self):
        """Test create has a docstring."""
        self.assertIsNotNone(Base.create.__doc__)


class TestBaseLoadFromFile(unittest.TestCase):
    """Tests for Base.load_from_file."""

    def tearDown(self):
        """Remove any files created during the tests."""
        for fname in ("Rectangle.json", "Square.json"):
            if os.path.exists(fname):
                os.remove(fname)

    def test_load_from_file_no_file(self):
        """Test load_from_file returns [] when the file is missing."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_rectangle(self):
        """Test load_from_file round-trips Rectangle instances."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        for orig, new in zip([r1, r2], loaded):
            self.assertEqual(orig.to_dictionary(), new.to_dictionary())

    def test_load_from_file_square(self):
        """Test load_from_file round-trips Square instances."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 2)
        for orig, new in zip([s1, s2], loaded):
            self.assertEqual(orig.to_dictionary(), new.to_dictionary())

    def test_load_from_file_docstring(self):
        """Test load_from_file has a docstring."""
        self.assertIsNotNone(Base.load_from_file.__doc__)


if __name__ == "__main__":
    unittest.main()
