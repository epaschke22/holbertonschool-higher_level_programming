#!/usr/bin/python3
"""This program devides each element of a matrix"""


def matrix_divided(matrix, div):
    """function checks all contents of matrix and divides all by div"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        mlen = len(matrix[0])
    for x in range(len(matrix)):
        if type(matrix[x]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[x]) != mlen:
            raise TypeError("Each row of the matrix must have the same size")
        for y in range(len(matrix[x])):
            if type(matrix[x][y]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    for row in matrix:
        result.append(list(map(lambda x: round(x / div, 2), row)))
    return result
