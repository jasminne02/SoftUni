year = int(input())
happyYear = False

while not happyYear:
    year += 1
    strYear = str(year)
    setYear = set()

    for i in range(len(strYear)):
        setYear.add(strYear[i])

    happyYear = len(strYear) == len(setYear)

print(year)
