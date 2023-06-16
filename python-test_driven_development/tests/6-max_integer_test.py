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

    def test_standar(self):
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_none(self):
        self.assertEqual(max_integer([None]), None)

    def test_empty(self):
        self.assertEqual(max_integer(), None)

    def test_negative(self):
        self.assertEqual(max_integer([-1]), -1)

    def test_float(self):
        self.assertEqual(max_integer([1.2]), 1.2)

    def test_only_zero(self):
        self.assertEqual(max_integer([0, 0]), 0)