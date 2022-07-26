from functools import wraps


def even_numbers(function):

    @wraps(function)
    def wrapper(numbers):
        evens = []
        for num in numbers:
            if num % 2 == 0:
                evens.append(num)
        return evens

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
