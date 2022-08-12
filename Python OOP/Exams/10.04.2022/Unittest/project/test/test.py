from project.movie import Movie
import unittest


class MovieTest(unittest.TestCase):
    NAME = 'Ice Age'
    YEAR = 2003
    RATING = 98.7

    def setUp(self):
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)
        self.other_movie = Movie('Tom&Jerry', 1989, 91.2)

    def test__init(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

        self.movie.name = 'Madagascar'
        self.assertEqual('Madagascar', self.movie.name)

    def test__name_property(self):
        with self.assertRaises(ValueError) as error:
            self.movie.name = ''
        self.assertIsNotNone(error.exception)
        self.assertEqual("Name cannot be an empty string!", str(error.exception))

    def test__year_property(self):
        with self.assertRaises(ValueError) as error:
            self.movie.year = 1886
        self.assertIsNotNone(error.exception)
        self.assertEqual("Year is not valid!", str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.movie.year = 0
        self.assertIsNotNone(error.exception)
        self.assertEqual("Year is not valid!", str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.movie.year = -12
        self.assertIsNotNone(error.exception)
        self.assertEqual("Year is not valid!", str(error.exception))

    def test__add_actor__name_not_in_actors(self):
        self.movie.add_actor('Sid')
        self.assertEqual(['Sid'], self.movie.actors)

        self.movie.actors = ['Mannie', 'Diego', 'Peach']
        self.assertEqual(['Mannie', 'Diego', 'Peach'], self.movie.actors)

    def test__add_actor__name_in_actors(self):
        self.movie.actors = ['Mannie', 'Diego', 'Peach']
        result = self.movie.add_actor('Diego')
        self.assertEqual("Diego is already added in the list of actors!", result)

        self.movie.add_actor('Sid')
        result = self.movie.add_actor('Sid')
        self.assertEqual("Sid is already added in the list of actors!", result)

    def test__gt__rating_greater(self):
        result = self.movie > self.other_movie
        self.assertEqual(f'"{self.movie.name}" is better than "{self.other_movie.name}"', result)

        result = self.movie.__gt__(self.other_movie)
        self.assertEqual(f'"{self.movie.name}" is better than "{self.other_movie.name}"', result)

    def test__gt__rating__lower(self):
        self.other_movie.rating = 100
        result = self.movie < self.other_movie
        self.assertEqual(f'"{self.other_movie.name}" is better than "{self.movie.name}"', result)

        result = self.movie.__gt__(self.other_movie)
        self.assertEqual(f'"{self.other_movie.name}" is better than "{self.movie.name}"', result)

    def test__gt(self):
        result = self.movie < self.movie
        self.assertEqual(f'"{self.movie.name}" is better than "{self.movie.name}"', result)

        result = self.movie.__gt__(self.movie)
        self.assertEqual(f'"{self.movie.name}" is better than "{self.movie.name}"', result)

    def test__repr(self):
        expected_result = f"Name: {self.movie.name}\n" \
               f"Year of Release: {self.movie.year}\n" \
               f"Rating: {self.movie.rating:.2f}\n" \
               f"Cast: {', '.join(self.movie.actors)}"
        result = self.movie.__repr__()
        self.assertEqual(expected_result, result)

        self.movie.actors = ['Sid', 'Diego', 'Mannie', 'Peach']
        expected_result = f"Name: {self.movie.name}\n" \
                          f"Year of Release: {self.movie.year}\n" \
                          f"Rating: {self.movie.rating:.2f}\n" \
                          f"Cast: {', '.join(self.movie.actors)}"
        result = self.movie.__repr__()
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
