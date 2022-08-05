from project.movie_specification.movie import Movie
from project.user import User


class Action(Movie):
    DEFAULT_AGE_RESTRICTION = 12

    def __init__(self, title: str, year: int, owner: User, age_restriction=DEFAULT_AGE_RESTRICTION):
        super().__init__(title, year, owner, age_restriction)

