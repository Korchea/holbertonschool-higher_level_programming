#!/usr/bin/python3
"""Crete a function is_same_class
"""


def is_same_class(obj, a_class):
    """is_same_class

    Args:
        obj (subclass): Is an objet to compare
        a_class (subclass): Is to compare

    Returns:
        Bool: If is an instance return True else False
    """
    return isinstance(obj, a_class)
