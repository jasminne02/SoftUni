import sys

size = int(input())
field = [[x for x in input().split(' ')] for line in range(size)]

bunnyRow = 0
bunnyCol = 0
pathName = ''
maxPath = []
path = []
maxSum = -sys.maxsize
eggsSum = 0

for row in range(size):
    for col in range(size):
        el = field[row][col]
        if el == 'B':
            bunnyRow = row
            bunnyCol = col

# goes up
if bunnyRow - 1 >= 0:
    for r in range(bunnyRow - 1, -1, -1):
        el = field[r][bunnyCol]
        if el == 'X':
            break
        eggsSum += int(el)
        coordinates = [r, bunnyCol]
        path.append(coordinates)

    if eggsSum > maxSum:
        maxPath = path
        pathName = 'up'
        maxSum = eggsSum

    path = []
    eggsSum = 0

# goes down
if bunnyRow + 1 <= size - 1:
    for r in range(bunnyRow + 1, size):
        el = field[r][bunnyCol]
        if el == 'X':
            break
        eggsSum += int(el)
        coordinates = [r, bunnyCol]
        path.append(coordinates)

    if eggsSum > maxSum:
        maxPath = path
        pathName = 'down'
        maxSum = eggsSum

    path = []
    eggsSum = 0

# goes left
if bunnyCol - 1 >= 0:
    for c in range(bunnyCol - 1, -1, -1):
        el = field[bunnyRow][c]
        if el == 'X':
            break
        eggsSum += int(el)
        coordinates = [bunnyRow, c]
        path.append(coordinates)

    if eggsSum > maxSum:
        maxPath = path
        pathName = 'left'
        maxSum = eggsSum

    path = []
    eggsSum = 0

# goes right
if bunnyCol + 1 <= size - 1:
    for c in range(bunnyCol + 1, size):
        el = field[bunnyRow][c]
        if el == 'X':
            break
        eggsSum += int(el)
        coordinates = [bunnyRow, c]
        path.append(coordinates)

    if eggsSum > maxSum:
        maxPath = path
        pathName = 'right'
        maxSum = eggsSum

    path = []
    eggsSum = 0

print(pathName)
for line in maxPath:
    print(line)
print(maxSum)
