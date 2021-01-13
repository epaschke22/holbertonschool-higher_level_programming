#!/usr/bin/python3
"""This program prints a square using # symbols"""


def print_square(size):
    """checks for positive ints"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
