number = int(input())
longest = set()

for n in range(number):
    f, s = input().split('-')
    firstS, firstE = f.split(',')
    secondS, secondE = s.split(',')
    first = set(range(int(firstS), int(firstE)+1))
    first = set(sorted(first))
    second = set(range(int(secondS), int(secondE)+1))
    second = set(sorted(second))
    intersection = first.intersection(second)

    if len(intersection) > len(longest):
        longest = intersection

print(f'Longest intersection is {[int(x) for x in longest]} with length {len(longest)}')