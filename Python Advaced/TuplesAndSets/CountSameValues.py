tt = tuple(float(x) for x in input().split(' '))
ttUnique = list()

for t in tt:
    if t not in ttUnique:
        ttUnique.append(t)

for number in ttUnique:
    count = tt.count(number)

    print(f'{number:.1f} - {count} times')
