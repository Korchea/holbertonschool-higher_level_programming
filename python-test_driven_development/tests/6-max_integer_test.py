#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestMaxInteger

    Args:
        unittest: Just cases to tests
    """

    def standar_case(self):
        self.assertAlmostEqual(max_integer([1, 2, 4, 3]), 4)

    def none_case(self):
        self.assertAlmostEqual(max_integer([None]), None)

    def empty_case(self):
        self.assertAlmostEqual(max_integer(), None)

    def negative_case(self):
        self.assertAlmostEqual(max_integer([-1]), -1)


if __name__ == '__main__':
    unittest.main()
