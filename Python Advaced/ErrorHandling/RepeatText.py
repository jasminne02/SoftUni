text = input()

try:
    times = int(input())
    print(text * times)
except (TypeError, ValueError):
    print('Variable times must be an integer')
