rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for row in range(rows):
    line = [int(x) for x in input().split(' ')]
    matrix.append(line)

for column in range(columns):
    columnSum = 0
    for row in range(rows):
        columnSum += matrix[row][column]

    print(columnSum)
