import sys

rows, columns = [int(x) for x in input().split(', ')]
matrix = []
info2x2 = dict()
lastRow = 0
lastColumn = 0
maxSum = -sys.maxsize
maxMatrix = []

for row in range(rows):
    line = [int(x) for x in input().split(', ')]
    matrix.append(line)

while lastRow < rows-1:
    subMatrix2x2 = []
    subMatrixSum = 0

    for row in range(lastRow, lastRow + 2):
        line = []
        for column in range(lastColumn, lastColumn + 2):
            line.append(matrix[row][column])

        subMatrix2x2.append(line)
        subMatrixSum += sum(line)

    info2x2[subMatrixSum] = subMatrix2x2
    if lastColumn + 1 == columns - 1:
        lastColumn = 0
        lastRow += 1
    else:
        lastColumn += 1

for sum, matrix in info2x2.items():
    if sum > maxSum:
        maxSum = sum
        maxMatrix = matrix

for row in range(2):
    for column in range(2):
        print(maxMatrix[row][column], end=' ')
    print()

print(maxSum)
