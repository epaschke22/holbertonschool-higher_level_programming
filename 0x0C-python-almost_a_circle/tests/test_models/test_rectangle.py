#!/usr/bin/python3
"""Unit tests for rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class TestRectangle(unittest.TestCase):
    """Testing rectangle.py"""
    def setUp(self):
        """runs before each test"""
        Base._Base__nb_objects = 0

    def test_rectangle(self):
        """testing attributes when making rectangle objects"""
        self.r1 = Rectangle(2, 3)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r1.id, 1)

        self.r2 = Rectangle(6, 3, 4, 5, 12)
        self.assertEqual(self.r2.width, 6)
        self.assertEqual(self.r2.height, 3)
        self.assertEqual(self.r2.x, 4)
        self.assertEqual(self.r2.y, 5)
        self.assertEqual(self.r2.id, 12)

    def test_rectangle_typeerrors(self):
        """testing incorrect types in rectangle objects"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle()
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2, "2")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", "2", "3", "5")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, None, None, None)

    def test_rectangle_valueerrors(self):
        """testing incorrect values in rectangle objects"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 3, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 3, 4, -1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 0, -1, -1)

    def test_rectangle_display(self):
        """testing display method"""
        expected = "##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as test_out:
            r1 = Rectangle(2, 3)
            r1.display()
        self.assertEqual(test_out.getvalue(), expected)
        expected = "\n\n\n  ######\n  ######\n  ######\n"
        with patch('sys.stdout', new=StringIO()) as test_out:
            r2 = Rectangle(6, 3, 2, 3)
            r2.display()
        self.assertEqual(test_out.getvalue(), expected)

    def test_rectangle_string(self):
        """testing string return on rectangle object"""
        r1 = Rectangle(4, 6)
        self.assertEqual(str(r1), "[Rectangle] (1) 0/0 - 4/6")
        r2 = Rectangle(4, 6, 10, 11, 12)
        self.assertEqual(str(r2), "[Rectangle] (12) 10/11 - 4/6")

    def test_rectangle_update_args(self):
        """testing update method in objects"""
        r1 = Rectangle(4, 6)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 0/0 - 4/6")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 0/0 - 2/6")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 0/0 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/0 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_rectangle_update_kwargs(self):
        """testing update method with kwargs in object"""
        r1 = Rectangle(4, 6)
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 0/0 - 4/1")
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/0 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")
        r1.update(x=3, height=5, id=10, y=1, width=7)
        self.assertEqual(str(r1), "[Rectangle] (10) 3/1 - 7/5")

    def test_rectangle_todict(self):
        """tests to_dictionary for rectangle"""
        rdict1 = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertDictEqual(rdict1, r1_dictionary)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/9 - 10/2")
