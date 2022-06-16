def math_operation(num1, num2, sign):
    if sign == '/' and num2 != 0:
        return num1 / num2
    elif sign == '*':
        return num1 * num2
    elif sign == '-':
        return num1 - num2
    elif sign == '+':
        return num1 + num2
    elif sign == '^':
        return num1 ** num2
