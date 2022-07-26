def multiply(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs) * times
            return result
        return wrapper
    return decorator


@multiply(2)
def add_ten(number):
    return number + 10


print(add_ten(5))
