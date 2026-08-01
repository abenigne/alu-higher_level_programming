#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class."""

    def test_is_base_instance(self):
        """Test that Rectangle inherits from Base."""
        r = Rectangle(1, 1)
        self.assertIsInstance(r, Base)

    def test_width_height_x_y(self):
        """Test width, height, x, y are correctly set."""
        r = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_default_x_y(self):
        """Test default x and y are 0."""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_width_type_error(self):
        """Test TypeError is raised for non-integer width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_height_type_error(self):
        """Test TypeError is raised for non-integer height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_x_type_error(self):
        """Test TypeError is raised for non-integer x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})

    def test_y_type_error(self):
        """Test TypeError is raised for non-integer y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, "4")

    def test_width_value_error(self):
        """Test ValueError is raised for width <= 0."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_height_value_error(self):
        """Test ValueError is raised for height <= 0."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_x_value_error(self):
        """Test ValueError is raised for x < 0."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3)

    def test_y_value_error(self):
        """Test ValueError is raised for y < 0."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -4)

    def test_area(self):
        """Test the area method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """Test the __str__ method."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Test update with no-keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test update with keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/10")

    def test_to_dictionary(self):
        """Test to_dictionary returns the correct dict."""
        r = Rectangle(10, 2, 1, 9, 1)
        expected = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
