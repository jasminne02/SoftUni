from project.bookstore import Bookstore
import unittest


class BookstoreTest(unittest.TestCase):
    BOOKS_LIMIT = 10

    def setUp(self):
        self.bookstore = Bookstore(self.BOOKS_LIMIT)

    def test__init(self):
        self.assertEqual(self.BOOKS_LIMIT, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

        with self.assertRaises(AttributeError) as error:
            self.bookstore.total_sold_books = 12
        self.assertIsNotNone(error.exception)

        self.bookstore.availability_in_store_by_book_titles['Roses'] = 12
        self.bookstore.availability_in_store_by_book_titles['Apples'] = 23
        self.assertEqual({'Roses': 12, 'Apples': 23}, self.bookstore.availability_in_store_by_book_titles)

    def test__books_limit_property(self):
        self.bookstore.books_limit = 45
        self.assertEqual(45, self.bookstore.books_limit)

        with self.assertRaises(ValueError) as error:
            self.bookstore.books_limit = 0
        self.assertIsNotNone(error.exception)
        self.assertEqual(f"Books limit of 0 is not valid", str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.bookstore.books_limit = -1
        self.assertIsNotNone(error.exception)
        self.assertEqual(f"Books limit of -1 is not valid", str(error.exception))

    def test__len(self):
        self.bookstore.availability_in_store_by_book_titles['Roses'] = 10
        self.bookstore.availability_in_store_by_book_titles['Apples'] = 5
        self.bookstore.availability_in_store_by_book_titles['Moon'] = 15
        self.assertEqual(30, len(self.bookstore))

        self.bookstore.availability_in_store_by_book_titles['Sand'] = 0
        self.bookstore.availability_in_store_by_book_titles['Rocks'] = -15
        self.assertEqual(15, len(self.bookstore))

    def test__receive_book__not_enough_space__expect_error(self):
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        with self.assertRaises(Exception) as error:
            self.bookstore.receive_book('Green', 12)
        self.assertIsNotNone(error.exception)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)

        self.bookstore.availability_in_store_by_book_titles['Roses'] = 1
        self.bookstore.availability_in_store_by_book_titles['Apples'] = 5
        self.bookstore.availability_in_store_by_book_titles['Moon'] = 1
        with self.assertRaises(Exception) as error:
            self.bookstore.receive_book('Green', 4)
        self.assertIsNotNone(error.exception)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))
        self.assertEqual({'Roses': 1, 'Apples': 5, 'Moon': 1}, self.bookstore.availability_in_store_by_book_titles)

        self.bookstore.books_limit = 15
        self.bookstore.receive_book('Summer', 3)
        self.bookstore.receive_book('Winter', 1)
        self.bookstore.receive_book('Spy', 1)
        with self.assertRaises(Exception) as error:
            self.bookstore.receive_book('Green', 4)
        self.assertIsNotNone(error.exception)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))
        self.assertEqual({'Roses': 1, 'Apples': 5, 'Moon': 1, 'Summer': 3, 'Winter': 1, 'Spy': 1}, self.bookstore.availability_in_store_by_book_titles)

    def test__receive_book__enough_space(self):
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.bookstore.receive_book('Roses', 3)
        self.assertEqual({'Roses': 3}, self.bookstore.availability_in_store_by_book_titles)
        self.bookstore.receive_book('Pink', 4)
        self.assertEqual({'Roses': 3, 'Pink': 4}, self.bookstore.availability_in_store_by_book_titles)

    def test__receive_book__result(self):
        result = self.bookstore.receive_book('Roses', 4)
        self.assertEqual(f"4 copies of Roses are available in the bookstore.", result)
        self.assertEqual({'Roses': 4}, self.bookstore.availability_in_store_by_book_titles)

        result = self.bookstore.receive_book('Pink life', 5)
        self.assertEqual("5 copies of Pink life are available in the bookstore.", result)
        self.assertEqual({'Roses': 4, 'Pink life': 5}, self.bookstore.availability_in_store_by_book_titles)

        result = self.bookstore.receive_book('Roses', 1)
        self.assertEqual("5 copies of Roses are available in the bookstore.", result)
        self.assertEqual({'Roses': 5, 'Pink life': 5}, self.bookstore.availability_in_store_by_book_titles)

    def test__sell_book__book_not_available__expect_error(self):
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book('Roses', 3)
        self.assertIsNotNone(error.exception)
        self.assertEqual(f"Book Roses doesn't exist!", str(error.exception))

        self.bookstore.receive_book('Pink', 3)
        self.bookstore.receive_book('Purple', 4)
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book('Roses', 3)
        self.assertIsNotNone(error.exception)
        self.assertEqual(f"Book Roses doesn't exist!", str(error.exception))

    def test__sell_book__book_not_enough_copies__expect_error(self):
        self.bookstore.receive_book('Roses', 6)
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book('Roses', 8)
        self.assertIsNotNone(error.exception)
        self.assertEqual("Roses has not enough copies to sell. Left: 6", str(error.exception))

        self.bookstore.receive_book('Moon', 0)
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book('Moon', 8)
        self.assertIsNotNone(error.exception)
        self.assertEqual("Moon has not enough copies to sell. Left: 0", str(error.exception))

        self.bookstore.receive_book('Green', 4)
        self.bookstore.sell_book('Green', 3)
        self.assertEqual({'Roses': 6, 'Moon': 0, 'Green': 1}, self.bookstore.availability_in_store_by_book_titles)
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book('Green', 4)
        self.assertIsNotNone(error.exception)
        self.assertEqual("Green has not enough copies to sell. Left: 1", str(error.exception))
        self.assertEqual({'Roses': 6, 'Moon': 0, 'Green': 1}, self.bookstore.availability_in_store_by_book_titles)

    def test__sell_book__sell_successfully(self):
        self.bookstore.receive_book('Summer', 3)
        self.bookstore.receive_book('Winter', 4)
        self.bookstore.receive_book('Spy', 3)
        self.assertEqual({'Summer': 3, 'Winter': 4, 'Spy': 3}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)
        result = self.bookstore.sell_book('Spy', 2)
        self.assertEqual("Sold 2 copies of Spy", result)
        self.assertEqual({'Summer': 3, 'Winter': 4, 'Spy': 1}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(2, self.bookstore.total_sold_books)

        result = self.bookstore.sell_book('Winter', 3)
        self.bookstore.sell_book('Summer', 2)
        self.assertEqual("Sold 3 copies of Winter", result)
        self.assertEqual(7, self.bookstore.total_sold_books)

        self.bookstore.availability_in_store_by_book_titles = {'Book': 3, 'Green': 4}
        result = self.bookstore.sell_book('Green', 2)
        self.assertEqual("Sold 2 copies of Green", result)

        result = self.bookstore.sell_book('Green', 2)
        self.assertEqual("Sold 2 copies of Green", result)
        self.assertEqual({'Book': 3, 'Green': 0}, self.bookstore.availability_in_store_by_book_titles)
        result = str(self.bookstore)
        expected = f"Total sold books: 11\nCurrent availability: 3\n" \
                          f" - Book: 3 copies\n"\
                          f" - Green: 0 copies"
        self.assertEqual(expected, result)

    def test__str(self):
        result = str(self.bookstore)
        expected_result = f"Total sold books: 0\nCurrent availability: 0"
        self.assertEqual(expected_result, result)

        result = self.bookstore.__str__()
        expected_result = f"Total sold books: 0\nCurrent availability: 0"
        self.assertEqual(expected_result, result)

        self.bookstore.receive_book('Rose', 2)
        self.bookstore.receive_book('Green', 7)
        self.bookstore.sell_book('Green', 6)
        self.bookstore.receive_book('Moon', 4)
        self.bookstore.sell_book('Moon', 2)
        self.bookstore.receive_book('Pink', 5)
        result = str(self.bookstore)
        expected_result = f"Total sold books: 8\nCurrent availability: 10\n" \
                          f" - Rose: 2 copies\n"\
                          f" - Green: 1 copies\n"\
                          f" - Moon: 2 copies\n"\
                          f" - Pink: 5 copies"
        self.assertEqual(expected_result, result)

        result = self.bookstore.__str__()
        self.assertEqual(expected_result, result)

        with self.assertRaises(ValueError) as error:
            self.bookstore.books_limit = -1
        self.assertIsNotNone(error.exception)
        self.assertEqual(f"Books limit of -1 is not valid", str(error.exception))
        result = str(self.bookstore)
        expected_result = f"Total sold books: 0\nCurrent availability: 0"
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
