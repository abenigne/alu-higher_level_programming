#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unit tests for the Square class."""

    def test_is_rectangle_instance(self):
        """Test that Square inherits from Rectangle."""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_size_sets_width_and_height(self):
        """Test that size is assigned to both width and height."""
        s = Square(5, 1, 2, 3)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 3)

    def test_size_type_error(self):
        """Test TypeError is raised for non-integer size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")

    def test_size_value_error(self):
        """Test ValueError is raised for size <= 0."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_str(self):
        """Test the __str__ method."""
        s = Square(3, 1, 3, 5)
        self.assertEqual(str(s), "[Square] (5) 1/3 - 3")

    def test_size_getter(self):
        """Test the size getter."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Test the size setter updates width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_update_args(self):
        """Test update with no-keyword arguments."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """Test update with keyword arguments."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_to_dictionary(self):
        """Test to_dictionary returns the correct dict."""
        s = Square(10, 2, 1, 1)
        expected = {"id": 1, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)

    def test_area(self):
        """Test the area method for Square."""
        s = Square(4)
        self.assertEqual(s.area(), 16)


if __name__ == "__main__":
    unittest.main()
