from project.plantation import Plantation
from unittest import TestCase
import unittest


class PlantationTest(TestCase):
    SIZE = 14

    def setUp(self) -> None:
        self.plantation = Plantation(self.SIZE)

    def test__init(self):
        self.assertEqual(self.SIZE, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test__size__validation(self):
        with self.assertRaises(ValueError) as error:
            Plantation(-2)
        self.assertIsNotNone(error.exception)
        self.assertEqual('Size must be positive number!', str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.plantation.size = -2
        self.assertIsNotNone(error.exception)
        self.assertEqual('Size must be positive number!', str(error.exception))
        self.assertEqual(self.SIZE, self.plantation.size)

    def test__hire_worker(self):
        worker = "John"
        result = self.plantation.hire_worker(worker)
        expected_result = f"{worker} successfully hired."
        self.assertEqual(expected_result, result)

    def test__hire_worker__expect_error(self):
        worker = "John"
        self.plantation.hire_worker(worker)
        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker(worker)
        self.assertIsNotNone(error.exception)
        self.assertEqual("Worker already hired!", str(error.exception))

    def test__len__with_plants(self):
        length = 5
        for n in range(length):
            self.plantation.plants[n] = "o"
        self.assertEqual(length, self.plantation.__len__())

    def test__len__no_plants(self):
        self.assertEqual(0, self.plantation.__len__())

    def test__planting(self):
        worker = "Nick"
        plant = "tree"
        self.plantation.hire_worker(worker)
        self.plantation.plants[worker] = [plant]
        result = self.plantation.planting(worker, plant)
        expected_result = f"{worker} planted {plant}."
        self.assertEqual(expected_result, result)

        worker2 = "John"
        self.plantation.hire_worker(worker2)
        result = self.plantation.planting(worker2, plant)
        expected_result = f"{worker2} planted it's first {plant}."
        self.assertEqual(expected_result, result)

    def test__planting__expect_worker_errors(self):
        worker = "Nick"
        plant = "tree"
        with self.assertRaises(ValueError) as error:
            self.plantation.planting(worker, plant)
        self.assertIsNotNone(error.exception)
        self.assertEqual(f"Worker with name {worker} is not hired!", str(error.exception))

    def test__planting__expect_len_errors(self):
        worker = "Nick"
        plant = "tree"
        self.plantation.hire_worker(worker)
        self.plantation.plants[worker] = "very big plant goes here"
        with self.assertRaises(ValueError) as error:
            self.plantation.planting(worker, plant)
        self.assertIsNotNone(error.exception)
        self.assertEqual("The plantation is full!", str(error.exception))

        self.plantation.plants.pop(worker)
        self.plantation.plants[worker] = '~ huge plant ~'
        with self.assertRaises(ValueError) as error:
            self.plantation.planting(worker, plant)
        self.assertIsNotNone(error.exception)
        self.assertEqual("The plantation is full!", str(error.exception))

    def test__str(self):
        worker1 = "Nick"
        worker2 = "John"
        self.plantation.hire_worker(worker2)
        self.plantation.hire_worker(worker1)
        self.plantation.planting(worker2, "tree")
        self.plantation.planting(worker1, "flower")
        self.plantation.planting(worker1, "grass")
        result = self.plantation.__str__()

        expected_result = [f"Plantation size: {self.SIZE}"]
        expected_result.append(f'{", ".join(self.plantation.workers)}')
        for worker, plants in self.plantation.plants.items():
            expected_result.append(f"{worker} planted: {', '.join(plants)}")
        expected_result = '\n'.join(expected_result)

        self.assertEqual(expected_result, result)

    def test__str__no_plants(self):
        worker1 = "Nick"
        worker2 = "John"
        self.plantation.hire_worker(worker2)
        self.plantation.hire_worker(worker1)
        result = self.plantation.__str__()

        expected_result = [f"Plantation size: {self.SIZE}"]
        expected_result.append(f'{", ".join(self.plantation.workers)}')
        for worker, plants in self.plantation.plants.items():
            expected_result.append(f"{worker} planted: {', '.join(plants)}")
        expected_result = '\n'.join(expected_result)

        self.assertEqual(expected_result, result)

    def test__str__no_workers(self):
        result = self.plantation.__str__()

        expected_result = [f"Plantation size: {self.SIZE}"]
        expected_result.append(f'{", ".join(self.plantation.workers)}')
        for worker, plants in self.plantation.plants.items():
            expected_result.append(f"{worker} planted: {', '.join(plants)}")
        expected_result = '\n'.join(expected_result)

        self.assertEqual(expected_result, result)

    def test__repr__workers(self):
        self.plantation.hire_worker("Nick")
        self.plantation.hire_worker("Daniel")
        self.plantation.hire_worker("Paul")
        result = self.plantation.__repr__()

        expected_result = f'Size: {self.SIZE}\n'
        expected_result += f'Workers: {", ".join(self.plantation.workers)}'
        self.assertEqual(expected_result, result)

    def test__repr__no_worker(self):
        result = self.plantation.__repr__()
        expected_result = ''
        expected_result += f'Size: {self.SIZE}\n'
        expected_result += f'Workers: {", ".join(self.plantation.workers)}'
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
