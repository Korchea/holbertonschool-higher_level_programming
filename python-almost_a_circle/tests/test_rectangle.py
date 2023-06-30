#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    def test_create_class(self):
        r1 = Rectangle(10, 2)
        self.assertAlmostEqual(r1.width, 10)
        self.assertAlmostEqual(r1.height, 2)
        self.assertAlmostEqual(r1.x, 0)
        self.assertAlmostEqual(r1.y, 0)
        self.assertAlmostEqual(r1.id, 7)
        r2 = Rectangle(2, 10)
        self.assertAlmostEqual(r2.width, 2)
        self.assertAlmostEqual(r2.height, 10)
        self.assertAlmostEqual(r2.x, 0)
        self.assertAlmostEqual(r2.y, 0)
        self.assertAlmostEqual(r2.id, 8)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertAlmostEqual(r3.width, 10)
        self.assertAlmostEqual(r3.height, 2)
        self.assertAlmostEqual(r3.id, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_print_and_update(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertAlmostEqual(Rectangle.__str__(
            r1), "[Rectangle] (12) 2/1 - 4/6")
        r1.update(89)
        self.assertAlmostEqual(Rectangle.__str__(
            r1), "[Rectangle] (89) 2/1 - 4/6")
        r1.update(89, 2)
        self.assertAlmostEqual(Rectangle.__str__(
            r1), "[Rectangle] (89) 2/1 - 2/6")
        r1.update(89, 2, 3)
        self.assertAlmostEqual(Rectangle.__str__(
            r1), "[Rectangle] (89) 2/1 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertAlmostEqual(Rectangle.__str__(
            r1), "[Rectangle] (89) 4/1 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertAlmostEqual(Rectangle.__str__(
            r1), "[Rectangle] (89) 4/5 - 2/3")
        r2 = Rectangle(10, 10, 10, 10, 100)
        self.assertAlmostEqual(Rectangle.__str__(
            r2), "[Rectangle] (100) 10/10 - 10/10")
        r2.update(height=1)
        self.assertAlmostEqual(Rectangle.__str__(
            r2), "[Rectangle] (100) 10/10 - 10/1")
        r2.update(width=1, x=2)
        self.assertAlmostEqual(Rectangle.__str__(
            r2), "[Rectangle] (100) 2/10 - 1/1")
        r2.update(y=1, width=2, x=3, id=89)
        self.assertAlmostEqual(Rectangle.__str__(
            r2), "[Rectangle] (89) 3/1 - 2/1")
        r2.update(x=1, height=2, y=3, width=4)
        self.assertAlmostEqual(Rectangle.__str__(
            r2), "[Rectangle] (89) 1/3 - 4/2")

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertAlmostEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertAlmostEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertAlmostEqual(r3.area(), 56)

    def test_setter(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)


if __name__ == "__main__":
    unittest.main()
