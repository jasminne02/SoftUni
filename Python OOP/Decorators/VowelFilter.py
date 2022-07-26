from functools import wraps


def vowel_filter(function):

    @wraps(function)
    def wrapper():
        vowels = []
        for letter in function():
            if letter in ["a", "e", "y", "u", "i", "o"]:
                vowels.append(letter)
        return vowels

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
