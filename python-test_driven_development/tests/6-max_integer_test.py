#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test with a list of ascending integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with a list of unordered integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """Test with a list of descending integers."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """Test with a list containing a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list, should return None."""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """Test the default argument (empty list)."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Test with a list of negative integers."""
        self.assertEqual(max_integer([-1, -3, -2]), -1)

    def test_mixed_positive_negative(self):
        """Test with a mix of positive and negative integers."""
        self.assertEqual(max_integer([-5, 3, 0, -2, 8]), 8)

    def test_duplicate_max_values(self):
        """Test with duplicate maximum values in the list."""
        self.assertEqual(max_integer([4, 4, 2, 4]), 4)

    def test_floats(self):
        """Test with a list of float numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_all_same_values(self):
        """Test with a list where all values are identical."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)


if __name__ == '__main__':
    unittest.main()
