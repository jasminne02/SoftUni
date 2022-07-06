def has_uppercase_letter(password):
    for idx in range(len(password)):
        if 65 <= ord(password[idx]) <= 90:
            return True
    return False


def has_digit(password):
    for idx in range(len(password)):
        if password[idx] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            return True
    return False


class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def __str__(self):
        return f"You have a profile with username: \"{self.__username}\" and password: {'*' * len(self.__password)}"

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) < 8 or not has_uppercase_letter(value) or not has_digit(value):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 "
                             "uppercase letter.")
        self.__password = value


profile_with_invalid_password = Profile('My_username', 'My-password')
print()
profile_with_invalid_username = Profile('Too_long_username', 'Any')
print()
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
