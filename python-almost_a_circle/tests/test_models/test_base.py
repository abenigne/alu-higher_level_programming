#!/usr/bin/python3
"""Unit tests for the Base class."""
import os
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unit tests for testing instantiation of the Base class."""

    def test_no_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_public(self):
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_id_none(self):
        b = Base(None)
        self.assertIsInstance(b.id, int)

    def test_two_no_id_incremented(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_is_int(self):
        b = Base(12)
        self.assertIsInstance(b.id, int)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Unit tests for testing to_json_string method of the Base class."""

    def test_list_output(self):
        r = Rectangle(10, 7, 2, 8, 5)
        dictionary = [r.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        self.assertEqual(json.loads(json_dictionary), dictionary)

    def test_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_is_string(self):
        r = Rectangle(10, 7, 2, 8, 5)
        dictionary = [r.to_dictionary()]
        self.assertIsInstance(Base.to_json_string(dictionary), str)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])


class TestBase_from_json_string(unittest.TestCase):
    """Unit tests for testing from_json_string method of Base class."""

    def test_valid_json_string(self):
        list_dicts = [
            {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}
        ]
        json_string = json.dumps(list_dicts)
        self.assertEqual(Base.from_json_string(json_string), list_dicts)

    def test_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_is_list(self):
        list_dicts = [
            {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}
        ]
        json_string = json.dumps(list_dicts)
        self.assertIsInstance(Base.from_json_string(json_string), list)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string("[]", "[]")


class TestBase_save_to_file(unittest.TestCase):
    """Unit tests for testing save_to_file method of the Base class."""

    def tearDown(self):
        for f in ("Rectangle.json", "Square.json"):
            try:
                os.remove(f)
            except IOError:
                pass

    def test_file_created(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_file_content_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(json.loads(content), [r.to_dictionary()])

    def test_save_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(json.loads(f.read()), [])

    def test_save_overwrite(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(1, 1)
        Rectangle.save_to_file([r1])
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(json.loads(f.read()), [r2.to_dictionary()])

    def test_save_square(self):
        s = Square(5, 1, 2, 9)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertEqual(json.loads(f.read()), [s.to_dictionary()])

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], [])


class TestBase_load_from_file(unittest.TestCase):
    """Unit tests for testing load_from_file method of the Base class."""

    def tearDown(self):
        for f in ("Rectangle.json", "Square.json"):
            try:
                os.remove(f)
            except IOError:
                pass

    def test_no_file(self):
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_matches_saved(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 3, 4, 5, 6)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(loaded[1].to_dictionary(), r2.to_dictionary())

    def test_loaded_are_instances(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r1])
        loaded = Rectangle.load_from_file()
        self.assertIsInstance(loaded[0], Rectangle)

    def test_load_square(self):
        s1 = Square(5, 1, 2, 9)
        Square.save_to_file([s1])
        loaded = Square.load_from_file()
        self.assertEqual(loaded[0].to_dictionary(), s1.to_dictionary())

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file([])


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unit tests for testing save_to_file_csv method of Base class."""

    def tearDown(self):
        for f in ("Rectangle.csv", "Square.csv"):
            try:
                os.remove(f)
            except IOError:
                pass

    def test_file_created(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        self.assertTrue(os.path.exists("Rectangle.csv"))

    def test_round_trip_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        loaded = Rectangle.load_from_file_csv()
        self.assertEqual(loaded[0].to_dictionary(), r.to_dictionary())

    def test_round_trip_square(self):
        s = Square(5, 1, 2, 9)
        Square.save_to_file_csv([s])
        loaded = Square.load_from_file_csv()
        self.assertEqual(loaded[0].to_dictionary(), s.to_dictionary())

    def test_save_none(self):
        Rectangle.save_to_file_csv(None)
        self.assertEqual(Rectangle.load_from_file_csv(), [])

    def test_save_empty_list(self):
        Rectangle.save_to_file_csv([])
        self.assertEqual(Rectangle.load_from_file_csv(), [])


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unit tests for testing load_from_file_csv method of Base class."""

    def tearDown(self):
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass

    def test_no_file(self):
        self.assertEqual(Rectangle.load_from_file_csv(), [])


class TestBase_create(unittest.TestCase):
    """Unit tests for testing the create method of the Base class."""

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1, 2, 99)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        s1 = Square(3, 1, 2, 99)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(s1.to_dictionary(), s2.to_dictionary())
        self.assertIsNot(s1, s2)


if __name__ == "__main__":
    unittest.main()
