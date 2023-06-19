#!/usr/bin/python3
"""is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class

    Args:
        obj (subclass): Is an object to compare
        a_class (subclass): Is to compare

    Returns:
        Bool: If is an instance return True else False
    """
    return isinstance(obj, a_class)
