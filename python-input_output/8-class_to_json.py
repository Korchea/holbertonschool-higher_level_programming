#!/usr/bin/python3
"""class_to_json
"""


def class_to_json(obj):
    """class_to_json

    Args:
        obj (class): Is an object

    Returns:
        dict: Is a the clas in dict form
    """
    return obj.__dict__
