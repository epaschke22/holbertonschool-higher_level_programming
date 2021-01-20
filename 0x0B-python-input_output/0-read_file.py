#!/usr/bin/python3
"""Read File"""


def read_file(filename=""):
    """This function reads and prints out text from file"""
    with open(filename) as f:
        for line in f:
            print(line)
