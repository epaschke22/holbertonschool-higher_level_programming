#!/usr/bin/python3
"""Technical Interview Prep"""


def find_peak(list_of_integers):
    """finds peak in list of ints"""
    n = len(list_of_integers)
    if n is 0:
        return None
    if n is 1:
        return list_of_integers[0]
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]
    for i in range(1, n - 1):
        if (list_of_integers[i] >= list_of_integers[i - 1] and
           list_of_integers[i] >= list_of_integers[i + 1]):
            return list_of_integers[i]
