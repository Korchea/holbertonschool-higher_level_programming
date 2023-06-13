#!/usr/bin/python3
"""say_my_name
"""


def say_my_name(first_name, last_name=""):
    """say_my_name

    Args:
        first_name (str): Is a string
        last_name (str): Is a string. Defaults to "".

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if not type(first_name) == str:
        raise TypeError("first_name must be a string")
    if not type(last_name) == str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
