from project.train.train import Train
import unittest


class TrainTest(unittest.TestCase):
    NAME = 'Train'
    CAPACITY = 30

    def setUp(self):
        self.train = Train(self.NAME, self.CAPACITY)

    def test__init(self):
        self.assertEqual(self.NAME, self.train.name)
        self.assertEqual(self.CAPACITY, self.train.capacity)
        self.assertEqual([], self.train.passengers)

        train = Train("", 0)
        self.assertEqual("", train.name)
        self.assertEqual(0, train.capacity)
        self.assertEqual([], train.passengers)

        train.passengers = ["John", "Maria", "Mario"]
        self.assertEqual(["John", "Maria", "Mario"], train.passengers)

    def test__add__not_enough_capacity__expect_error(self):
        self.train.capacity = 3
        self.train.add("Mike")
        self.train.add("Lilly")
        self.train.add("Paul")

        with self.assertRaises(ValueError) as error:
            self.train.add("John")
        self.assertIsNotNone(error.exception)
        self.assertEqual("Train is full", str(error.exception))

    def test__add__passenger_name_already_exists__expect_error(self):
        self.train.add("Mike")
        self.train.add("Lilly")

        with self.assertRaises(ValueError) as error:
            self.train.add("Mike")
        self.assertIsNotNone(error.exception)
        self.assertEqual("Passenger Mike Exists", str(error.exception))

    def test__add__valid(self):
        result = self.train.add("Mike")
        self.assertEqual("Added passenger Mike", result)

        self.train.add("Lilly")
        self.train.add("Paul")
        self.assertEqual(["Mike", "Lilly", "Paul"], self.train.passengers)

    def test__remove_passenger_name_not_exist__expect_error(self):
        self.train.add("Mike")
        self.train.add("Lilly")
        self.train.add("Paul")
        self.train.add("Daniel")
        self.train.add("Nicolas")

        with self.assertRaises(ValueError) as error:
            self.train.remove("Anna")
        self.assertIsNotNone(error.exception)
        self.assertEqual("Passenger Not Found", str(error.exception))

    def test__remove(self):
        self.train.add("Mike")
        self.train.add("Lilly")
        self.train.add("Paul")
        self.train.add("Daniel")
        self.train.add("Nicolas")

        result = self.train.remove("Mike")
        self.assertEqual("Removed Mike", result)


if __name__ == '__main__':
    unittest.main()
