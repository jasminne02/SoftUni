import math

size = int(input())
field = [[x for x in input().split(' ')] for line in range(size)]

playerRow = 0
playerCol = 0
collectedCoins = 0
hitsWall = False
path = []

for r in range(size):
    for c in range(size):
        if field[r][c] == 'P':
            playerRow = r
            playerCol = c
            path.append([playerRow, playerCol])
            break

while True:
    command = input()

    if command == 'up':
        if playerRow - 1 >= 0:
            playerRow -= 1
        else:
            playerRow = size - 1
        if field[playerRow][playerCol].isdigit():
            collectedCoins += int(field[playerRow][playerCol])
            field[playerRow][playerCol] = '-'
        elif field[playerRow][playerCol] == 'X':
            hitsWall = True
        path.append([playerRow, playerCol])
    elif command == 'down':
        if playerRow + 1 <= size - 1:
            playerRow += 1
        else:
            playerRow = 0
        if field[playerRow][playerCol].isdigit():
            collectedCoins += int(field[playerRow][playerCol])
            field[playerRow][playerCol] = '-'
        elif field[playerRow][playerCol] == 'X':
            hitsWall = True
        path.append([playerRow, playerCol])
    elif command == 'left':
        if playerCol - 1 >= 0:
            playerCol -= 1
        else:
            playerCol = size - 1
        if field[playerRow][playerCol].isdigit():
            collectedCoins += int(field[playerRow][playerCol])
            field[playerRow][playerCol] = '-'
        elif field[playerRow][playerCol] == 'X':
            hitsWall = True
        path.append([playerRow, playerCol])
    elif command == 'right':
        if playerCol + 1 <= size - 1:
            playerCol += 1
        else:
            playerCol = 0
        if field[playerRow][playerCol].isdigit():
            collectedCoins += int(field[playerRow][playerCol])
            field[playerRow][playerCol] = '-'
        elif field[playerRow][playerCol] == 'X':
            hitsWall = True
        path.append([playerRow, playerCol])

    if collectedCoins >= 100:
        break
    elif hitsWall:
        collectedCoins = math.floor(collectedCoins * 0.5)
        break

if collectedCoins >= 100:
    print(f"You won! You've collected {collectedCoins} coins.")
else:
    print(f"Game over! You've collected {math.floor(collectedCoins)} coins.")

print("Your path:")
for coordinates in path:
    print(coordinates)
