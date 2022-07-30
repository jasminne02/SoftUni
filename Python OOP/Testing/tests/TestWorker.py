import unittest
from Worker import Worker


class WorkerTests(unittest.TestCase):
    NAME = "Kris"
    SALARY = 2000
    ENERGY = 100

    def setUp(self):
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test__initialization(self):
        self.assertEqual(self.NAME, self.worker.name)
        self.assertEqual(self.SALARY, self.worker.salary)
        self.assertEqual(self.ENERGY, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test__rest__expect_to_increase_energy(self):
        self.worker.rest()
        result = self.worker.energy
        expected_result = self.ENERGY + 1
        self.assertEqual(result, expected_result)

    def test__work__if_energy_is_0_or_less(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertIsNotNone(ex)

        self.worker.energy = -90
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertIsNotNone(ex)

    def test__money__expect_salary_to_be_incremented(self):
        self.worker.work()
        result = self.worker.money
        expected_result = self.SALARY
        self.assertEqual(result, expected_result)

    def test__energy__expect_energy_to_be_decreased_after_work(self):
        self.worker.work()
        result = self.worker.energy
        expected_result = self.ENERGY - 1
        self.assertEqual(result, expected_result)

    def test__get_info(self):
        result = self.worker.get_info()
        expected_result = f'{self.NAME} has saved {self.worker.money} money.'
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
