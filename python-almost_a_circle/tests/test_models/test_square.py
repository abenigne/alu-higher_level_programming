#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInit(unittest.TestCase):
    """Tests for Square instantiation and validation."""

    def test_size(self):
        """Test Square(1)."""
        s = Square(1)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 0, 0))

    def test_size_x(self):
        """Test Square(1, 2)."""
        s = Square(1, 2)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 2, 0))

    def test_size_x_y(self):
        """Test Square(1, 2, 3)."""
        s = Square(1, 2, 3)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 2, 3))

    def test_size_x_y_id(self):
        """Test Square(1, 2, 3, 4)."""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_is_rectangle_instance(self):
        """Test that a Square instance is also a Rectangle instance."""
        s = Square(1)
        self.assertIsInstance(s, Rectangle)

    def test_size_str_type(self):
        """Test Square("1") raises TypeError."""
        with self.assertRaises(TypeError):
            Square("1")

    def test_x_str_type(self):
        """Test Square(1, "2") raises TypeError."""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_str_type(self):
        """Test Square(1, 2, "3") raises TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_too_many_args(self):
        """Test Square(1, 2, 3, 4, 5) raises TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_negative_size(self):
        """Test Square(-1) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_negative_x(self):
        """Test Square(1, -2) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_negative_y(self):
        """Test Square(1, 2, -3) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_zero_size(self):
        """Test Square(0) raises ValueError."""
        with self.assertRaises(ValueError):
            Square(0)


class TestSquareStr(unittest.TestCase):
    """Tests for the Square.__str__ method."""

    def test_str(self):
        """Test the string representation of a Square."""
        s = Square(3, 1, 3, 9)
        self.assertEqual(str(s), "[Square] (9) 1/3 - 3")


class TestSquareSize(unittest.TestCase):
    """Tests for the Square size getter and setter."""

    def test_size_getter(self):
        """Test that the size getter returns width."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Test that the size setter updates width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))

    def test_size_setter_type_error(self):
        """Test that the size setter raises TypeError on bad type."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_size_setter_value_error(self):
        """Test that the size setter raises ValueError on bad value."""
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -1


class TestSquareToDictionary(unittest.TestCase):
    """Tests for the Square.to_dictionary method."""

    def test_to_dictionary(self):
        """Test that to_dictionary returns the correct dict."""
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": s.id, "size": 10, "x": 2, "y": 1})

    def test_to_dictionary_type(self):
        """Test that to_dictionary returns a dict instance."""
        s = Square(10)
        self.assertIsInstance(s.to_dictionary(), dict)


class TestSquareUpdate(unittest.TestCase):
    """Tests for the Square.update method."""

    def test_update_no_args(self):
        """Test update() with no arguments changes nothing."""
        s = Square(5)
        before = s.to_dictionary()
        s.update()
        self.assertEqual(before, s.to_dictionary())

    def test_update_id(self):
        """Test update(89) sets the id."""
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_id_size(self):
        """Test update(1, 2) sets id and size."""
        s = Square(5)
        s.update(1, 2)
        self.assertEqual((s.id, s.size), (1, 2))

    def test_update_id_size_x(self):
        """Test update(1, 2, 3) sets id, size, and x."""
        s = Square(5)
        s.update(1, 2, 3)
        self.assertEqual((s.id, s.size, s.x), (1, 2, 3))

    def test_update_id_size_x_y(self):
        """Test update(1, 2, 3, 4) sets id, size, x, and y."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual((s.id, s.size, s.x, s.y), (1, 2, 3, 4))

    def test_update_kwargs_id(self):
        """Test update(**{'id': 89}) sets the id."""
        s = Square(5)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_update_kwargs_id_size(self):
        """Test update with id and size kwargs."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_kwargs_id_size_x(self):
        """Test update with id, size, and x kwargs."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_update_kwargs_all(self):
        """Test update with id, size, x, and y kwargs."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    def test_update_docstring(self):
        """Test that update has a docstring."""
        self.assertIsNotNone(Square.update.__doc__)


class TestSquareDocstrings(unittest.TestCase):
    """Tests for module, class, and method documentation."""

    def test_module_docstring(self):
        """Test that the square module has a docstring."""
        mod = __import__("models.square", fromlist=["square"])
        self.assertIsNotNone(mod.__doc__)

    def test_class_docstring(self):
        """Test that the Square class has a docstring."""
        self.assertIsNotNone(Square.__doc__)

    def test_init_docstring(self):
        """Test that __init__ has a docstring."""
        self.assertIsNotNone(Square.__init__.__doc__)


if __name__ == "__main__":
    unittest.main()
