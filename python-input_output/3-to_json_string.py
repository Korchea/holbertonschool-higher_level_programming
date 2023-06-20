#!/usr/bin/python3
import json
"""to_json_string
"""


def to_json_string(my_obj):
    """to_json_string

    Args:
        my_obj (any): is an object

    Returns:
        str: a json
    """
    return json.dumps(my_obj)
