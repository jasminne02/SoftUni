number = int(input())
elements = set()

for n in range(number):
    line = input().split(' ')

    for el in line:
        elements.add(el)

[print(el) for el in elements]