#!/usr/bin/python3
"""to_json_string
"""
import json


def to_json_string(my_obj):
    """to_json_string

    Args:
        my_obj (any): is an object

    Returns:
        str: a json
    """
    return json.dumps(my_obj)
