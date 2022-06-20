def numbers_searching(*args):
    sortedNumbers = set(sorted(args))
    sortedNumbers = list(sortedNumbers)
    missingNumber = ''
    duplicates = []
    returnList = []

    for index in range(1, len(sortedNumbers)):
        previous = sortedNumbers[index-1]
        current = sortedNumbers[index]
        if previous + 1 == current:
            continue
        else:
            missingNumber = previous + 1
            break

    returnList.append(missingNumber)

    for num in args:
        if args.count(num) > 1 and num not in duplicates:
            duplicates.append(num)

    duplicates.sort()
    returnList.append(duplicates)

    return returnList


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
