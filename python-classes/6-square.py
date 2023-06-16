#!/usr/bin/python3
"""
In this file I create a class squere
"""


class Square:
    """Defining a Square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Define the size of the class.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of a Square.
        """
        return self.__size * self.__size

    def my_print(self):

        if self.size == 0:
            print()
        else:
            for x in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for y in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
