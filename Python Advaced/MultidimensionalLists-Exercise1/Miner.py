fieldSize = int(input())
commands = input().split(' ')
field = [[x for x in input().split(' ')] for line in range(fieldSize)]

currentMinerRow = 0
currentMinerCol = 0
totalCoals = 0
collectedCoals = 0
succeeded = False
gameOver = False

for r in range(fieldSize):
    for c in range(fieldSize):
        if field[r][c] == 's':
            currentMinerRow = r
            currentMinerCol = c
        elif field[r][c] == 'c':
            totalCoals += 1

for command in commands:
    if command == 'left':
        if currentMinerCol-1 >= 0:
            currentMinerCol -= 1
    elif command == 'right':
        if currentMinerCol+1 <= fieldSize-1:
            currentMinerCol += 1
    elif command == 'up':
        if currentMinerRow-1 >= 0:
            currentMinerRow -= 1
    elif command == 'down':
        if currentMinerRow+1 <= fieldSize-1:
            currentMinerRow += 1

    if field[currentMinerRow][currentMinerCol] == 'c':
        collectedCoals += 1
        field[currentMinerRow][currentMinerCol] = '*'
    elif field[currentMinerRow][currentMinerCol] == 'e':
        gameOver = True
        break

    if collectedCoals == totalCoals:
        succeeded = True
        break

if succeeded:
    print(f'You collected all coal! ({currentMinerRow}, {currentMinerCol})')
elif gameOver:
    print(f'Game over! ({currentMinerRow}, {currentMinerCol})')
else:
    print(f'{totalCoals - collectedCoals} pieces of coal left. ({currentMinerRow}, {currentMinerCol})')
