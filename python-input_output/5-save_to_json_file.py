#!/usr/bin/python3
import json
"""save_to_json_file
"""


def save_to_json_file(my_obj, filename):
    """save_to_json_file

    Args:
        my_obj (anytype): Is an object
        filename (str): Is the name file
    """
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
