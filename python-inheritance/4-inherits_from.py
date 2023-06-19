#!/usr/bin/python3
"""inherits_from
"""


def inherits_from(obj, a_class):
    """inherits_from

    Args:
        obj (subclass): Is an object to compare
        a_class (subclass): To compare

    Returns:
        Bool: If is an instance return True else False
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
