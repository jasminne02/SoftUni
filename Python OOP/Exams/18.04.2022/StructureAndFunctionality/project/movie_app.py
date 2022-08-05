import os

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    USER_EXISTS_ERROR_MESSAGE = 'User already exists!'
    USER_NOT_EXIST_ERROR_MESSAGE = 'This user does not exist!'
    MOVIE_UPLOADED_ERROR_MESSAGE = 'Movie already added to the collection!'

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []
        self.users_by_username = {}

    def register_user(self, username: str, age: int):
        user = self.__get_user_by_username(username)

        if user:
            raise Exception(self.USER_EXISTS_ERROR_MESSAGE)

        user = User(username, age)
        self.users_collection.append(user)
        self.users_by_username[user.username] = user

        return f'{user.username} registered successfully.'

    def upload_movie(self, username: str, movie: Movie):
        user = self.__get_user_by_username(username)

        self.__validate_user_exists(user)
        self.__validate_user_is_movie_owner(user, movie)
        self.__validate_movie_not_uploaded(movie)

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f'{username} successfully added {movie.title} movie.'

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.__get_user_by_username(username)

        self.__validate_movie_uploaded(movie)
        self.__validate_user_is_movie_owner(user, movie)

        movie.title = kwargs.get('title', movie.title)
        movie.year = kwargs.get('year', movie.year)
        movie.age_restriction = kwargs.get('age_restriction', movie.age_restriction)

        return f'{user.username} successfully edited {movie.title} movie.'

    def delete_movie(self, username: str, movie: Movie):
        user = self.__get_user_by_username(username)

        self.__validate_movie_uploaded(movie)
        self.__validate_user_is_movie_owner(user, movie)

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f'{user.username} successfully deleted {movie.title} movie.'

    def like_movie(self, username: str, movie: Movie):
        user = self.__get_user_by_username(username)

        self.__validate_user_is_not_movie_owner(user, movie)
        self.__validate_user_not_liked_movie(user, movie)

        movie.likes += 1
        user.movies_liked.append(movie)
        return f'{user.username} liked {movie.title} movie.'

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__get_user_by_username(username)

        self.__validate_user_liked_movie(user, movie)

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f'{user.username} disliked {movie.title} movie.'

    def display_movies(self):
        if not self.movies_collection:
            return 'No movies found.'

        sorted_movies = sorted(self.movies_collection, key=self.__movie_order_by)
        return os.linesep.join(m.details() for m in sorted_movies)

    def __str__(self):
        result = 'All users: '
        if self.users_collection:
            result = ', '.join(u.username for u in self.users_collection)
        else:
            result += 'No users.'
        result += '\nAll movies: '
        if self.movies_collection:
            result += ', '.join(m.title for m in self.movies_collection)
        else:
            result += 'No movies.'
        return result

    #  PRIVATE METHODS  #

    def __get_user_by_username(self, username) -> User:
        return self.users_by_username.get(username, None)

    def __validate_user_exists(self, user):
        if user is None:
            raise Exception(self.USER_NOT_EXIST_ERROR_MESSAGE)

    def __validate_user_is_movie_owner(self, user: User, movie: Movie):
        if user.username != movie.owner.username:
            raise Exception(self.__build_not_movie_owner_error_message(user, movie))

    def __validate_user_is_not_movie_owner(self, user, movie):
        if user.username == movie.owner.username:
            raise Exception(self.__build_movie_owner_error_message(user, movie))

    def __is_movie_uploaded(self, movie):
        matching_movies = [m for m in self.movies_collection if m == movie]
        return len(matching_movies) > 0

    def __validate_movie_uploaded(self, movie):
        if not self.__is_movie_uploaded(movie):
            raise Exception(self.__build_movie_not_uploaded_error_message(movie))

    def __validate_movie_not_uploaded(self, movie):
        if self.__is_movie_uploaded(movie):
            raise Exception(self.MOVIE_UPLOADED_ERROR_MESSAGE)

    def __validate_user_liked_movie(self, user: User, movie: Movie):
        if movie not in user.movies_liked:
            raise Exception(self.__build_user_not_liked_movie(user, movie))

    def __validate_user_not_liked_movie(self, user: User, movie: Movie):
        if movie in user.movies_liked:
            raise Exception(self.__build_user_liked_movie(user, movie))

    @staticmethod
    def __build_not_movie_owner_error_message(user, movie):
        return f'{user.username} is not the owner of the movie {movie.title}!'

    @staticmethod
    def __build_movie_owner_error_message(user: User, movie: Movie):
        return f'{user.username} is the owner of the movie {movie.title}!'

    @staticmethod
    def __build_movie_not_uploaded_error_message(movie):
        return f'The movie {movie.title} is not uploaded!'

    @staticmethod
    def __build_user_liked_movie(user: User, movie: Movie):
        return f'{user.username} already liked the movie {movie.title}!'

    @staticmethod
    def __build_user_not_liked_movie(user: User, movie: Movie):
        return f'{user.username} has not liked the movie {movie.title}!'

    @staticmethod
    def __movie_order_by(movie: Movie):
        return -movie.year, movie.title
