#!/usr/bin/python3
"""Example class to inherit from"""


class MyList(list):
    """My own list class"""
    def print_sorted(self):
        """prints out list in sorted order"""
        print(sorted(self))
