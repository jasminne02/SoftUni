size = int(input())
matrix = [[int(x) for x in input().split(' ')] for line in range(size)]
primaryDiagonal = []
secondaryDiagonal = []

for i in range(size):
    primaryDiagonal.append(matrix[i][i])
for row in range(size):
    secondaryDiagonal.append(matrix[row][size - 1 - row])

diff = abs(sum(primaryDiagonal) - sum(secondaryDiagonal))
print(diff)
