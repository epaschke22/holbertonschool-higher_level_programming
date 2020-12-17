#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    output = []
    for row in matrix:
        output.append(list(map(lambda x: x * x, row)))
    return output
