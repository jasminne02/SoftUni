matrix = []
rowsNum, columnsNum = tuple(input().split(', '))
matrixSum = 0

for row in range(int(rowsNum)):
    line = [int(x) for x in input().split(', ')]
    matrix.append(line)
    matrixSum += sum(line)

print(matrixSum)
print(matrix)
