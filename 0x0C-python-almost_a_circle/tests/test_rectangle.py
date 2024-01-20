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

""" test my classes Rectangle"""


class Test_Rectangle_task_2(TestCase):
    """Test pass argument, and getter - setter."""

    def test_empty(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg_pass(self):
        with self.assertRaises(TypeError):
            Rectangle(6)

    def test_to_many_arg_pass(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 32, 0, 0, 15, 61)

    def test_pass_None(self):
        with self.assertRaises(TypeError):
            Rectangle(None)

    def setUp(self):
        # problem initialize n_object
        Base._Base__nb_objects = 0

    def test_no_id_pass_or_None(self):
        self.assertAlmostEqual(Rectangle(2, 3, 0, 0).id, 1)
        self.assertAlmostEqual(Rectangle(2, 3, 0, 0).id, 2)
        self.assertAlmostEqual(Rectangle(2, 3, 0, 0, None).id, 3)

    def test_with_id_pass(self):
        self.assertAlmostEqual(Rectangle(2, 3, 0, 0, 12).id, 12)
        self.assertAlmostEqual(Rectangle(2, 3, 0, 0, -2).id, -2)

    def test_privet_width_get_and_set(self):
        T = Rectangle(1, 2)
        # privet attribute
        with self.assertRaises(AttributeError):
            T.__width
        # getter Test
        self.assertAlmostEqual(T.width, 1)
        T.width = 66
        self.assertAlmostEqual(T.width, 66)

    def test_privet_height_get_and_set(self):
        T = Rectangle(1, 2)
        # privet attribute
        with self.assertRaises(AttributeError):
            T.__height
        # getter Test
        self.assertAlmostEqual(T.height, 2)
        T.height = 55
        self.assertAlmostEqual(T.height, 55)

    def test_privet_x_get_and_set(self):
        T = Rectangle(1, 2, 3, 4)
        # privet attribute
        with self.assertRaises(AttributeError):
            T.__x
        # getter Test
        self.assertAlmostEqual(T.x, 3)
        T.x = 678
        self.assertAlmostEqual(T.x, 678)

    def test_privet_y_get_and_set(self):
        T = Rectangle(1, 2, 3, 4)
        # privet attribute
        with self.assertRaises(AttributeError):
            T.__y
        # getter Test
        self.assertAlmostEqual(T.y, 4)
        T.y = 100
        self.assertAlmostEqual(T.y, 100)


class Test_Rectangle_task_3(TestCase):
    """ Test ValueError and TypeError """
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
    def test_width_not_int(self):
        for T in self.No_valide_types:
            with self.subTest(T=T):
                with self.assertRaisesRegex(TypeError,
                                            "width must be an integer"):
                    Rectangle(T, 4)

    def test_height_not_int(self):
        for T in self.No_valide_types:
            with self.subTest(T=T):
                with self.assertRaisesRegex(TypeError,
                                            "height must be an integer"):
                    Rectangle(6, T)

    def test_x_not_int(self):
        for T in self.No_valide_types:
            with self.subTest(T=T):
                with self.assertRaisesRegex(TypeError, "x must be an integer"):
                    Rectangle(6, 7, T)

    def test_y_not_int(self):
        for T in self.No_valide_types:
            with self.subTest(T=T):
                with self.assertRaisesRegex(TypeError, "y must be an integer"):
                    Rectangle(6, 10, 1, T)

    # ValueError
    def test_width_negative_or_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-12, 11)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 11)

    def test_height_negative_or_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(12, -11)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(11, 0)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(12, 11, -2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(11, 11, -55)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(12, 11, 1, -6)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(100, 11, 9, -123)


class Test_Rectangle_area(TestCase):
    """ Test method area """

    def test_area(self):
        self.assertAlmostEqual(Rectangle(2, 3, 0, 0, 1).area(), 6)
        self.assertAlmostEqual(Rectangle(6, 6, 0, 0, 1).area(), 36)

    def test_area_pass_argu(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 0, 0, 1).area("test")


class Test_Rectangle_display(TestCase):
    """Test method display """

    def test_display_width_height(self):
        with mock.patch('sys.stdout', new=StringIO()) as op:
            Rectangle(3, 4, 0, 0, 12).display()
            self.assertEqual(op.getvalue(), "###\n###\n###\n###\n")

    def test_display_with_x(self):
        with mock.patch('sys.stdout', new=StringIO()) as op:
            Rectangle(3, 4, 2, 0, 12).display()
            self.assertEqual(op.getvalue(), "  ###\n  ###\n  ###\n  ###\n")

    def test_display_with_y(self):
        with mock.patch('sys.stdout', new=StringIO()) as op:
            Rectangle(3, 4, 0, 2, 12).display()
            self.assertEqual(op.getvalue(), "\n\n###\n###\n###\n###\n")

    def test_display_with_x_y(self):
        with mock.patch('sys.stdout', new=StringIO()) as op:
            Rectangle(3, 4, 3, 2, 12).display()
            self.assertEqual(
                op.getvalue(), "\n\n   ###\n   ###\n   ###\n   ###\n")

    def test_display_with_pass_argument(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 4, 0, 2, 12).display(5)


class Test_Rectangle_str(TestCase):
    """test method str"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test__str_normal(self):
        with mock.patch('sys.stdout', new=StringIO()) as op:
            print(Rectangle(4, 6, 2, 1, 12))
            self.assertEqual(op.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")
        with mock.patch('sys.stdout', new=StringIO()) as op:
            print(Rectangle(5, 5, 0, 0, 120))
            self.assertEqual(op.getvalue(), "[Rectangle] (120) 0/0 - 5/5\n")
        with mock.patch('sys.stdout', new=StringIO()) as op:
            print(Rectangle(5, 5))
            self.assertEqual(op.getvalue(), "[Rectangle] (1) 0/0 - 5/5\n")
        with mock.patch('sys.stdout', new=StringIO()) as op:
            print(Rectangle(5, 5))
            self.assertEqual(op.getvalue(), "[Rectangle] (2) 0/0 - 5/5\n")

    def test_str_method(self):
        T2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(T2.__str__(), "[Rectangle] (5) 3/4 - 1/2")

        T3 = Rectangle(1, 2)
        self.assertEqual(T3.__str__(), "[Rectangle] (1) 0/0 - 1/2")

    def test_str_str(self):
        T4 = Rectangle(5, 4, 3, 2, 1)
        self.assertEqual(str(T4), "[Rectangle] (1) 3/2 - 5/4")

        T5 = Rectangle(2, 1)
        self.assertEqual(str(T5), "[Rectangle] (1) 0/0 - 2/1")

    def test_str_pass_argumant(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5).__str__(123)


class Test_Rectangle_update_args(TestCase):
    """Test method update."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_no_arg_pass(self):
        T5 = Rectangle(1, 2, 3, 4, 5)
        T5.update()
        self.assertEqual(str(T5), "[Rectangle] (5) 3/4 - 1/2")

    def test_no_id(self):
        T8 = Rectangle(1, 2, 3, 4, 5)
        T8.update(None)
        self.assertEqual(str(T8), "[Rectangle] (1) 3/4 - 1/2")

    def test_disply_normal(self):
        r1 = Rectangle(10, 10, 10, 10)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            print(r1)
            self.assertEqual(op.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")

        r1.update(89)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            print(r1)
            self.assertEqual(op.getvalue(), "[Rectangle] (89) 10/10 - 10/10\n")

        r1.update(89, 2)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            print(r1)
            self.assertEqual(op.getvalue(), "[Rectangle] (89) 10/10 - 2/10\n")

        r1.update(89, 2, 3)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            print(r1)
            self.assertEqual(op.getvalue(), "[Rectangle] (89) 10/10 - 2/3\n")

        r1.update(89, 2, 3, 4)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            print(r1)
            self.assertEqual(op.getvalue(), "[Rectangle] (89) 4/10 - 2/3\n")

        r1.update(89, 2, 3, 4, 5)
        with mock.patch('sys.stdout', new=StringIO()) as op:
            print(r1)
            self.assertEqual(op.getvalue(), "[Rectangle] (89) 4/5 - 2/3\n")

    def test_too_many_argu_pass(self):
        T6 = Rectangle(1, 2, 3, 4, 5)
        T6.update(5, 4, 7, 2, 1, 9)
        self.assertEqual(str(T6), "[Rectangle] (5) 2/1 - 4/7")


class Test_Rectangle_update_kwargs(TestCase):
    """Test update public method with kwargs"""

    def test_pass_nothing(self):
        T9 = Rectangle(2, 3, 0, 0, 11)
        T9.update()
        self.assertEqual(str(T9), "[Rectangle] (11) 0/0 - 2/3")

    def test_pass_id_come_number_and_None(self):
        T10 = Rectangle(2, 3, 0, 0, 11)
        T10.update(id=None)
        self.assertEqual(str(T10), "[Rectangle] (1) 0/0 - 2/3")

        T11 = Rectangle(2, 3, 0, 0, 11)
        T11.update(id=66)
        self.assertEqual(str(T11), "[Rectangle] (66) 0/0 - 2/3")

        T11 = Rectangle(2, 3, 0, 0, 11)
        T11.update(id=None)
        self.assertEqual(str(T11), "[Rectangle] (2) 0/0 - 2/3")

    def test_pass_id_width(self):
        T12 = Rectangle(2, 3, 0, 0, 11)
        T12.update(width=11, id=5)
        self.assertEqual(str(T12), "[Rectangle] (5) 0/0 - 11/3")

    def test_pass_id_width_height(self):
        T12 = Rectangle(2, 3, 0, 0, 11)
        T12.update(width=11, id=6, height=22)
        self.assertEqual(str(T12), "[Rectangle] (6) 0/0 - 11/22")

    def test_pass_width_height_x(self):
        T12 = Rectangle(2, 3, 0, 0, 11)
        T12.update(x=3, width=11, id=2, height=22)
        self.assertEqual(str(T12), "[Rectangle] (2) 3/0 - 11/22")

    def test_pass_width_height_x_y(self):
        T12 = Rectangle(2, 3, 0, 0, 11)
        T12.update(x=3, width=11, y=2, id=9, height=22)
        self.assertEqual(str(T12), "[Rectangle] (9) 3/2 - 11/22")

    def test_pass_too_many_arg(self):
        T12 = Rectangle(1, 1, 0, 0, 1)
        T12.update(x=2, width=3, y=4, id=5, height=6, test=1000)
        self.assertEqual(str(T12), "[Rectangle] (5) 2/4 - 3/6")

    def test_pass_too_many_arg_mixed(self):
        T12 = Rectangle(1, 1, 0, 0, 1)
        T12.update(x=2, hj=1002, width=3, y=4,
                   k=1001, id=5, height=6, test=1000)
        self.assertEqual(str(T12), "[Rectangle] (5) 2/4 - 3/6")

    def test_pass_args_and_kwargs(self):
        T12 = Rectangle(1, 1, 0, 0, 1)
        T12.update(11, 22, 33, 44, 55, x=2, width=3, y=4, id=5, height=6)
        self.assertEqual(str(T12), "[Rectangle] (11) 44/55 - 22/33")

    def test_pass_wrong_key(self):
        T12 = Rectangle(1, 1, 0, 0, 1)
        T12.update(test=1000, e=1001, med=1002, x1=1002, y2=1003)
        self.assertEqual(str(T12), "[Rectangle] (1) 0/0 - 1/1")

    def test_value_type_error_pass_negative_number(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError) as err:
            r.update(1, [1, 2])
        self.assertEqual(str(err.exception), "width must be an integer")

        with self.assertRaises(ValueError) as err:
            r.update(1, -1)
        self.assertEqual(str(err.exception), "width must be > 0")

        with self.assertRaises(TypeError) as err:
            r.update(height=[1, 2])
        self.assertEqual(str(err.exception), "height must be an integer")

        with self.assertRaises(ValueError) as err:
            r.update(height=-1)
        self.assertEqual(str(err.exception), "height must be > 0")


class Test_rectangle_to_dictionary(TestCase):
    """Test dict"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_normalTest(self):
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/9 - 10/2")
        r1_dictionary = r1.to_dictionary()
        shoud_be = "{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}"
        self.assertEqual(str(r1_dictionary), shoud_be)
        self.assertEqual(type(r1_dictionary), dict)

        r2 = Rectangle(1, 1)
        self.assertEqual(str(r2), "[Rectangle] (2) 0/0 - 1/1")
        r2.update(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/9 - 10/2")
        self.assertEqual(r1 == r2, False)

    def test_to_dict_pass_argument(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.to_dictionary(11)


if __name__ == '__main__':
    unittest.main()
