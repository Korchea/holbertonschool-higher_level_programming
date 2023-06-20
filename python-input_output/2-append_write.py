#!/usr/bin/python3
"""append_write
"""


def append_write(filename="", text=""):
    """append_write

    Args:
        filename (str): Is the name of a file. Defaults to "".
    """
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(text)
    return len(text)
