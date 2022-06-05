size = int(input())
matrix = []

for row in range(size):
    matrix.append(list(input()))

symbol = input()
location = ()
found = False

for row in range(size):
    if found:
        break
    for column in range(size):
        if matrix[row][column] == symbol:
            location = (row, column)
            found = True
            break

if found:
    print(location)
else:
    print(f"{symbol} does not occur in the matrix")
