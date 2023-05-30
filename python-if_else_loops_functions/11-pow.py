#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return (1)
    if b < 0:
        a = 1 / a
        b = -b
    x = a
    for i in range(1, b):
        if a < 0:
            a = -a
            a = a * x
            a = -a
        else:
            a = a * x
    return (a)
