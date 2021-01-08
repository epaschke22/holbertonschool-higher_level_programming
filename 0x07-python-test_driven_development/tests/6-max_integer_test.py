#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """class holding testscases"""
    def test_integers(self):
        """test correct input"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2]), -1)
        self.assertEqual(max_integer([2]), 2)

    def test_strings(self):
        """test string inputs"""
        self.assertEqual(max_integer("freeze"), "z")
        self.assertEqual(max_integer(["Joe", "Bob"]), "Joe")

    def test_empty(self):
        """test empty inputs"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([[]]), [])

    def test_error(self):
        """test incorrect type inputs"""
        self.assertRaises(TypeError, max_integer, 2)
        self.assertRaises(TypeError, max_integer, None)

