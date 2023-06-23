#!/usr/bin/python3
"""pascal_triangle
"""


def pascal_triangle(n):
    """pascal_triangle

    Args:
        n (int): Is the size

    Returns:
        list: Is a list of list, a pascal triangle
    """
    pascal = []
    for i in range(n):
        pascal.append([1])
        for j in range(i):
            if j == i - 1:
                pascal[i].append(1)
            else:
                pascal[i].append(pascal[i-1][j+1] + pascal[i-1][j])
    return pascal
