#!/usr/bin/python3
"""read_file
"""


def read_file(filename=""):
    """read_file

    Args:
        filename (str): Is the name of a file. Defaults to "".
    """
    with open(filename) as file:
        txt = file.read()
        print(txt)
