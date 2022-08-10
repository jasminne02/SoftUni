from project.pet_shop import PetShop
import unittest


class PetShopTest(unittest.TestCase):
    NAME = 'PetShop'

    def setUp(self):
        self.pet_shop = PetShop(self.NAME)

    def test__init(self):
        self.assertEqual(self.NAME, self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

        pet_shop = PetShop('')
        self.assertEqual('', pet_shop.name)
        self.assertEqual({}, pet_shop.food)
        self.assertEqual([], pet_shop.pets)

    def test__add_food__name_not_in_food_list(self):
        result = self.pet_shop.add_food('cat food', 28.1)
        expected_result = f"Successfully added 28.10 grams of cat food."
        self.assertEqual(expected_result, result)

    def test__add_food__name_in_food_list(self):
        self.pet_shop.food['dog food'] = 0
        result = self.pet_shop.add_food('dog food', 28.8123)
        expected_result = f"Successfully added 28.81 grams of dog food."
        self.assertEqual(expected_result, result)

        self.pet_shop.add_food('cat food', 30)
        result = self.pet_shop.add_food('cat food', 28.8123)
        expected_result = f"Successfully added 28.81 grams of cat food."
        self.assertEqual(expected_result, result)
        self.assertEqual(58.8123, self.pet_shop.food['cat food'])

    def test__add_food__invalid_quantity__expect_error(self):
        with self.assertRaises(ValueError) as error:
            self.pet_shop.add_food('cat food', -1)
        self.assertIsNotNone(error.exception)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.pet_shop.add_food('cat food', 0)
        self.assertIsNotNone(error.exception)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

    def test__add_food__invalid_quantity_str_not_float_expect_error(self):
        with self.assertRaises(TypeError) as error:
            self.pet_shop.add_food('cat food', 'k')
        self.assertIsNotNone(error.exception)

        with self.assertRaises(TypeError) as error:
            self.pet_shop.add_food('cat food', '25')
        self.assertIsNotNone(error.exception)

    def test__add_pet__name_not_in_pets_list(self):
        result = self.pet_shop.add_pet('Kate')
        expected_result = f"Successfully added Kate."
        self.assertEqual(result, expected_result)

    def test__add_pet__name_in_pets_list__expect_error(self):
        self.pet_shop.pets.append('Kate')
        with self.assertRaises(Exception) as error:
            self.pet_shop.add_pet('Kate')
        self.assertIsNotNone(error.exception)
        self.assertEqual("Cannot add a pet with the same name", str(error.exception))

        self.pet_shop.add_pet('Mickey')
        with self.assertRaises(Exception) as error:
            self.pet_shop.add_pet('Mickey')
        self.assertIsNotNone(error.exception)
        self.assertEqual("Cannot add a pet with the same name", str(error.exception))

    def test__add_pet__empty_string_name(self):
        result = self.pet_shop.add_pet('')
        self.assertEqual(f"Successfully added .", result)

    def test__add_pet__name_not_string(self):
        result = self.pet_shop.add_pet(9)
        self.assertEqual(f"Successfully added 9.", result)

    def test__feed_pet__pet_name_not_in_pets_list__expect_error(self):
        with self.assertRaises(Exception) as error:
            self.pet_shop.feed_pet('cat food', 'Cattie')
        self.assertIsNotNone(error.exception)
        self.assertEqual(f"Please insert a valid pet name", str(error.exception))

    def test__feed_pet__food_name_not_in_food_list(self):
        self.pet_shop.add_pet('Cattie')
        result = self.pet_shop.feed_pet('cat food', 'Cattie')
        self.assertEqual(f'You do not have cat food', result)

    def test__feed_pet__food_quantity_lower_than_100(self):
        self.pet_shop.add_pet('Cattie')
        self.pet_shop.add_food('cat food', 50)
        result = self.pet_shop.feed_pet('cat food', 'Cattie')
        self.assertEqual("Adding food...", result)
        self.assertEqual(1050.00, self.pet_shop.food['cat food'])

    def test__feed_pet__food_quantity_greater_than_100(self):
        self.pet_shop.add_pet('Cattie')
        self.pet_shop.add_food('cat food', 150)
        result = self.pet_shop.feed_pet('cat food', 'Cattie')
        self.assertEqual(f"Cattie was successfully fed", result)
        self.assertEqual(50.00, self.pet_shop.food['cat food'])

    def test__repr(self):
        self.pet_shop.add_pet('Cattie')
        self.pet_shop.add_pet('Doggie')
        self.pet_shop.add_pet('Piggie')
        result = self.pet_shop.__repr__()
        expected_result = f'Shop {self.pet_shop.name}:\n' \
                          f'Pets: {", ".join(self.pet_shop.pets)}'
        self.assertEqual(expected_result, result)

    def test__repr__empty_pets_list(self):
        result = self.pet_shop.__repr__()
        expected_result = f'Shop {self.pet_shop.name}:\n' \
                          f'Pets: {", ".join(self.pet_shop.pets)}'
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
