#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_create_class(self):
        """test_create_class
        """
        base1 = Base()
        self.assertAlmostEqual(base1.id, 1)
        base2 = Base()
        self.assertAlmostEqual(base2.id, 2)
        base3 = Base(22)
        self.assertAlmostEqual(base3.id, 22)
        base4 = Base(-22)
        self.assertAlmostEqual(base4.id, -22)

    def test_first_function(self):
        self.assertAlmostEqual(Base.to_json_string(None), "[]")
        self.assertAlmostEqual(Base.to_json_string([{'id': 1}]),
                               '[{"id": 1}]')
        self.assertAlmostEqual(Base.to_json_string([]), "[]")

    def test_second_function(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertAlmostEqual(file.read(), "[]")

    def test_third_function(self):
        self.assertAlmostEqual(Base.from_json_string(None), [])
        self.assertAlmostEqual(
            Base.from_json_string('[{"id": 1}]'), [{"id": 1}])
        self.assertAlmostEqual(Base.from_json_string("[]"), [])

    def test_fourth_function(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertAlmostEqual(r1 is r2, False)
        self.assertAlmostEqual(r1 == r2, False)


if __name__ == "__main__":
    unittest.main()
