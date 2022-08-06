from project.factory.paint_factory import PaintFactory
import unittest


class PaintFactoryTest(unittest.TestCase):
    NAME = 'Colors'
    CAPACITY = 45

    def setUp(self):
        self.paint_factory = PaintFactory(self.NAME, self.CAPACITY)

    def test__initialisation(self):
        self.assertEqual(self.NAME, self.paint_factory.name)
        self.assertEqual(self.CAPACITY, self.paint_factory.capacity)
        self.assertEqual({}, self.paint_factory.ingredients)

    def test__add_ingredient__valid_ingredient_can_be_added_already_exists(self):
        self.paint_factory.add_ingredient("white", 23)
        self.paint_factory.add_ingredient("red", 3)
        self.paint_factory.add_ingredient("white", 12)
        result = self.paint_factory.ingredients["white"]
        self.assertEqual(35, result)

    def test__add_ingredient__valid_ingredient_can_be_added_not_exist(self):
        self.paint_factory.add_ingredient("white", 23)
        result = self.paint_factory.ingredients["white"]
        self.assertEqual(23, result)

    def test__add_ingredient__valid_ingredient_cannot_be_added__expect_error(self):
        with self.assertRaises(ValueError) as error:
            self.paint_factory.add_ingredient("blue", 75)
        self.assertIsNotNone(error.exception)
        self.assertEqual("Not enough space in factory", str(error.exception))

    def test__add_ingredient__invalid_ingredient__expect_error(self):
        product_type = "black"
        with self.assertRaises(TypeError) as error:
            self.paint_factory.add_ingredient(product_type, 5)
        self.assertIsNotNone(error.exception)
        self.assertEqual(f"Ingredient of type {product_type} not allowed in PaintFactory", str(error.exception))

    def test__remove_ingredient__exist_quantity_greater_than_0(self):
        self.paint_factory.add_ingredient("blue", 19)
        self.paint_factory.remove_ingredient("blue", 16)
        result = self.paint_factory.ingredients["blue"]
        self.assertEqual(3, result)

    def test__remove_ingredient__exist_quantity_equal_to_0(self):
        self.paint_factory.add_ingredient("blue", 19)
        self.paint_factory.remove_ingredient("blue", 19)
        result = self.paint_factory.ingredients["blue"]
        self.assertEqual(0, result)

    def test__remove_ingredient__exist_invalid_quantity__expect__error(self):
        self.paint_factory.add_ingredient("blue", 13)
        with self.assertRaises(ValueError) as error:
            self.paint_factory.remove_ingredient("blue", 16)
        self.assertIsNotNone(error.exception)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(error.exception))

    def test__remove_ingredient__not_exist__expect__error(self):
        with self.assertRaises(KeyError) as error:
            self.paint_factory.remove_ingredient("blue", 18)
        self.assertIsNotNone(error.exception)
        # self.assertEqual("No such ingredient in the factory", str(error.exception))

    def test__products__with_ingredients(self):
        self.paint_factory.add_ingredient("green", 3)
        self.paint_factory.add_ingredient("yellow", 1)
        self.paint_factory.add_ingredient("green", 5)
        result = self.paint_factory.products
        expected_result = {"green": 8, "yellow": 1}
        self.assertEqual(expected_result, result)

    def test__products__with_no_ingredients(self):
        result = self.paint_factory.products
        self.assertEqual({}, result)

    def test__can_add__capacity_greater_than_0(self):
        result = self.paint_factory.can_add(30)
        self.assertTrue(result)

        self.paint_factory.add_ingredient("white", 28)
        self.paint_factory.add_ingredient("red", 2)
        result = self.paint_factory.can_add(10)
        self.assertTrue(result)

    def test__can_add__capacity_equal_to_0(self):
        self.paint_factory.add_ingredient("white", 28)
        self.paint_factory.add_ingredient("red", 2)
        self.paint_factory.add_ingredient("blue", 5)
        result = self.paint_factory.can_add(10)
        self.assertTrue(result)

    def test__can_add__capacity_lower_than_0(self):
        self.paint_factory.add_ingredient("white", 28)
        self.paint_factory.add_ingredient("red", 15)
        result = self.paint_factory.can_add(57)
        self.assertFalse(result)

    def test__repr__with_ingredients(self):
        self.paint_factory.add_ingredient("white", 28)
        self.paint_factory.add_ingredient("red", 15)
        self.paint_factory.add_ingredient("blue", 1)
        result = self.paint_factory.__repr__()
        expected_result = f"Factory name: {self.paint_factory.name} with capacity {self.paint_factory.capacity}.\n"
        expected_result += f"white: 28\nred: 15\nblue: 1\n"
        self.assertEqual(expected_result, result)

    def test__repr__with_one_ingredient(self):
        self.paint_factory.add_ingredient("white", 28)
        result = self.paint_factory.__repr__()
        expected_result = f"Factory name: {self.paint_factory.name} with capacity {self.paint_factory.capacity}.\n"
        expected_result += f"white: 28\n"
        self.assertEqual(expected_result, result)

    def test__repr__with_no_ingredients(self):
        result = self.paint_factory.__repr__()
        expected_result = f"Factory name: {self.paint_factory.name} with capacity {self.paint_factory.capacity}.\n"
        for ingredient in self.paint_factory.ingredients:
            result += f"{ingredient}: {self.paint_factory.ingredients[ingredient]}\n"
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
