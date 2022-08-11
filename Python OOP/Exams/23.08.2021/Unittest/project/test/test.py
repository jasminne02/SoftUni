from project.library import Library
import unittest


class LibraryTest(unittest.TestCase):
    NAME = 'Library'

    def setUp(self):
        self.library = Library(self.NAME)

    def test__init(self):
        self.assertEqual(self.NAME, self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

        self.library.name = 'Lib'
        self.assertEqual('Lib', self.library.name)
        self.library.name = ' '
        self.assertEqual(' ', self.library.name)

        self.library.books_by_authors = {'J.K.': ['Mouse', 'House'], 'E.G.': ['Come']}
        self.assertEqual({'J.K.': ['Mouse', 'House'], 'E.G.': ['Come']}, self.library.books_by_authors)

    def test__name_property__invalid_name__expect_error(self):
        with self.assertRaises(ValueError) as error:
            self.library.name = ''
        self.assertIsNotNone(error.exception)
        self.assertEqual("Name cannot be empty string!", str(error.exception))

    def test__add_book__author_n_title_not_in_books_by_authors(self):
        self.library.add_book('K.L.', 'Egg')
        self.assertEqual({'K.L.': ['Egg']}, self.library.books_by_authors)

    def test__add_book__title_not_in_books_by_authors(self):
        self.library.books_by_authors['S.P.'] = ['Bill']
        self.library.add_book('S.P.', 'Pink')
        self.assertEqual({'S.P.': ['Bill', 'Pink']}, self.library.books_by_authors)

    def test__add_book__title_in_books_by_authors(self):
        self.library.books_by_authors['S.P.'] = ['Bill']
        self.library.add_book('S.P.', 'Bill')
        self.assertEqual({'S.P.': ['Bill']}, self.library.books_by_authors)

    def test__add_reader__name_not_in_readers(self):
        self.library.add_reader('L')
        self.assertEqual({'L': []}, self.library.readers)

    def test__add_reader__name_in_readers(self):
        self.library.readers['M'] = []
        result = self.library.add_reader('M')
        self.assertEqual(f"M is already registered in the {self.NAME} library.", result)

        self.library.add_reader('D')
        result = self.library.add_reader('D')
        self.assertEqual(f"D is already registered in the {self.NAME} library.", result)

    def test__rent_book__reader_name_not_in_readers(self):
        result = self.library.rent_book('Jasmine', 'J.K', 'Pink')
        expected_result = f"Jasmine is not registered in the {self.NAME} Library."
        self.assertEqual(result, expected_result)

    def test__rent_book__book_author_not_in_books_by_authors(self):
        self.library.add_reader('Jasmine')
        result = self.library.rent_book('Jasmine', 'J.K', 'Pink')
        expected_result = f"{self.NAME} Library does not have any J.K's books."
        self.assertEqual(expected_result, result)

    def test__rent_book__book_title_not_in_books_by_authors(self):
        self.library.add_reader('Jasmine')
        self.library.add_book('J.K', 'Blue')
        result = self.library.rent_book('Jasmine', 'J.K', 'Pink')
        expected_result = f"""{self.NAME} Library does not have J.K's "Pink"."""
        self.assertEqual(expected_result, result)

    def test__rent_book(self):
        self.library.add_reader('Jasmine')
        self.library.add_book('J.K', 'Pink')
        self.library.rent_book('Jasmine', 'J.K', 'Pink')
        self.assertEqual({'J.K': []}, self.library.books_by_authors)
        self.assertEqual({'Jasmine': [{'J.K': 'Pink'}]}, self.library.readers)


if __name__ == '__main__':
    unittest.main()
