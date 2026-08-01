#!/usr/bin/python3
"""Unit tests for Base class in models.base module."""
import unittest
from models.base import Base


class TestBaseDocs(unittest.TestCase):
    """Tests to check documentation and style compliance for Base class."""

    def test_module_docstring(self):
        """Test module docstring presence."""
        import models.base as base_module
        self.assertIsNotNone(base_module.__doc__)
        self.assertTrue(len(base_module.__doc__.strip()) > 0)

    def test_class_docstring(self):
        """Test Base class docstring presence."""
        self.assertIsNotNone(Base.__doc__)
        self.assertTrue(len(Base.__doc__.strip()) > 0)

    def test_init_docstring(self):
        """Test __init__ method docstring presence."""
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertTrue(len(Base.__init__.__doc__.strip()) > 0)


class TestBaseInstantiation(unittest.TestCase):
    """Tests for instantiation of Base class objects."""

    def setUp(self):
        """Reset private variable before each test."""
        Base._Base__nb_objects = 0

    def test_id_auto_increment(self):
        """Test automatic ID assignment incrementing by 1."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_explicit_value(self):
        """Test explicit ID assignment."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_id_mixed_auto_and_explicit(self):
        """Test mixture of automatic and explicit IDs."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_id_negative(self):
        """Test negative integer as explicit ID."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_id_string(self):
        """Test string as explicit ID."""
        b = Base("test_id")
        self.assertEqual(b.id, "test_id")

    def test_id_float(self):
        """Test float as explicit ID."""
        b = Base(3.14)
        self.assertEqual(b.id, 3.14)

    def test_id_list(self):
        """Test list as explicit ID."""
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

    def test_id_dict(self):
        """Test dictionary as explicit ID."""
        b = Base({"key": "val"})
        self.assertEqual(b.id, {"key": "val"})

    def test_id_none(self):
        """Test passing None explicitly triggers auto-increment."""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)


if __name__ == "__main__":
    unittest.main()
