import math
from collections import deque

expression = deque(input().split(' '))
operators = ['*', '+', '-', '/']
numbers = list()
result = ''

while expression:
    currentElement = expression.popleft()
    operator = ''

    if currentElement in operators:
        operator = currentElement
    else:
        numbers.append(int(currentElement))

    if operator != '':
        if result != '':
            numbers.insert(0, result)

        for i in range(len(numbers)):
            if i == 0:
                result = numbers[i]
            elif operator == '*':
                result *= numbers[i]
            elif operator == '+':
                result += numbers[i]
            elif operator == '-':
                result -= numbers[i]
            elif operator == '/':
                result /= numbers[i]
                result = math.floor(result)

        numbers = []

print(result)
