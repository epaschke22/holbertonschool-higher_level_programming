#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """writes text to file and returns bytes written"""
    with open(filename, 'w') as f:
        return f.write(text)
