number = int(input())
evens = set()
odds = set()

for n in range(1, number + 1):
    name = input()
    asciiSum = 0

    for ch in name:
        asciiSum += ord(ch)

    asciiSum /= n
    asciiSum = int(asciiSum)
    if asciiSum % 2 == 0:
        evens.add(asciiSum)
    elif asciiSum % 2 != 0:
        odds.add(asciiSum)

evenSum = sum(evens)
oddSum = sum(odds)

if evenSum == oddSum:
    union = list(evens.union(odds))
    for i in range(len(union)):
        if i == len(union) - 1:
            print(union[i])
        else:
            print(union[i], end=', ')
elif oddSum > evenSum:
    diff = list(odds.difference(evens))
    for i in range(len(diff)):
        if i == len(diff) - 1:
            print(diff[i])
        else:
            print(diff[i], end=', ')
elif evenSum > oddSum:
    diff = list(evens.symmetric_difference(odds))
    for i in range(len(diff)):
        if i == len(diff) - 1:
            print(diff[i])
        else:
            print(diff[i], end=', ')
