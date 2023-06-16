#!/usr/bin/python3
"""Write a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """matrix_divided

    Args:
        matrix (list): Is a list of list
        div (int): Is an int different of 0

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: div must be a number
        ZeroDivisionError: division by zero
        TypeError: Each row of the matrix must have the same size
        TypeError: matrix must be a matrix (list of lists) of integers/floats

    Returns:
        list: Divided matrix
    """
    txt = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list:
        raise TypeError(txt)
    if len(matrix) == 0:
        raise TypeError(txt)
    matrix_cpy = matrix.copy()
    aux = -1
    if not type(div) == int and not type(div) == float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix_cpy)):
        if aux != -1 and aux != len(matrix_cpy[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix_cpy[i])):
            if not type(matrix_cpy[i][j]) == int and\
                    not type(matrix_cpy[i][j]) == float:
                raise TypeError(txt)
        matrix_cpy[i] = list(map(lambda x: round(x / div, 2), matrix[i]))
        aux = len(matrix_cpy[i])
    return matrix_cpy
