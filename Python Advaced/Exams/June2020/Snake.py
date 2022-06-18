size = int(input())
matrix = [[el for el in input()] for line in range(size)]

snakeRow = 0
snakeCol = 0
burrowFound = False
firstBurrowRow = 0
firstBurrowCol = 0
secondBurrowRow = 0
secondBurrowCol = 0
foodQuantity = 0
win = False

for r in range(size):
    for c in range(size):
        if matrix[r][c] == 'S':
            snakeRow = r
            snakeCol = c
        elif matrix[r][c] == 'B' and burrowFound:
            secondBurrowRow = r
            secondBurrowCol = c
        elif matrix[r][c] == 'B':
            firstBurrowRow = r
            firstBurrowCol = c
            burrowFound = True

while True:
    command = input()
    x = 0
    y = 0

    if command == 'up':
        if snakeRow - 1 < 0:
            matrix[snakeRow][snakeCol] = '.'
            break
        x = -1
    elif command == 'down':
        if snakeRow + 1 > size -1:
            matrix[snakeRow][snakeCol] = '.'
            break
        x = 1
    elif command == 'left':
        if snakeCol - 1 < 0:
            matrix[snakeRow][snakeCol] = '.'
            break
        y = -1
    elif command == 'right':
        if snakeCol + 1 > size - 1:
            matrix[snakeRow][snakeCol] = '.'
            break
        y = 1

    matrix[snakeRow][snakeCol] = '.'
    snakeRow += x
    snakeCol += y

    if matrix[snakeRow][snakeCol] == '*':
        foodQuantity += 1
    elif matrix[snakeRow][snakeCol] == 'B':
        if snakeRow == firstBurrowRow and snakeCol == firstBurrowCol:
            snakeRow = secondBurrowRow
            snakeCol = secondBurrowCol
        else:
            snakeRow = firstBurrowRow
            snakeCol = firstBurrowCol

        matrix[firstBurrowRow][firstBurrowCol] = '.'
        matrix[secondBurrowRow][secondBurrowCol] = '.'

    matrix[snakeRow][snakeCol] = 'S'

    if foodQuantity >= 10:
        win = True
        break

if win:
    print("You won! You fed the snake.")
else:
    print("Game over!")

print(f"Food eaten: {foodQuantity}")

for r in range(size):
    for c in range(size):
        print(matrix[r][c], end='')
    print()
