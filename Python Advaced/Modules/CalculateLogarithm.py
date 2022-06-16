from math import log

number = int(input())
base = input()
logarithm = 0

if base == 'natural':
    logarithm = log(number)
else:
    logarithm = log(number, int(base))

print(f'{logarithm:.2f}')
