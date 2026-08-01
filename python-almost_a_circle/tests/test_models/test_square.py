#!/usr/bin/python3
"""
Unittest module for testing the Square class.
"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def setUp(self):
        """
        Resets the __nb_objects counter before each test.
        """
        Base._Base__nb_objects = 0

    def test_square_creation(self):
        """
        Tests initialization of Square object attributes.
        """
        s = Square(5, 1, 2, 9)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 9)

    def test_invalid_types(self):
        """
        Tests raising TypeError for non-integer inputs.
        """
        with self.assertRaises(TypeError):
            Square("5")
        with self.assertRaises(TypeError):
            Square(5, "1")
        with self.assertRaises(TypeError):
            Square(5, 1, "2")

    def test_invalid_values(self):
        """
        Tests raising ValueError for non-positive or negative values.
        """
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-5)
        with self.assertRaises(ValueError):
            Square(5, -1)
        with self.assertRaises(ValueError):
            Square(5, 1, -2)

    def test_str(self):
        """
        Tests string representation of Square.
        """
        s = Square(5, 2, 1, 3)
        self.assertEqual(str(s), "[Square] (3) 2/1 - 5")

    def test_to_dictionary(self):
        """
        Tests dictionary representation of Square.
        """
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        expected = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(d, expected)


if __name__ == "__main__":
    unittest.main()
