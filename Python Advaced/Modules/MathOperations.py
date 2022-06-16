from MathOperationsPackage import *

num1, sign, num2 = input().split(' ')
result = math_operation(float(num1), float(num2), sign)
print(f'{result:.2f}')
