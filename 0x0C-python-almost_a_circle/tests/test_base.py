#!/usr/bin/python3
"""import unittest
import Base from models.base
import Square from models.square
import Rectangle from models.rectangle
"""

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import unittest

"""Test Class Base"""


class Test_Bs_BaseId(unittest.TestCase):
    """Test ID """
    # positive nagative id

    def test_pass_id_positive(self):
        """Test id"""
        Base._Base__nb_objects = 0
        Tp0 = Base(12)
        self.assertAlmostEqual(Tp0.id, 12)
        Tp1 = Base()
        self.assertAlmostEqual(Tp1.id, 1)
        Tp2 = Base()
        self.assertAlmostEqual(Tp2.id, 2)
        Tp3 = Base()
        self.assertAlmostEqual(Tp3.id, 3)
        Tp4 = Base()
        self.assertAlmostEqual(Tp4.id, 4)
        Tp5 = Base(None)
        self.assertAlmostEqual(Tp5.id, 5)
        Tp6 = Base(None)
        self.assertAlmostEqual(Tp6.id, 6)
        Tn0 = Base(-12)
        self.assertAlmostEqual(Tn0.id, -12)
        Tn1 = Base()
        self.assertAlmostEqual(Tn1.id, 7)
        Tn2 = Base()
        self.assertAlmostEqual(Tn2.id, 8)
        Tn3 = Base()
        self.assertAlmostEqual(Tn3.id, 9)
        Tn4 = Base()
        self.assertAlmostEqual(Tn4.id, 10)
        Tn5 = Base(None)
        self.assertAlmostEqual(Tn5.id, 11)
        Tn6 = Base(None)
        self.assertAlmostEqual(Tn6.id, 12)

    def test_base_id_zero(self):
        """Test id = 0"""
        Base._Base__nb_objects = 0
        zero1 = Base(0)
        self.assertEqual(zero1.id, 0)


class Test_Bs_ToJsonString(unittest.TestCase):
    """test to json string."""

    def test_to_Json_string(self):
        """Test"""
        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        a = {'x': 2, 'y': 8, 'id': 1, 'height': 7, 'width': 10}
        self.assertEqual(dictionary, a)
        self.assertEqual(type(dictionary), dict)
        b = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]'
        self.assertEqual(json_dictionary, b)
        self.assertEqual(type(json_dictionary), str)

    def test_empty_Dict(self):
        """Test"""
        empty_dic = Base.to_json_string([])
        self.assertEqual(empty_dic, "[]")

    def test_None_Dict(self):
        """Test"""
        empty_dict = Base.to_json_string(None)
        self.assertEqual(empty_dict, "[]")

    def test_two_dict(self):
        """Test"""
        dic1 = {"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}
        dic2 = {"x": 11, "y": 12, "id": 13, "height": 14, "width": 15}
        json_dictionary2 = Base.to_json_string([dic1, dic2])
        j_d2 = '[{"x": 2, "y": 8, "id": 1, '
        j = '"height": 7, "width": 10}, {"x": 11, "y": 12,'
        k = ' "id": 13, "height": 14, "width": 15}]'
        self.assertEqual(json_dictionary2, j_d2 + j + k)

    def test_no_argumant(self):
        """Test"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_many_argument(self):
        """Test"""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 123)


class Test_Bs_save_to_file(unittest.TestCase):
    """Test class method."""

    def test_normal(self):
        """init number object"""
        Base._Base__nb_objects = 0

        # rectangle only
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            c = file.read()
            self.assertAlmostEqual(len(c), 105)
            dd = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}'
            ddd = '{"x": 0, "y": 0, "id": 2, "height": 4, "width": 2}]'
            self.assertEqual(c, dd + ", " + ddd)

        # square only
        s1 = Square(10, 2, 8)
        s2 = Square(2)
        Square.save_to_file([s1, s2])

        with open("Square.json", "r") as file:
            ss = file.read()
            self.assertAlmostEqual(len(ss), 77)
            dddd = '[{"id": 3, "size": 10, "x": 2, "y": 8}, {"id": '
            self.assertEqual(ss, dddd + '4, "size": 2, "x": 0, "y": 0}]')

    def test_None(self):
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            c = file.read()
            self.assertAlmostEqual(len(c), 2)
            self.assertEqual(c, '[]')

        Square.save_to_file(None)

        with open("Square.json", "r") as file:
            s = file.read()
            self.assertAlmostEqual(len(s), 2)
            self.assertEqual(s, '[]')

    def test_empty_list(self):
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r") as file:
            c = file.read()
            self.assertAlmostEqual(len(c), 2)
            self.assertEqual(c, '[]')

        Square.save_to_file([])

        with open("Square.json", "r") as file:
            ss = file.read()
            self.assertAlmostEqual(len(ss), 2)
            self.assertEqual(ss, '[]')


class Test_Bs_from_json_string(unittest.TestCase):
    """Test from_json_string"""

    def test_type(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_rectangle(self):
        """Test"""
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_square(self):
        """Test"""
        list_input = [{'id': 89, 'size': 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_mul_rectangles(self):
        """Test"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 98, 'width': 1, 'height': 8}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_mul_square(self):
        """Test"""
        list_input = [
            {'id': 89, 'size': 4},
            {'id': 98, 'size': 8}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_mul_None(self):
        """Test"""
        self.assertEqual([], Base.from_json_string(None))

    def test_mul_empty(self):
        """Test"""
        self.assertEqual([], Base.from_json_string('[]'))

    def test_mul_no_args(self):
        """Test"""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_mul_too_many_args(self):
        """Test"""
        with self.assertRaises(TypeError):
            Base.from_json_string([], 42)


class Test_Bs_create(unittest.TestCase):
    """test create"""

    def test_create_rectangle(self):
        """Test"""
        dct = {'width': 2, 'height': 4, 'x': 1, 'y': 2, 'id': 42}
        r = Rectangle.create(**dct)
        self.assertDictEqual(r.to_dictionary(), dct)

    def test_create_square(self):
        """Test"""
        dct = {'size': 2, 'x': 1, 'y': 2, 'id': 42}
        s = Square.create(**dct)
        self.assertDictEqual(s.to_dictionary(), dct)


class Test_Bs_load_from_file(unittest.TestCase):
    """Test load_from_file"""

    def test_rectangles(self):
        """Test"""
        r1 = Rectangle(2, 4, 1, 2, 42)
        r2 = Rectangle(4, 2, 2, 1, 24)
        Rectangle.save_to_file([r1, r2])
        lst = Rectangle.load_from_file()
        self.assertDictEqual(lst[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(type(lst[0]), Rectangle)
        self.assertDictEqual(lst[1].to_dictionary(), r2.to_dictionary())
        self.assertEqual(type(lst[1]), Rectangle)

    def test_squares(self):
        """Test"""
        s1 = Square(2, 1, 2, 42)
        s2 = Square(4, 2, 1, 24)
        Square.save_to_file([s1, s2])
        lst = Square.load_from_file()
        self.assertDictEqual(lst[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(type(lst[0]), Square)
        self.assertDictEqual(lst[1].to_dictionary(), s2.to_dictionary())
        self.assertEqual(type(lst[0]), Square)

    def test_No_file(self):
        """Test"""
        Rectangle.save_to_file([])
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])

        Square.save_to_file([])
        lt = Square.load_from_file()
        self.assertEqual(lt, [])

    def test_too_many_args(self):
        """Test"""
        with self.assertRaises(TypeError):
            Base.load_from_file(42)


if __name__ == '__main__':
    unittest.main()
