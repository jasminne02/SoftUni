def operate(operator, *args):
    result = 0

    if operator == '+':
        for num in args:
            result += num
    elif operator == '-':
        for num in args:
            result -= num
    if operator == '*':
        result = 1
        for num in args:
            result *= num
    if operator == '/':
        for idx in range(len(args)):
            if idx != 0 and args[idx] != 0:
                result /= args[idx]
            elif idx == 0:
                result = args[idx]
            else:
                return 'Invalid operation!'

    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 20, 0))
