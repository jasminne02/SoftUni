matrix = []
rows = int(input())

for row in range(rows):
    line = [int(x) for x in input().split(', ')]
    matrix.append(line)

matrix = [[k for k in row if k % 2 == 0] for row in matrix]
print(matrix)
