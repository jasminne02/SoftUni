import unittest
from unittest import TestCase
from project.mammal import Mammal


class TestMammal(TestCase):
    NAME = "Tommie"
    SOUND = "meow"
    TYPE = "cat"

    def setUp(self):
        self.mammal = Mammal(self.NAME, self.TYPE, self.SOUND)

    def test__init(self):
        self.assertEqual(self.NAME, self.mammal.name)
        self.assertEqual(self.SOUND, self.mammal.sound)
        self.assertEqual(self.TYPE, self.mammal.type)

    def test__make_sound(self):
        result = self.mammal.make_sound()
        expected_result = f"{self.NAME} makes {self.SOUND}"
        self.assertEqual(expected_result, result)

    def test__get_kingdom(self):
        result = self.mammal.get_kingdom()
        expected_result = "animals"
        self.assertEqual(expected_result, result)

    def test__info(self):
        result = self.mammal.info()
        expected_result = f"{self.NAME} is of type {self.TYPE}"
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
