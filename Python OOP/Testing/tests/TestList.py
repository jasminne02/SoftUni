import unittest
from unittest import TestCase
from List import IntegerList


class TestList(TestCase):
    LIST = [3, 4, 5, 6]

    def setUp(self):
        list = self.LIST.copy()
        self.list = IntegerList(list)

    def test__add__integer(self):
        result = self.list.add(9)
        expected_result = self.LIST + [9]
        self.assertEqual(result, expected_result)

    def test__add__not_integer(self):
        with self.assertRaises(ValueError) as ex:
            self.list.add("f")
        self.assertIsNotNone(ex)

    def test__remove_index__valid(self):
        index = 0
        result = self.list.remove_index(index)
        self.LIST.pop(index)
        expected_value = self.LIST
        self.assertEqual(result, expected_value)

    def test__remove_index__invalid(self):
        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(-2)
        self.assertIsNotNone(ex)

    def test__init_valid(self):
        expected_result = self.LIST
        result = self.list.list
        self.assertEqual(result, expected_result)

    def test__init__invalid(self):
        with self.assertRaises(ValueError) as ex:
            IntegerList(["dsj", "sr", "po"])
        self.assertIsNotNone(ex)

    def test__get__valid(self):
        index = 0
        result = self.list.get(index)
        expected_value = self.LIST[index]
        self.assertEqual(result, expected_value)

    def test__get__invalid(self):
        with self.assertRaises(IndexError) as ex:
            self.list.get(-2)
        self.assertIsNotNone(ex)

    def test__insert__valid(self):
        self.list.insert(0, 9)
        result = self.list.list
        expected_value = [9, 3, 4, 5, 6]
        self.assertEqual(result, expected_value)

    def test__insert__invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.list.insert(-7, 0)
        self.assertIsNotNone(ex)

    def test__insert__invalid_value(self):
        with self.assertRaises(ValueError) as ex:
            self.list.insert(1, "p")
        self.assertIsNotNone(ex)

    def test__get_biggest(self):
        result = self.list.get_biggest()
        expected_result = 6
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
