#!/usr/bin/python3
"""This program prints out someones name"""


def say_my_name(first_name=None, last_name=""):
    """checks for strings"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
