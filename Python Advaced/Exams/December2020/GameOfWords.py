string = input()
size = int(input())
matrix = [[x for x in input()] for line in range(size)]
commandsNumber = int(input())

playerRow = 0
playerCol = 0

for r in range(size):
    for c in range(size):
        if matrix[r][c] == 'P':
            playerRow = r
            playerCol = c
            break

for _ in range(commandsNumber):
    command = input()

    if command == 'up':
        if playerRow-1 < 0 and len(string) > 0:
            string = string[:-1]
        elif playerRow-1 >= 0:
            matrix[playerRow][playerCol] = '-'
            playerRow -= 1
            if (matrix[playerRow][playerCol]).isalpha():
                letter = matrix[playerRow][playerCol]
                string += letter
            matrix[playerRow][playerCol] = 'P'
    elif command == 'down':
        if playerRow+1 > size-1 and len(string) > 0:
            string = string[:-1]
        elif playerRow+1 <= size-1:
            matrix[playerRow][playerCol] = '-'
            playerRow += 1
            if (matrix[playerRow][playerCol]).isalpha():
                letter = matrix[playerRow][playerCol]
                string += letter
            matrix[playerRow][playerCol] = 'P'
    elif command == 'left':
        if playerCol-1 < 0 and len(string) > 0:
            string = string[:-1]
        elif playerCol-1 >= 0:
            matrix[playerRow][playerCol] = '-'
            playerCol -= 1
            if (matrix[playerRow][playerCol]).isalpha():
                letter = matrix[playerRow][playerCol]
                string += letter
            matrix[playerRow][playerCol] = 'P'
    elif command == 'right':
        if playerCol+1 > size-1 and len(string) > 0:
            string = string[:-1]
        elif playerCol+1 <= size-1:
            matrix[playerRow][playerCol] = '-'
            playerCol += 1
            if (matrix[playerRow][playerCol]).isalpha():
                letter = matrix[playerRow][playerCol]
                string += letter
            matrix[playerRow][playerCol] = 'P'

print(string)
for r in range(size):
    for c in range(size):
        print(matrix[r][c], end='')
    print()
