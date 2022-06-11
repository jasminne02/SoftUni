rows = int(input())
matrix = [[int(x) for x in input().split(' ')] for line in range(rows)]

while True:
    command = input()
    if command == 'END':
        for line in matrix:
            for num in line:
                print(num, end=' ')
            print()
        break

    command = command.split(' ')
    command, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])
    if 0 <= row <= len(matrix)-1 and 0 <= col <= len(matrix)-1:
        if command == 'Add':
            matrix[row][col] += value
        elif command == 'Subtract':
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")
