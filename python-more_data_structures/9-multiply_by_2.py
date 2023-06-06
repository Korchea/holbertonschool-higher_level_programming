#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul = {}
    for key, value in a_dictionary.items():
        mul.update({key: value * 2})
    return mul
