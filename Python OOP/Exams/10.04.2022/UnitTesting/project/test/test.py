from project.movie import Movie
from unittest import TestCase
import unittest


class MovieTests(TestCase):
    NAME = "Ice Age"
    YEAR = 2003
    RATING = 8.7

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test__init(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test__init__wrong_should_raise_error(self):
        with self.assertRaises(ValueError) as error:
            Movie('', 2002, 9.0)
        self.assertEqual(str(error.exception), "Name cannot be an empty string!")

        with self.assertRaises(ValueError) as error:
            Movie('Ice Age', 1800, 9.8)
        self.assertEqual(str(error.exception), "Year is not valid!")

    def test__add_actor__name_not_in_actors(self):
        actor1 = "Sid"
        actor2 = "Diego"
        self.movie.add_actor(actor1)
        self.movie.add_actor(actor2)
        result = self.movie.actors
        self.assertEqual([actor1, actor2], result)

    def test__add_actor__name_in_actors(self):
        actor = "Sid"
        self.movie.add_actor(actor)
        result = self.movie.add_actor(actor)
        expected_result = f"{actor} is already added in the list of actors!"
        self.assertEqual(expected_result, result)
        self.assertEqual([actor], self.movie.actors)

    def test__gt__true_when_current_rating_is_greater(self):
        other_movie = Movie("Madagascar", 2006, 8.1)
        result = self.movie.__gt__(other_movie)
        expected_result = f'"{self.movie.name}" is better than "{other_movie.name}"'
        self.assertEqual(expected_result, result)

        other_movie = Movie("Tom & Jerry", 1989, 9.6)
        result = self.movie.__gt__(other_movie)
        expected_result = f'"{other_movie.name}" is better than "{self.movie.name}"'
        self.assertEqual(expected_result, result)

    def test__repr(self):
        actors = ['Sid', 'Diego']
        self.movie.actors = actors
        expected_result = f"Name: {self.movie.name}\n" \
               f"Year of Release: {self.movie.year}\n" \
               f"Rating: {self.movie.rating:.2f}\n" \
               f"Cast: {', '.join(self.movie.actors)}"
        self.assertEqual(expected_result, repr(self.movie))


if __name__ == '__main__':
    unittest.main()
