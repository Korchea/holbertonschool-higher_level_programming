#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    c = 0
    d = 0
    if len(tuple_a) >= 1:
        a = tuple_a[0]
    if len(tuple_b) >= 1:
        b = tuple_b[0]
    if len(tuple_a) >= 2:
        c = tuple_a[1]
    if len(tuple_b) >= 2:
        d = tuple_b[1]
    return (a + b, c + d)
