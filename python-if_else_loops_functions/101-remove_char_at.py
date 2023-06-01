#!/usr/bin/python3
def remove_char_at(str, n):
    str_aux = ""
    for i in range(len(str)):
        if i != n:
            str_aux += str[i]
    return str_aux
