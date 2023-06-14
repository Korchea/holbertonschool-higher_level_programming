#!/usr/bin/python3
"""text_indentation
"""


def text_indentation(text):
    """text_identation

    Args:
        text (str): Is a string

    Raises:
        TypeError: text must be a string
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    flag = False
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print(i)
            print()
            flag = True
        elif i != ' ' or flag == False:
            print(i, end="")
            flag = False
