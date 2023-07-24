#!/usr/bin/python3
"""Unittest for class Square
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_create_class(self):
        s1 = Square(5)
        self.assertAlmostEqual(Square.__str__(s1), "[Square] (1) 0/0 - 5")
        self.assertAlmostEqual(s1.area(), 25)


if __name__ == "__main__":
    unittest.main()
