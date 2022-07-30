import unittest
from unittest import TestCase
from Car import Car


class TestCar(TestCase):
    MAKE = "Tesla"
    MODEL = "A13"
    FUEL_CONSUMPTION = 20
    FUEL_AMOUNT = 590
    FUEL_CAPACITY = 1000

    def setUp(self):
        self.car = Car(self.MAKE, self.MODEL, self.FUEL_CONSUMPTION, self.FUEL_AMOUNT, self.FUEL_CAPACITY)

    def test__init(self):
        self.assertEqual(self.car.make, self.MAKE)
        self.assertEqual(self.car.model, self.MODEL)
        self.assertEqual(self.car.fuel_capacity, self.FUEL_CAPACITY)
        self.assertEqual(self.car.fuel_amount, self.FUEL_AMOUNT)
        self.assertEqual(self.car.fuel_consumption, self.FUEL_CONSUMPTION)

    def test__add_fuel__valid_params(self):
        amount = 340
        self.car.add_fuel(amount)
        result = self.car.fuel_amount
        expected_result = self.FUEL_AMOUNT + amount
        self.assertEqual(result, expected_result)

    def test__add_fuel__invalid_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.add_fuel(-100)
        self.assertIsNotNone(ex)

    def test__add_fuel__no_more_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.add_fuel(900)
        self.assertIsNotNone(ex)

    def test__drive__valid_params(self):
        distance = 120
        self.car.drive(distance)
        result = self.car.fuel_amount
        expected_result = self.FUEL_AMOUNT - distance * self.FUEL_CONSUMPTION
        self.assertEqual(result, expected_result)

    def test__drive__invalid_distance(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(-100)
        self.assertIsNotNone(ex)

    def test__drive__not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)
        self.assertIsNotNone(ex)


if __name__ == "__main__":
    unittest.main()
