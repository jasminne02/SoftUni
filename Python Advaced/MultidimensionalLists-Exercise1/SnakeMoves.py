rows, columns = tuple(map(int, input().split(' ')))
word = input()
idx = 0

for row in range(rows):
    elements = [None] * columns
    if row % 2 == 0:
        for col in range(columns):
            elements[col] = word[idx % len(word)]
            idx += 1
    else:
        for col in range(columns - 1, -1, -1):
            elements[col] = word[idx % len(word)]
            idx += 1
    print(''.join(elements))
