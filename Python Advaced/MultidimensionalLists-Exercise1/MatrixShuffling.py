rows, columns = tuple(map(int, input().split(' ')))
matrix = [[x for x in input().split(' ')] for line in range(rows)]

while True:
    command = input()
    if command == 'END':
        break

    command = command.split(' ')
    if 'swap' in command:
        if len(command) == 5:
            if command[0] == 'swap' and command[1].isdigit() and command[2].isdigit() \
                    and command[3].isdigit() and command[4].isdigit():
                row1 = int(command[1])
                col1 = int(command[2])
                row2 = int(command[3])
                col2 = int(command[4])

                if row1 > rows-1 or row2 > rows-1 or col1 > columns-1 or col2 > columns-1 \
                        or row1 < 0 or row2 < 0 or col1 < 0 or col2 < 0:
                    print('Invalid input!')
                else:
                    x = matrix[row1][col1]
                    y = matrix[row2][col2]

                    matrix[row1][col1] = y
                    matrix[row2][col2] = x

                    for row in range(rows):
                        for column in range(columns):
                            print(matrix[row][column], end=' ')
                        print()
            else:
                print('Invalid input!')
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
