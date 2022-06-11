size = int(input())
field = [[x for x in input().split(' ')] for line in range(size)]

aliceRow = 0
aliceCol = 0
teaCollected = 0

for r in range(size):
    for c in range(size):
        if field[r][c] == 'A':
            aliceRow = r
            aliceCol = c

field[aliceRow][aliceCol] = '*'

while True:
    command = input()

    if command == 'up':
        if aliceRow > 0:
            aliceRow -= 1
    elif command == 'down':
        if aliceRow < size - 1:
            aliceRow += 1
    elif command == 'left':
        if aliceCol > 0:
            aliceCol -= 1
    elif command == 'right':
        if aliceCol < size - 1:
            aliceCol += 1

    if field[aliceRow][aliceCol].isdigit():
        teaCollected += int(field[aliceRow][aliceCol])
    elif field[aliceRow][aliceCol] == 'R':
        print("Alice didn't make it to the tea party.")
        field[aliceRow][aliceCol] = '*'
        break

    field[aliceRow][aliceCol] = '*'

    if teaCollected >= 10:
        print("She did it! She went to the party.")
        break

for r in range(size):
    for c in range(size):
        print(field[r][c], end=' ')
    print()
