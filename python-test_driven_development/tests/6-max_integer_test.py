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
        self.assertEqual('[1, 2, 4, 3]'.max_integer(), '4')

    def test_none(self):
        self.assertEqual('[None]'.max_integer(), 'None')

    def test_empty(self):
        self.assertEqual(''.max_integer(), 'None')

    def test_negative(self):
        self.assertEqual('[-1]'.max_integer(), '-1')

    def test_string(self):
        self.assertEqual('["Hi"]'.max_integer(), 'Hi')


if __name__ == '__main__':
    unittest.main()
