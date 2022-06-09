import sys

rows, columns = tuple(map(int, input().split(' ')))
matrix = [[int(x) for x in input().split(' ')] for line in range(rows)]
maxSum = -sys.maxsize
maxMatrix = []
currentRow = 0
currentColumn = 0

while currentRow < rows - 2:
    currentSum = 0
    currentMatrix = []

    for row in range(currentRow, currentRow + 3):
        line = []
        for column in range(currentColumn, currentColumn + 3):
            line.append(matrix[row][column])
        currentSum += sum(line)
        currentMatrix.append(line)

    if currentSum > maxSum:
        maxSum = currentSum
        maxMatrix = currentMatrix

    if currentColumn + 2 == columns - 1:
        currentColumn = 0
        currentRow += 1
    else:
        currentColumn += 1

print(f"Sum = {maxSum}")
for row in range(3):
    for column in range(3):
        print(maxMatrix[row][column], end=' ')
    print()
