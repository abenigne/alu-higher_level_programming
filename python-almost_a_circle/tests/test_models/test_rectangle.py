#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInit(unittest.TestCase):
    """Tests for Rectangle instantiation and validation."""

    def test_width_height(self):
        """Test Rectangle(1, 2)."""
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 0, 0))

    def test_width_height_x(self):
        """Test Rectangle(1, 2, 3)."""
        r = Rectangle(1, 2, 3)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 0))

    def test_width_height_x_y(self):
        """Test Rectangle(1, 2, 3, 4)."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 4))

    def test_width_height_x_y_id(self):
        """Test Rectangle(1, 2, 3, 4, 5)."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_is_base_instance(self):
        """Test that a Rectangle instance is also a Base instance."""
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Base)

    def test_width_str_type(self):
        """Test Rectangle("1", 2) raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_height_str_type(self):
        """Test Rectangle(1, "2") raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_x_str_type(self):
        """Test Rectangle(1, 2, "3") raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_y_str_type(self):
        """Test Rectangle(1, 2, 3, "4") raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_too_many_args(self):
        """Test Rectangle(1, 2, 3, 4, 5, 6) raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_negative_width(self):
        """Test Rectangle(-1, 2) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_negative_height(self):
        """Test Rectangle(1, -2) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_zero_width(self):
        """Test Rectangle(0, 2) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_zero_height(self):
        """Test Rectangle(1, 0) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_negative_x(self):
        """Test Rectangle(1, 2, -3) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_negative_y(self):
        """Test Rectangle(1, 2, 3, -4) raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_error_messages(self):
        """Test that the correct error messages are used."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)


class TestRectangleArea(unittest.TestCase):
    """Tests for the Rectangle.area method."""

    def test_area(self):
        """Test that area() returns the correct value."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    def test_area_docstring(self):
        """Test that area has a docstring."""
        self.assertIsNotNone(Rectangle.area.__doc__)


class TestRectangleStr(unittest.TestCase):
    """Tests for the Rectangle.__str__ method."""

    def test_str(self):
        """Test the string representation of a Rectangle."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_default_x_y(self):
        """Test __str__ with default x and y."""
        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), "[Rectangle] ({}) 1/0 - 5/5".format(r.id))


class TestRectangleDisplay(unittest.TestCase):
    """Tests for the Rectangle.display method."""

    def capture_display(self, rect):
        """Helper to capture the stdout output of display()."""
        captured = io.StringIO()
        sys.stdout = captured
        rect.display()
        sys.stdout = sys.__stdout__
        return captured.getvalue()

    def test_display_no_x_y(self):
        """Test display() without x and y offsets."""
        r = Rectangle(4, 6)
        output = self.capture_display(r)
        expected = ("#" * 4 + "\n") * 6
        self.assertEqual(output, expected)

    def test_display_no_y(self):
        """Test display() with x but default y."""
        r = Rectangle(3, 2, 1, 0)
        output = self.capture_display(r)
        expected = ((" " * 1 + "#" * 3 + "\n") * 2)
        self.assertEqual(output, expected)

    def test_display_x_and_y(self):
        """Test display() taking care of x and y."""
        r = Rectangle(2, 3, 2, 2)
        output = self.capture_display(r)
        expected = "\n\n" + (("  " + "##" + "\n") * 3)
        self.assertEqual(output, expected)

    def test_display_docstring(self):
        """Test that display has a docstring."""
        self.assertIsNotNone(Rectangle.display.__doc__)


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for the Rectangle.to_dictionary method."""

    def test_to_dictionary(self):
        """Test that to_dictionary returns the correct dict."""
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertEqual(d, {
            "id": r.id, "width": 10, "height": 2, "x": 1, "y": 9
        })

    def test_to_dictionary_type(self):
        """Test that to_dictionary returns a dict instance."""
        r = Rectangle(10, 2)
        self.assertIsInstance(r.to_dictionary(), dict)


class TestRectangleUpdate(unittest.TestCase):
    """Tests for the Rectangle.update method."""

    def test_update_no_args(self):
        """Test update() with no arguments changes nothing."""
        r = Rectangle(10, 10, 10, 10)
        before = r.to_dictionary()
        r.update()
        self.assertEqual(before, r.to_dictionary())

    def test_update_id(self):
        """Test update(89) sets the id."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_id_width(self):
        """Test update(89, 1) sets id and width."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1)
        self.assertEqual((r.id, r.width), (89, 1))

    def test_update_id_width_height(self):
        """Test update(89, 1, 2) sets id, width, and height."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2)
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_update_id_width_height_x(self):
        """Test update(89, 1, 2, 3) sets id, width, height, x."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3)
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_update_id_width_height_x_y(self):
        """Test update(89, 1, 2, 3, 4) sets all args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (89, 1, 2, 3, 4))

    def test_update_kwargs_id(self):
        """Test update(**{'id': 89}) sets the id."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_update_kwargs_id_width(self):
        """Test update(**{'id': 89, 'width': 1}) sets id and width."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual((r.id, r.width), (89, 1))

    def test_update_kwargs_id_width_height(self):
        """Test update with id, width, and height kwargs."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_update_kwargs_id_width_height_x(self):
        """Test update with id, width, height, and x kwargs."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_update_kwargs_all(self):
        """Test update with id, width, height, x, and y kwargs."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (89, 1, 2, 3, 4))

    def test_update_docstring(self):
        """Test that update has a docstring."""
        self.assertIsNotNone(Rectangle.update.__doc__)


class TestRectangleDocstrings(unittest.TestCase):
    """Tests for module, class, and method documentation."""

    def test_module_docstring(self):
        """Test that the rectangle module has a docstring."""
        mod = __import__("models.rectangle", fromlist=["rectangle"])
        self.assertIsNotNone(mod.__doc__)

    def test_class_docstring(self):
        """Test that the Rectangle class has a docstring."""
        self.assertIsNotNone(Rectangle.__doc__)

    def test_init_docstring(self):
        """Test that __init__ has a docstring."""
        self.assertIsNotNone(Rectangle.__init__.__doc__)


if __name__ == "__main__":
    unittest.main()
