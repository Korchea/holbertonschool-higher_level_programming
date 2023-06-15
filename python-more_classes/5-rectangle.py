#!/usr/bin/python3
"""Define class Rectangle
"""


class Rectangle():
    """Rectangle
    """

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        per = (2 * self.__width) + (2 * self.__height)
        if self.__height == 0 or self.__width == 0:
            per = 0
        return per

    def __str__(self):
        rec = ""
        if self.__height == 0 or self.__width == 0:
            return rec
        for i in range(self.__height):
            for j in range(self.__width):
                rec += '#'
            if i != self.__height - 1:
                rec += "\n"
        return rec

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
