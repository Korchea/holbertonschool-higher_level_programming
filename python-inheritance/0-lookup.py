#!/usr/bin/python3
"""Function declare
"""


def lookup(obj):
    """lookup

    Args:
        obj (subclass): Is an objet from a class

    Returns:
        list: Return the list of available attributes and methods of an object
    """
    return dir(obj)
