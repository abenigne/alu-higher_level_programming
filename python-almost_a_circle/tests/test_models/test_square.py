#!/usr/bin/python3
"""Unit tests for the Square class."""
import io
import os
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unit tests for testing instantiation of the Square class."""

    def test_is_rectangle(self):
        self.assertIsInstance(Square(3), Rectangle)

    def test_is_base(self):
        self.assertIsInstance(Square(3), Base)

    def test_size_only(self):
        s = Square(5)
        self.assertEqual((s.width, s.height, s.x, s.y), (5, 5, 0, 0))

    def test_size_x(self):
        s = Square(5, 2)
        self.assertEqual((s.width, s.height, s.x, s.y), (5, 5, 2, 0))

    def test_size_x_y(self):
        s = Square(5, 2, 3)
        self.assertEqual((s.width, s.height, s.x, s.y), (5, 5, 2, 3))

    def test_size_x_y_id(self):
        s = Square(5, 2, 3, 99)
        self.assertEqual(s.id, 99)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_size_type(self):
        with self.assertRaises(TypeError):
            Square("5")

    def test_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_size_negative(self):
        with self.assertRaises(ValueError):
            Square(-5)

    def test_x_type(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_type(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)


class TestSquare_size(unittest.TestCase):
    """Unit tests for testing the size property of the Square class."""

    def test_size_getter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))

    def test_size_setter_invalid_type(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "10"

    def test_size_setter_invalid_value(self):
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = 0


class TestSquare_area(unittest.TestCase):
    """Unit tests for testing the area method of the Square class."""

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)


class TestSquare_display(unittest.TestCase):
    """Unit tests for testing the display method of the Square class."""

    def test_display_no_offset(self):
        s = Square(2)
        captured = io.StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")


class TestSquare_str(unittest.TestCase):
    """Unit tests for testing __str__ method of the Square class."""

    def test_str(self):
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")


class TestSquare_update_args(unittest.TestCase):
    """Unit tests for testing update method (args) of the Square class."""

    def test_update_no_args(self):
        s = Square(10, 10, 10, 1)
        s.update()
        expected = {"id": 1, "size": 10, "x": 10, "y": 10}
        self.assertEqual(s.to_dictionary(), expected)

    def test_update_all_args(self):
        s = Square(10, 10, 10, 1)
        s.update(89, 1, 2, 3)
        expected = {"id": 89, "size": 1, "x": 2, "y": 3}
        self.assertEqual(s.to_dictionary(), expected)


class TestSquare_update_kwargs(unittest.TestCase):
    """Unit tests for testing update method (kwargs) of Square class."""

    def test_update_kwargs(self):
        s = Square(10, 10, 10, 1)
        s.update(size=1, x=2, y=3, id=89)
        expected = {"id": 89, "size": 1, "x": 2, "y": 3}
        self.assertEqual(s.to_dictionary(), expected)

    def test_update_partial_kwargs(self):
        s = Square(10, 10, 10, 1)
        s.update(size=5)
        self.assertEqual(s.size, 5)


class TestSquare_save_to_file(unittest.TestCase):
    """Unit tests for testing save_to_file method of the Square class."""

    def tearDown(self):
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")


class TestSquare_to_dictionary(unittest.TestCase):
    """Unit tests for testing to_dictionary method of the Square class."""

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 9)
        expected = {"id": 9, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)

    def test_to_dictionary_is_dict(self):
        s = Square(10, 2, 1, 9)
        self.assertIsInstance(s.to_dictionary(), dict)


if __name__ == "__main__":
    unittest.main()
