from functools import wraps


def logged(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        params = []
        for x in args:
            params.append(str(x))
        for x in kwargs:
            params.append(str(x))
        func_result = function(*args, *kwargs)
        return f"you called {function.__name__}({', '.join(params)})\nit returned {func_result}"
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
