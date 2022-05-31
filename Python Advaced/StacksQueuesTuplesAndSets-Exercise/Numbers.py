first = set(map(int, input().split(' ')))
second = set(map(int, input().split(' ')))
number = int(input())

for n in range(number):
    commandParts = input().split()
    command = commandParts[0]
    targetSet = commandParts[1]

    if command == 'Add':
        if targetSet == 'First':
            first = first.union([int(x) for x in commandParts[2:]])
        else:
            second = second.union([int(x) for x in commandParts[2:]])
    elif command == 'Remove':
        if targetSet == 'First':
            first = first.difference([int(x) for x in commandParts[2:]])
        else:
            second = second.difference([int(x) for x in commandParts[2:]])
    else:
        print(first.issubset(second) or first.issuperset(second))

print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')
