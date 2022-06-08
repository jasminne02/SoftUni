rows, columns = tuple([int(x) for x in input().split(' ')])
matrix = []
equalMatrices = 0
currentChar = ''
currentRow = 0
currentColumn = 0

for row in range(rows):
    line = input().split(' ')
    matrix.append(line)

while currentRow < rows - 1:
    currentChar = matrix[currentRow][currentColumn]
    identicalChars = True

    for row in range(currentRow, currentRow + 2):
        if not identicalChars:
            break
        for column in range(currentColumn, currentColumn + 2):
            if matrix[row][column] != currentChar:
                identicalChars = False
                break

    if identicalChars:
        equalMatrices += 1

    if currentColumn + 1 == columns - 1:
        currentColumn = 0
        currentRow += 1
    else:
        currentColumn += 1

print(equalMatrices)
