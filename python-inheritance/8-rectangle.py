#!/usr/bin/python3
"""BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle

    Args:
        BaseGeometry (class): Is a class
    """

    def __init__(self, width, height):
        self.integer_validator("height", height)
        self._Rectangle__height = height
        self.integer_validator("width", width)
        self._Rectangle__width = width
