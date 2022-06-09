rows, columns = tuple(map(int, input().split(' ')))
matrix = [[char for char in input()] for line in range(rows)]
commands = [c for c in input()]

playerCurrentRow = 0
playerCurrentCol = 0
bunnyCurrentRow = 0
bunnyCurrentCol = 0
wins = False
died = False

for row in range(rows):
    for column in range(columns):
        if matrix[row][column] == 'P':
            playerCurrentRow = row
            playerCurrentCol = column
        elif matrix[row][column] == 'B':
            bunnyCurrentRow = row
            bunnyCurrentCol = column

for command in commands:
    for br in range(bunnyCurrentRow - 1, bunnyCurrentRow + 2):
        if br >= rows:
            break
        if br == bunnyCurrentRow:
            y = - 1
            x = 2
        else:
            x = 1
            y = 0
        for bc in range(bunnyCurrentCol + y, bunnyCurrentCol + x):
            if bc < columns:
                matrix[br][bc] = 'B'
                if playerCurrentRow == br and playerCurrentCol == bc:
                    died = True
                    break
            else:
                break

    bunnyCurrentRow += 2
    bunnyCurrentCol += 2

    if command == 'L':
        playerCurrentCol -= 1
        if playerCurrentCol < 0:
            playerCurrentCol += 1
            matrix[playerCurrentRow][playerCurrentCol] = '.'
            wins = True
            break
    elif command == 'R':
        playerCurrentCol += 1
        if playerCurrentCol >= columns:
            playerCurrentCol -= 1
            matrix[playerCurrentRow][playerCurrentCol] = '.'
            wins = True
            break
    elif command == 'U':
        playerCurrentRow -= 1
        if playerCurrentRow < 0:
            playerCurrentRow += 1
            matrix[playerCurrentRow][playerCurrentCol] = '.'
            wins = True
            break
    elif command == 'D':
        playerCurrentRow += 1
        if playerCurrentRow >= rows:
            playerCurrentRow -= 1
            matrix[playerCurrentRow][playerCurrentCol] = '.'
            wins = True
            break

    if playerCurrentRow == bunnyCurrentRow and playerCurrentCol == bunnyCurrentCol:
        died = True
        break

for r in range(rows):
    for c in range(columns):
        print(matrix[r][c], end='')
    print()

if wins:
    print(f'won: {playerCurrentRow} {playerCurrentCol}')
if died:
    print(f'died: {playerCurrentRow} {playerCurrentCol}')
