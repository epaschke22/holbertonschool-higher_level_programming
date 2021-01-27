#!/usr/bin/python3
"""Unit tests for base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import patch
from io import StringIO


class TestBaseInit(unittest.TestCase):
    """Testing base.py"""
    def setUp(self):
        """runs before each test"""
        Base._Base__nb_objects = 0

    def test_base_init(self):
        """testing attributes in each base object"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base(-2)
        self.assertEqual(b4.id, -2)
        b5 = Base(12)
        self.assertEqual(b5.id, 12)

    def test_json(self):
        """tests to_json methon in Base"""
        r1 = Rectangle(10, 7, 2, 8)
        s1 = Square(4, 2, 3)
        dictionary1 = r1.to_dictionary()
        dictionary2 = s1.to_dictionary()
        json_dictionary = Rectangle.to_json_string([dictionary1, dictionary2])
        list_dict = Rectangle.from_json_string(json_dictionary)
        self.assertDictEqual(list_dict[0], dictionary1)
        self.assertDictEqual(list_dict[1], dictionary2)
