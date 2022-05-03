operator_input = input()
x = int(input())
y = int(input())


def calculate(first, second, operator):
    if operator == 'multiply':
        return first * second
    elif operator == 'divide':
        return int(first / second)
    elif operator == 'add':
        return first + second
    elif operator == 'subtract':
        return first - second


print(calculate(x, y, operator_input))
