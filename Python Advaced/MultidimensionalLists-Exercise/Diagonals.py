size = int(input())
matrix = [[int(x) for x in input().split(', ')] for line in range(size)]
primaryDiagonal = []
secondaryDiagonal = []

for i in range(size):
    primaryDiagonal.append(matrix[i][i])
for row in range(size):
    secondaryDiagonal.append(matrix[row][size - 1 - row])

print(f"Primary diagonal: ", end='')
for i in range(len(primaryDiagonal)):
    if i == len(primaryDiagonal) - 1:
        print(f"{primaryDiagonal[i]}. ", end='')
    else:
        print(f"{primaryDiagonal[i]}, ", end='')
print(f"Sum: {sum(primaryDiagonal)}")
print(f"Secondary diagonal: ", end='')
for i in range(len(secondaryDiagonal)):
    if i == len(secondaryDiagonal) - 1:
        print(f"{secondaryDiagonal[i]}. ", end='')
    else:
        print(f"{secondaryDiagonal[i]}, ", end='')
print(f"Sum: {sum(secondaryDiagonal)}")
