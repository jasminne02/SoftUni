import unittest
from unittest import TestCase
from Cat import Cat


class CatTests(TestCase):
    NAME = "Rissie"

    def setUp(self):
        self.cat = Cat(self.NAME)

    def test__size__expect_to_be_increased(self):
        self.cat.eat()
        result = self.cat.size
        expected_result = 1
        self.assertEqual(result, expected_result)

    def test__fed__expect_true_after_eating(self):
        self.cat.eat()
        result = self.cat.fed
        self.assertTrue(result)

    def test__fed__expect_exception_if_already_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertIsNotNone(ex)

    def test__sleep__expect_exception_if_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertIsNotNone(ex)

    def test__sleepy__after_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        result = self.cat.sleepy
        expected_result = False
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
