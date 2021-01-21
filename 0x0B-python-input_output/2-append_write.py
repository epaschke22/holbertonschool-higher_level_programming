#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """appends text to file at the end and returns bytes written"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
