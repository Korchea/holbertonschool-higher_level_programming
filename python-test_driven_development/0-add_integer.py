#!/usr/bin/python3
"""
I add two numbers
"""


def add_integer(a, b=98):
    """add_integer

    Args:
        a (int, float): Is a number
        b (int, float): Is a number. Defaults to 98.

    Raises:
        TypeError: "a must be an integer"
        TypeError: "b must be an integer"

    Returns:
        _type_: a + b
    """
    if not type(a) == int and not type(a) == float:
        raise TypeError("a must be an integer")
    if not type(b) == int and not type(b) == float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
