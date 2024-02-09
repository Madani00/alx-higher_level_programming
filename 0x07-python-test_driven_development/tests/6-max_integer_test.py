#!/usr/bin/python3
"""Unittests for max_integer([..])."""


import unittest
max_integer = __import__('6-max_integer').max_integer

class MaxIntegerTestCase(unittest.TestCase):
    """Define unittests for max_integer([..])."""
    def test_empty(self):
        result = max_integer([])
        self.assertIsNone(result)
        self.assertIsNone(max_integer(), None)

    def test_positive_integers(self):
        result = max_integer([1, 3, 5, 2, 4])
        self.assertEqual(result, 5)

    def test_negative_integers(self):
        result = max_integer([-1, -3, -5, -2, -4])
        self.assertEqual(result, -1)

    def test_mixed_integers(self):
        result = max_integer([1, -3, 5, -2, 4])
        self.assertEqual(result, 5)

    def test_single_element(self):
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_duplicate_values(self):
        result = max_integer([3, 2, 3, 1, 1])
        self.assertEqual(result, 3)

    def test_ordered(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

if __name__ == "__main__":
    unittest.main()
