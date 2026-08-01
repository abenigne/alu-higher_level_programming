#!/usr/bin/python3
"""
Unittest module for testing the Rectangle class.
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def setUp(self):
        """
        Resets the __nb_objects counter before each test.
        """
        Base._Base__nb_objects = 0

    def test_rectangle_creation(self):
        """
        Tests initialization of Rectangle object attributes.
        """
        r = Rectangle(10, 20, 1, 2, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 5)

    def test_invalid_types(self):
        """
        Tests raising TypeError for non-integer inputs.
        """
        with self.assertRaises(TypeError):
            Rectangle("10", 20)
        with self.assertRaises(TypeError):
            Rectangle(10, "20")
        with self.assertRaises(TypeError):
            Rectangle(10, 20, "1")
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 1, "2")

    def test_invalid_values(self):
        """
        Tests raising ValueError for invalid dimensions.
        """
        with self.assertRaises(ValueError):
            Rectangle(0, 20)
        with self.assertRaises(ValueError):
            Rectangle(10, -5)
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -1)
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 1, -2)

    def test_area(self):
        """
        Tests calculating the area of Rectangle.
        """
        r = Rectangle(5, 4)
        self.assertEqual(r.area(), 20)

    def test_str(self):
        """
        Tests string representation of Rectangle.
        """
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_to_dictionary(self):
        """
        Tests dictionary representation of Rectangle.
        """
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        expected = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(d, expected)


if __name__ == "__main__":
    unittest.main()
