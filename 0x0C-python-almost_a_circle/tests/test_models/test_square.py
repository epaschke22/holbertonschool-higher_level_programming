#!/usr/bin/python3
"""Unit tests for square.py"""
import unittest
from models.base import Base
from models.square import Square
from unittest.mock import patch
from io import StringIO


class TestSquare(unittest.TestCase):
    """Testing square.py"""
    def setUp(self):
        """runs before each test"""
        Base._Base__nb_objects = 0

    def test_square(self):
        """testing creating square objects"""
        self.s1 = Square(2)
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s1.id, 1)

        self.s2 = Square(4, 1, 1, 12)
        self.assertEqual(self.s2.size, 4)
        self.assertEqual(self.s2.x, 1)
        self.assertEqual(self.s2.y, 1)
        self.assertEqual(self.s2.id, 12)

    def test_square_typeerrors(self):
        """testing incorrect types in square objects"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square()
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "3")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, "4")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("2", "3", "4")

    def test_square_valueerrors(self):
        """testing incorrect values in square objects"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 3, -1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, -1, -1)

    def test_square_display(self):
        """testing display method"""
        expected = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as test_out:
            s1 = Square(2)
            s1.display()
        self.assertEqual(test_out.getvalue(), expected)
        expected = "\n\n\n  ####\n  ####\n  ####\n  ####\n"
        with patch('sys.stdout', new=StringIO()) as test_out:
            s2 = Square(4, 2, 3)
            s2.display()
        self.assertEqual(test_out.getvalue(), expected)

    def test_square_string(self):
        """testing string return on square object"""
        s1 = Square(4)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 4")
        s2 = Square(4, 10, 11, 12)
        self.assertEqual(str(s2), "[Square] (12) 10/11 - 4")

    def test_rectangle_update_args(self):
        """testing update method in objects"""
        s1 = Square(4)
        s1.update(89)
        self.assertEqual(str(s1), "[Square] (89) 0/0 - 4")
        s1.update(89, 2)
        self.assertEqual(str(s1), "[Square] (89) 0/0 - 2")
        s1.update(89, 2, 3)
        self.assertEqual(str(s1), "[Square] (89) 3/0 - 2")
        s1.update(89, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (89) 3/4 - 2")

    def test_rectangle_update_kwargs(self):
        """testing update method with kwargs in object"""
        s1 = Square(4)
        s1.update(size=1)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 1")
        s1.update(size=1, x=2)
        self.assertEqual(str(s1), "[Square] (1) 2/0 - 1")
        s1.update(y=1, size=2, x=3)
        self.assertEqual(str(s1), "[Square] (1) 3/1 - 2")
        s1.update(size=4, y=3, id=89, x=1)
        self.assertEqual(str(s1), "[Square] (89) 1/3 - 4")

    def test_square_todict(self):
        """tests to_dictionary for square"""
        sdict1 = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertDictEqual(sdict1, s1_dictionary)
        s2 = Square(1)
        s2.update(**s1_dictionary)
        self.assertEqual(str(s1), "[Square] (1) 2/1 - 10")
