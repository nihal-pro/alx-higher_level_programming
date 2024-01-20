#!/bin/usr/python3
"""import unittest
import Base from models.base
import Square from models.square
import Rectangle from models.rectangle
import StringIO from io
import TestCae and mock from unittest
"""

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
from unittest import TestCase, mock
import unittest
from io import StringIO

"""Test my class Square"""


class Test_Square_task_10(TestCase):
    """test pass arguent and display and str"""

    def test_empty_pass(self):
        """Test"""
        with self.assertRaises(TypeError):
            Square()

    def test_with_argument(self):
        """Test"""
        Base._Base__nb_objects = 0
        # with size.
        t = Square(4)
        self.assertEqual(str(t), "[Square] (1) 0/0 - 4")
        self.assertAlmostEqual(t.area(), 16)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            t.display()
            self.assertEqual(op.getvalue(), "####\n####\n####\n####\n")

        # with size and x
        t1 = Square(2, 2)
        self.assertEqual(str(t1), "[Square] (2) 2/0 - 2")
        self.assertAlmostEqual(t1.area(), 4)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            t1.display()
            self.assertEqual(op.getvalue(), "  ##\n  ##\n")

        # with size and x and y
        t2 = Square(3, 1, 2)
        self.assertEqual(str(t2), "[Square] (3) 1/2 - 3")
        self.assertAlmostEqual(t2.area(), 9)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            t2.display()
            self.assertEqual(op.getvalue(), "\n\n ###\n ###\n ###\n")

        # with size, and x and y and id
        t3 = Square(5, 2, 1, 10)
        self.assertEqual(str(t3), "[Square] (10) 2/1 - 5")
        self.assertAlmostEqual(t3.area(), 25)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            t3.display()
            test = "\n  #####\n  #####\n  #####\n  #####\n  #####\n"
            self.assertEqual(op.getvalue(), test)

    def test_to_many_argument(self):
        """Test"""
        with self.assertRaises(TypeError):
            Square(1, 2, 4, 5, 6)

    def testPassNone(self):
        """Test"""
        with self.assertRaises(TypeError):
            Square(None)

    def test_getter_setter(self):
        """Test"""
        Base._Base__nb_objects = 0
        t = Square(4)
        self.assertAlmostEqual(t.size, 4)

        with self.assertRaises(AttributeError):
            t.__width

        t.size = 22
        self.assertAlmostEqual(t.size, 22)
        # cal area pass size
        self.assertAlmostEqual(t.area(), 484)
        # str Square pass size
        self.assertEqual(str(t), "[Square] (1) 0/0 - 22")
        # get height
        self.assertAlmostEqual(t.height, 22)
        # get width
        self.assertAlmostEqual(t.width, 22)

        # set value
        t = Square(3, 4, 5, 6)
        # get x
        self.assertAlmostEqual(t.x, 4)
        # get y
        self.assertAlmostEqual(t.y, 5)
        # get id
        self.assertAlmostEqual(t.id, 6)


class Test_Square_values_Type_Error(TestCase):
    """test ValueError and TypeError"""
    No_valide_types = [
        None,
        1024.44,
        3j,
        "test",
        ["test", "me"],
        ("test", "me"),
        {"test": 12, "me": 13},
        {"test", "me"},
        True,
        False
    ]

    # TypeError
    def test_size_not_int(self):
        """Test"""
        for T in self.No_valide_types:
            with self.subTest(T=T):
                with self.assertRaisesRegex(TypeError,
                                            "width must be an integer"):
                    Square(T)

    def test_x_not_int(self):
        """Test"""
        for T in self.No_valide_types:
            with self.subTest(T=T):
                with self.assertRaisesRegex(TypeError, "x must be an integer"):
                    Square(6, T)

    def test_y_not_int(self):
        """Test"""
        for T in self.No_valide_types:
            with self.subTest(T=T):
                with self.assertRaisesRegex(TypeError, "y must be an integer"):
                    Square(6, 10, T)

    # ValueError
    def test_size_negative_or_zero(self):
        """Test"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-12)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_x_negative(self):
        """Test"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(12, -2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(11, -55)

    def test_y_negative(self):
        """Test"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(12, 11, -6)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(100, 11, -123)


class Test_Square_area(TestCase):
    """ Test method area """

    def test_area(self):
        """Test"""
        self.assertAlmostEqual(Square(2, 0, 0, 1).area(), 4)
        self.assertAlmostEqual(Square(6, 0, 0, 1).area(), 36)

    def test_area_pass_argu(self):
        """Test"""
        with self.assertRaises(TypeError):
            Square(1, 0, 0, 1).area("test")


class Test_Square_display(TestCase):
    """Test method display """

    def test_display_size(self):
        """Test"""
        with mock.patch('sys.stdout', new=StringIO()) as op:
            Square(3, 0, 0, 12).display()
            self.assertEqual(op.getvalue(), "###\n###\n###\n")

    def test_display_with_x(self):
        """Test"""
        with mock.patch('sys.stdout', new=StringIO()) as op:
            Square(4, 2, 0, 12).display()
            self.assertEqual(op.getvalue(), "  ####\n  ####\n  ####\n  ####\n")

    def test_display_with_y(self):
        """Test"""
        with mock.patch('sys.stdout', new=StringIO()) as op:
            Square(2, 0, 2, 12).display()
            self.assertEqual(op.getvalue(), "\n\n##\n##\n")

    def test_display_with_x_y(self):
        """Test"""
        with mock.patch('sys.stdout', new=StringIO()) as op:
            Square(3, 2, 2).display()
            self.assertEqual(
                op.getvalue(), "\n\n  ###\n  ###\n  ###\n")

    def test_display_with_pass_argument(self):
        """Test"""
        with self.assertRaises(TypeError):
            Square(3, 0, 2, 12).display(5)


class Test_Square_update_args(TestCase):
    """Test method update."""

    def setUp(self):
        """Test"""
        Base._Base__nb_objects = 0

    def test_no_arg_pass(self):
        """Test"""
        T5 = Square(2, 3, 4, 5)
        T5.update()
        self.assertEqual(str(T5), "[Square] (5) 3/4 - 2")

    def test_no_id(self):
        """Test"""
        n = Square(2, 11, 22, 9)
        n.update(None)
        self.assertEqual(str(n), "[Square] (1) 11/22 - 2")

    def test_disply_normal(self):
        """Test"""
        r1 = Square(10, 10, 10)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            print(r1)
            self.assertEqual(op.getvalue(), "[Square] (1) 10/10 - 10\n")

        r1.update(89)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            print(r1)
            self.assertEqual(op.getvalue(), "[Square] (89) 10/10 - 10\n")

        r1.update(89, 2)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            print(r1)
            self.assertEqual(op.getvalue(), "[Square] (89) 10/10 - 2\n")

        r1.update(89, 2, 4)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            print(r1)
            self.assertEqual(op.getvalue(), "[Square] (89) 4/10 - 2\n")

        r1.update(89, 2, 4, 5)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            print(r1)
            self.assertEqual(op.getvalue(), "[Square] (89) 4/5 - 2\n")

    def test_too_many_argu_pass(self):
        """Test"""
        T6 = Square(1, 2, 4, 5)
        T6.update(5, 4, 2, 1, 9)
        self.assertEqual(str(T6), "[Square] (5) 2/1 - 4")


class Test_Square_update_kwargs(TestCase):
    """Test update public method with kwargs"""

    def test_pass_nothing(self):
        """Test"""
        T9 = Square(2, 0, 0, 11)
        T9.update()
        self.assertEqual(str(T9), "[Square] (11) 0/0 - 2")

    def test_pass_id_come_number_and_None(self):
        """Test"""
        T10 = Square(2, 0, 0, 11)
        T10.update(id=None)
        self.assertEqual(str(T10), "[Square] (1) 0/0 - 2")

        T11 = Square(2, 0, 0, 11)
        T11.update(id=66)
        self.assertEqual(str(T11), "[Square] (66) 0/0 - 2")

        T11 = Square(2, 0, 0, 11)
        T11.update(id=None)
        self.assertEqual(str(T11), "[Square] (2) 0/0 - 2")

    def test_pass_id_width(self):
        """Test"""
        T12 = Square(2, 0, 0, 11)
        T12.update(width=11, id=5)
        self.assertEqual(str(T12), "[Square] (5) 0/0 - 11")

    def test_pass_id_width_height(self):
        """Test"""
        T12 = Square(2, 0, 0, 11)
        T12.update(width=11, id=6, height=22)
        self.assertEqual(str(T12), "[Square] (6) 0/0 - 11")

    def test_pass_width_height_x(self):
        """Test"""
        T12 = Square(2, 0, 0, 11)
        T12.update(x=3, width=11, id=2, height=22)
        self.assertEqual(str(T12), "[Square] (2) 3/0 - 11")

    def test_pass_width_height_x_y(self):
        """Test"""
        T12 = Square(2, 0, 0, 11)
        T12.update(x=3, width=11, y=2, id=9, height=22)
        self.assertEqual(str(T12), "[Square] (9) 3/2 - 11")

    def test_pass_too_many_arg(self):
        """Test"""
        T12 = Square(1, 0, 0, 1)
        T12.update(x=2, width=3, y=4, id=5, height=6, test=1000)
        self.assertEqual(str(T12), "[Square] (5) 2/4 - 3")

    def test_pass_too_many_arg_mixed(self):
        """Test"""
        T12 = Square(1, 0, 0, 1)
        T12.update(x=2, hj=1002, width=3, y=4,
                   k=1001, id=5, height=6, test=1000)
        self.assertEqual(str(T12), "[Square] (5) 2/4 - 3")

    def test_pass_args_and_kwargs(self):
        """Test"""
        T12 = Square(1, 0, 0, 1)
        T12.update(11, 33, 44, 55, x=2, width=3, y=4, id=5, height=6)
        self.assertEqual(str(T12), "[Square] (11) 44/55 - 33")

    def test_pass_wrong_key(self):
        """Test"""
        T12 = Square(1, 0, 0, 1)
        T12.update(test=1000, e=1001, med=1002, x1=1002, y2=1003)
        self.assertEqual(str(T12), "[Square] (1) 0/0 - 1")

    def test_value_type_error_pass_negative_number(self):
        """Test"""
        r = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError) as err:
            r.update(1, [1, 2])
        self.assertEqual(str(err.exception), "width must be an integer")

        with self.assertRaises(ValueError) as err:
            r.update(1, -1)
        self.assertEqual(str(err.exception), "width must be > 0")

        with self.assertRaises(TypeError) as err:
            r.update(size=(1, 2))
        self.assertEqual(str(err.exception), "width must be an integer")

        with self.assertRaises(ValueError) as err:
            r.update(size=-1)
        self.assertEqual(str(err.exception), "width must be > 0")


class Test_Square_to_dictionary(TestCase):
    """Test dict"""

    def setUp(self):
        """Test"""
        Base._Base__nb_objects = 0

    def test_normalTest(self):
        """Test"""
        r1 = Square(10, 1, 9)
        self.assertEqual(str(r1), "[Square] (1) 1/9 - 10")
        r1_dictionary = r1.to_dictionary()
        shoud_be = "{'id': 1, 'size': 10, 'x': 1, 'y': 9}"
        self.assertEqual(str(r1_dictionary), shoud_be)
        self.assertEqual(type(r1_dictionary), dict)

        r2 = Square(1)
        self.assertEqual(str(r2), "[Square] (2) 0/0 - 1")
        r2.update(**r1_dictionary)
        self.assertEqual(str(r2), "[Square] (1) 1/9 - 10")
        self.assertEqual(r1 == r2, False)

    def test_to_dict_pass_argument(self):
        """Test"""
        r = Square(1, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.to_dictionary(11)


if __name__ == '__main__':
    unittest.main()
