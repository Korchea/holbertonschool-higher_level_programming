#!/usr/bin/python3
"""write_file
"""


def write_file(filename="", text=""):
    """write_file

    Args:
        filename (str): Is the name of a file. Defaults to "".
    """
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
    return len(text)
