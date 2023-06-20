#!/usr/bin/python3
"""from_json_string
"""
import json


def from_json_string(my_str):
    """from_json_string

    Args:
        my_obj (any): is an object

    Returns:
        str: a json
    """
    return json.loads(my_str)
