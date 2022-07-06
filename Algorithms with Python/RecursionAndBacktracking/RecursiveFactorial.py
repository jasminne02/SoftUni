def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number-1)


num = int(input())
print(factorial(num))
