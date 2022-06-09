rows, columns = tuple(map(int, input().split(' ')))
matrix = []

for r in range(rows):
    line = []
    for c in range(columns):
        string = ''
        string += chr(97 + r)
        string += chr(97 + c + r)
        string += chr(97 + r)
        line.append(string)
    matrix.append(line)

for row in range(rows):
    for column in range(columns):
        print(matrix[row][column], end=' ')
    print()
