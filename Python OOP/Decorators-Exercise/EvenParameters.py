from functools import wraps


def even_parameters(function):
    @wraps(function)
    def wrapper(*args):
        only_evens = True
        for x in args:
            try:
                num = int(x)
                if num:
                    if num % 2 != 0:
                        only_evens = False
            except ValueError:
                only_evens = False

        if only_evens:
            return function(*args)
        else:
            return "Please use only even numbers!"
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))

print()


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
