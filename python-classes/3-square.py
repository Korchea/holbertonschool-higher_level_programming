#!/usr/bin/python3
"""
In this file I create a class squere
"""


class Square:
    """
    Is a class Squere.
    """

    def __init__(self, size=0):
        """
        Define the size of the class.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of a Square.
        """
        return self.__size * self.__size
