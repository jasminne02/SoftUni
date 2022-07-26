from functools import wraps
from collections import deque


def make_bold(function):
    @wraps(function)
    def wrapper(*args):
        result = function(*args)
        info = deque()
        info.append(result)
        info.appendleft("<b>")
        info.append("</b>")
        return "".join([str(x) for x in list(info)])
    return wrapper


def make_italic(function):
    @wraps(function)
    def wrapper(*args):
        result = function(*args)
        info = deque()
        info.append(result)
        info.appendleft("<i>")
        info.append("</i>")
        return "".join([str(x) for x in list(info)])
    return wrapper


def make_underline(function):
    @wraps(function)
    def wrapper(*args):
        result = function(*args)
        info = deque()
        info.append(result)
        info.appendleft("<u>")
        info.append("</u>")
        return "".join([str(x) for x in list(info)])
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
