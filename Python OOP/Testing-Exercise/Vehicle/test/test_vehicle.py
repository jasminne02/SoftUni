import unittest
from unittest import TestCase
from project.vehicle import Vehicle


class VehicleTest(TestCase):
    FUEL = 98.34
    HORSE_POWER = 78.45

    def setUp(self):
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test__init(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test__drive__valid(self):
        kilometers = 10
        self.vehicle.drive(kilometers)
        result = self.vehicle.fuel
        expected_result = self.FUEL - 1.25 * kilometers
        self.assertEqual(expected_result, result)

    def test__drive__invalid(self):
        kilometers = 1230
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(kilometers)
        self.assertIsNotNone(ex)

    def test__refuel_valid(self):
        fuel = 50
        kilometers = 40
        self.vehicle.drive(kilometers)
        self.vehicle.refuel(fuel)
        result = self.vehicle.fuel
        expected_result = self.FUEL - 1.25 * kilometers + fuel
        self.assertEqual(expected_result, result)

    def test__refuel__invalid(self):
        fuel = 120
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(fuel)
        self.assertIsNotNone(ex)

    def test__str(self):
        result = self.vehicle.__str__()
        expected_result = f"The vehicle has {self.HORSE_POWER} " \
                          f"horse power with {self.FUEL} fuel left and 1.25 fuel consumption"


if __name__ == "__main__":
    unittest.main()
