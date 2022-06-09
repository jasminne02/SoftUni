size = int(input())
matrix = [[int(x) for x in input().split(' ')] for line in range(size)]
coordinates = [x for x in input().split(' ')]
aliveCells = size * size
aliveSum = 0

for i in range(len(coordinates)):
    row, column = tuple(map(int, (coordinates[i]).split(',')))
    value = matrix[row][column]

    if value > 0:
        for r in range(row - 1, row + 2):
            if r < 0:
                continue
            elif r > size - 1:
                break

            for c in range(column - 1, column + 2):
                if c < 0:
                    continue
                elif c > size - 1:
                    break

                if matrix[r][c] > 0:
                    matrix[r][c] -= value

for r in range(size):
    for c in range(size):
        if matrix[r][c] <= 0:
            aliveCells -= 1
        else:
            aliveSum += matrix[r][c]

print(f'Alive cells: {aliveCells}')
print(f'Sum: {aliveSum}')
for r in range(size):
    for c in range(size):
        print(matrix[r][c], end=' ')
    print()
