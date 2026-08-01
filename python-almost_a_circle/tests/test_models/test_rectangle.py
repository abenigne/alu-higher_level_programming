#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unit tests for testing instantiation of the Rectangle class."""

    def test_is_base(self):
        self.assertIsInstance(Rectangle(2, 3), Base)

    def test_width_height_only(self):
        r = Rectangle(10, 2)
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 2, 0, 0))

    def test_width_height_x(self):
        r = Rectangle(10, 2, 5)
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 2, 5, 0))

    def test_width_height_x_y(self):
        r = Rectangle(10, 2, 5, 6)
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 2, 5, 6))

    def test_width_height_x_y_id(self):
        r = Rectangle(10, 2, 5, 6, 99)
        self.assertEqual(r.id, 99)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_width_type(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_height_type(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_x_type(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "5")

    def test_y_type(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 5, "6")

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_width_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_height_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_height_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -5)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 5, -6)


class TestRectangle_area(unittest.TestCase):
    """Unit tests for testing the area method of the Rectangle class."""

    def test_area(self):
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)

    def test_area_after_update(self):
        r = Rectangle(3, 5)
        r.width = 10
        self.assertEqual(r.area(), 50)

    def test_too_many_args(self):
        r = Rectangle(3, 5)
        with self.assertRaises(TypeError):
            r.area(1)


class TestRectangle_display(unittest.TestCase):
    """Unit tests for testing the display method of the Rectangle class."""

    def test_display_no_offset(self):
        r = Rectangle(2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_with_offset(self):
        r = Rectangle(2, 2, 1, 1)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ##\n ##\n")


class TestRectangle_str(unittest.TestCase):
    """Unit tests for testing __str__ method of the Rectangle class."""

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")


class TestRectangle_update_args(unittest.TestCase):
    """Unit tests for testing update method (args) of Rectangle class."""

    def test_update_no_args(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        expected = {"id": 1, "width": 10, "height": 10, "x": 10, "y": 10}
        self.assertEqual(r.to_dictionary(), expected)

    def test_update_id(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_all_args(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 1, 2, 3, 4)
        expected = {"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}
        self.assertEqual(r.to_dictionary(), expected)


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unit tests for testing update method (kwargs) of Rectangle class."""

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(width=1, height=2, x=3, y=4, id=89)
        expected = {"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}
        self.assertEqual(r.to_dictionary(), expected)

    def test_update_partial_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(width=5)
        self.assertEqual(r.width, 5)

    def test_update_no_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual(r.width, 10)


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unit tests for testing to_dictionary method of Rectangle class."""

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        expected = {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_to_dictionary_is_dict(self):
        r = Rectangle(10, 2, 1, 9, 5)
        self.assertIsInstance(r.to_dictionary(), dict)

    def test_to_dictionary_doesnt_affect_instance(self):
        r = Rectangle(10, 2, 1, 9, 5)
        d = r.to_dictionary()
        d["width"] = 100
        self.assertEqual(r.width, 10)


if __name__ == "__main__":
    unittest.main()
