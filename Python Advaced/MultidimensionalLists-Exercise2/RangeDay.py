field = [[x for x in input().split(' ')] for line in range(5)]
commandsCount = int(input())

currentRow = 0
currentCol = 0
shotTargets = 0
totalTargets = 0
shotPositions = []

for r in range(5):
    for c in range(5):
        if field[r][c] == 'A':
            currentRow = r
            currentCol = c
        elif field[r][c] == 'x':
            totalTargets += 1

for n in range(commandsCount):
    command = input()
    command = command.split(' ')

    if 'move' in command:
        direction, steps = command[1], int(command[2])
        x, y, k = 0, 0, 0
        if direction == 'up':
            x = -2
        elif direction == 'down':
            x = 2
        elif direction == 'left':
            y = -2
        elif direction == 'right':
            y = 2

        if not (0 <= currentRow + x < 5 and 0 <= currentCol < 5):
            continue

        for r in range(currentRow, currentRow + x):
            for c in range(currentCol, currentCol + y):
                if field[r][c] == '.':
                    k += 1

        if direction == 'up' or direction == 'down':
            currentRow += k
        elif direction == 'left' or direction == 'right':
            currentCol += k
    elif 'shoot' in command:
        direction = command[1]
        if direction == 'up':
            for r in range(currentRow, -1, -1):
                if field[r][currentCol] == 'x':
                    field[r][currentCol] = '.'
                    idx = [r, currentCol]
                    shotPositions.append(idx)
                    shotTargets += 1
                    break
        elif direction == 'down':
            for r in range(currentRow, 5):
                if field[r][currentCol] == 'x':
                    field[r][currentCol] = '.'
                    idx = [r, currentCol]
                    shotPositions.append(idx)
                    shotTargets += 1
                    break
        elif direction == 'left':
            for c in range(currentCol, -1, -1):
                if field[currentRow][c] == 'x':
                    field[currentRow][c] = '.'
                    idx = [currentRow, c]
                    shotPositions.append(idx)
                    shotTargets += 1
                    break
        elif direction == 'right':
            for c in range(currentCol, 5):
                if field[currentRow][c] == 'x':
                    field[currentRow][c] = '.'
                    idx = [currentRow, c]
                    shotPositions.append(idx)
                    shotTargets += 1
                    break

    if shotTargets == totalTargets:
        print(f"Training completed! All {totalTargets} targets hit.")
        break

if shotTargets < totalTargets:
    print(f"Training not completed! {totalTargets - shotTargets} targets left.")

for position in shotPositions:
    print(position)
