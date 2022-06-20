size = int(input())
bombsNumber = int(input())

matrix = [[0 for x in range(size)] for line in range(size)]

for _ in range(bombsNumber):
    command = input()
    bombRow = ''
    bombCol = ''

    for idx in range(len(command)):
        if bombRow == '' and command[idx].isdigit():
            bombRow = int(command[idx])
        elif bombCol == '' and command[idx].isdigit():
            bombCol = int(command[idx])
            break

    if 0 <= bombRow < size and 0 <= bombCol < size:
        matrix[bombRow][bombCol] = '*'

        if bombRow - 1 >= 0:
            if bombCol - 1 >= 0 and matrix[bombRow-1][bombCol-1] != '*':
                matrix[bombRow-1][bombCol-1] += 1
            if matrix[bombRow-1][bombCol] != '*':
                matrix[bombRow-1][bombCol] += 1
            if bombCol + 1 < size and matrix[bombRow-1][bombCol+1] != '*':
                matrix[bombRow-1][bombCol+1] += 1

        if bombCol - 1 >= 0 and matrix[bombRow][bombCol-1] != '*':
            matrix[bombRow][bombCol-1] += 1
        if bombCol + 1 < size and matrix[bombRow][bombCol+1] != '*':
            matrix[bombRow][bombCol+1] += 1

        if bombRow + 1 < size:
            if bombCol - 1 >= 0 and matrix[bombRow+1][bombCol-1] != '*':
                matrix[bombRow+1][bombCol-1] += 1
            if matrix[bombRow+1][bombCol] != '*':
                matrix[bombRow + 1][bombCol] += 1
            if bombCol + 1 < size and matrix[bombRow+1][bombCol] != '*':
                matrix[bombRow+1][bombCol+1] += 1

for r in range(size):
    for c in range(size):
        print(matrix[r][c], end=' ')
    print()
