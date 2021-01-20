#!/usr/bin/python3
"""Append to a file"""


def write_file(filename="", text=""):
    """appends text to file at the end and returns bytes written"""
    with open(filename, 'a') as f:
        return f.write(text)