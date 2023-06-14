#!/usr/bin/python3
"""print_square
"""


def print_square(size):
    """print_square

    Args:
        size (int): Is an integer

    Raises:
        TypeError: size must be an integer
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
