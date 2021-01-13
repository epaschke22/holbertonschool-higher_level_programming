#!/usr/bin/python3
"""This program adds two intagers together and returns total"""


def add_integer(a=None, b=98):
    """Returns a + b only if they are numbers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
