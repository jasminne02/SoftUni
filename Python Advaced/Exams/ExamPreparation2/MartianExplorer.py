field = [[x for x in input().split(' ')] for line in range(6)]
commands = input().split(', ')

roverRow = 0
roverCol = 0
water = False
metal = False
concrete = False

for r in range(6):
    for c in range(6):
        if field[r][c] == 'E':
            roverRow = r
            roverCol = c
            break

for command in commands:
    if command == 'up':
        if roverRow-1 >= 0:
            roverRow -= 1
        else:
            roverRow = 5
    elif command == 'down':
        if roverRow+1 <= 5:
            roverRow += 1
        else:
            roverRow = 0
    elif command == 'left':
        if roverCol-1 >= 0:
            roverCol -= 1
        else:
            roverCol = 5
    elif command == 'right':
        if roverCol+1 <= 5:
            roverCol += 1
        else:
            roverCol = 0

    if field[roverRow][roverCol] in ['W', 'M', 'C']:
        deposit = ''
        if field[roverRow][roverCol] == 'W':
            deposit = 'Water'
            water = True
        elif field[roverRow][roverCol] == 'M':
            deposit = 'Metal'
            metal = True
        else:
            deposit = 'Concrete'
            concrete = True
        print(f"{deposit} deposit found at ({roverRow}, {roverCol})")
    elif field[roverRow][roverCol] == 'R':
        print(f"Rover got broken at ({roverRow}, {roverCol})")
        break

if water and concrete and metal:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
