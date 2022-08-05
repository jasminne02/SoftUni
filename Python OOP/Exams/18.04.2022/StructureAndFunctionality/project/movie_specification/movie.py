from abc import ABC, abstractmethod
from project.user import User


class Movie(ABC):
    DEFAULT_AGE_RESTRICTION = None
    MIN_YEAR = 1888
    DEFAULT_LIKES = 0

    @abstractmethod
    def __init__(self, title: str, year: int, owner: User, age_restriction=DEFAULT_AGE_RESTRICTION):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = self.DEFAULT_LIKES  # number of movie's likes

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value: str):
        if not value:
            raise ValueError("The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value: int):
        if value < self.MIN_YEAR:
            raise ValueError("Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value: User):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")
        self.__owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value: int):
        if value < self.DEFAULT_AGE_RESTRICTION:
            raise ValueError(f"{self.__class__.__name__} movies must be restricted for audience under {self.DEFAULT_AGE_RESTRICTION} years!")
        self.__age_restriction = value

    def details(self):
        return f"{self.__class__.__name__} - Title:{self.title}, Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"
