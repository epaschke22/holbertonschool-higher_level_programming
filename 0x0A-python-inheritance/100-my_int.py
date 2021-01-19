#!/usr/bin/python3
"""changing the int class"""


class MyInt(int):
    """New version of int"""
    def __eq__(self, other):
        """check if equal to other"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """check if not equal to other"""
        return int.__eq__(self, other)
