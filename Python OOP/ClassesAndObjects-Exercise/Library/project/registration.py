from project.library import Library
from project.user import User


class Registration:
    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for user in library.user_records:
            if user_id == user.user_id and new_username != user.username:
                if user.username in library.rented_books:
                    library.rented_books[new_username] = library.rented_books[user.username]
                    del library.rented_books[user.username]

                idx = library.user_records.index(user)
                library.user_records.remove(user)
                user.username = new_username
                library.user_records.insert(idx, user)
                return f"Username successfully changed to: {new_username} for user id: {user_id}"
            elif user_id == user.user_id and new_username == user.username:
                return "Please check again the provided username - it should be different than the username used so " \
                       "far! "
        return f"There is no user with id = {user_id}!"



