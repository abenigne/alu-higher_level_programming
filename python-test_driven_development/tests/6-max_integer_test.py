#!/usr/bin/python3
"""Unit tests for max_integer."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([4, 1, 3, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -1, -3]), -1)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.2, 5.4, 2.8]), 5.4)

    def test_string_list(self):
        self.assertEqual(max_integer(["a", "z", "b"]), "z")


if __name__ == "__main__":
    unittest.main()
