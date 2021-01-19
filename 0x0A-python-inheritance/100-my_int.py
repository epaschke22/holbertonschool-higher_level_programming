#!/usr/bin/python3
"""changing the int class"""


class MyInt(int):
    """New version of int"""
    def __eq__(self, other):
        """check if equal to other"""
        return False

    def __ne__(self, other):
        """check if not equal to other"""
        return True
