rows = int(input())
matrix = []

for row in range(rows):
    elements = [int(x) for x in input().split(', ')]
    matrix.append(elements)

flattenedMatrix = [num for substring in matrix for num in substring]
print(flattenedMatrix)
