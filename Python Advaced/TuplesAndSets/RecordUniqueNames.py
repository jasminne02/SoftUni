number = int(input())
uniqueNames = set()

for n in range(number):
    name = input()
    uniqueNames.add(name)

for name in uniqueNames:
    print(name)
