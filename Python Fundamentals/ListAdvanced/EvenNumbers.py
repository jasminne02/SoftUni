numbers = list(map(int, input().split(', ')))
evenIndexes = []

for number in range(len(numbers)):
    if numbers[number] % 2 == 0:
        evenIndexes.append(number)

print(evenIndexes)
