#!/usr/bin/python3
"""max_integer_test
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class max_integer_test(unittest.TestCase):
    """max_integer_test

    Args:
        unittest: Just cases to tests
    """

    def standar_case(self):
        self.assertEqual('[1, 2, 4, 3]'.max_integer(), '4')

    def none_case(self):
        self.assertEqual('[None]'.max_integer(), 'None')

    def empty_case(self):
        self.assertEqual(''.max_integer(), 'None')

    def negative_case(self):
        self.assertEqual('[-1]'.max_integer(), '-1')

    def string_case(self):
        self.assertEqual('["Hi"]'.max_integer(), 'Hi')


if __name__ == '__main__':
    unittest.main()
