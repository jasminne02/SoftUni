size = int(input())
matrix = []
diagonalSum = 0

for row in range(size):
    line = [int(x) for x in input().split(' ')]
    matrix.append(line)

for index in range(size):
    diagonalSum += matrix[index][index]

print(diagonalSum)
