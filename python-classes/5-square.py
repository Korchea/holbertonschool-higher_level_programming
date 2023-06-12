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

    @property
    def size(self):
        """
        Returns the size of a Squere.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Define the size of the class.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
