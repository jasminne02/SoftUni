board = [[x for x in input().split(' ')] for line in range(8)]
capturingQueens = []
kingRow = 0
kingCol = 0

for r in range(8):
    for c in range(8):
        if board[r][c] == 'K':
            kingRow = r
            kingCol = c
            break

for row in range(8):
    for col in range(8):
        if board[row][col] == 'Q':
            if kingRow == row:
                apnd = True
                if kingCol > col:
                    for c in range(col+1, kingCol):
                        if board[row][c] == 'Q':
                            apnd = False
                elif kingCol < col:
                    for c in range(col-1, kingCol, -1):
                        if board[row][c] == 'Q':
                            apnd = False

                if apnd:
                    capturingQueens.append([row, col])
            if kingCol == col:
                apnd = True
                if kingRow > row:
                    for r in range(row+1, kingRow):
                        if board[r][col] == 'Q':
                            apnd = False
                elif kingRow < row:
                    for r in range(row-1, kingRow, -1):
                        if board[r][col] == 'Q':
                            apnd = False

                if apnd:
                    capturingQueens.append([row, col])
            if row - 1 >= 0:
                c = col
                for r in range(row-1, -1, -1):
                    c -= 1
                    if r == kingRow and c == kingCol:
                        capturingQueens.append([row, col])
                        break

                c = col
                for r in range(row-1, -1, -1):
                    c += 1
                    if r == kingRow and c == kingCol:
                        capturingQueens.append([row, col])
                        break
            if row + 1 < 8:
                c = col
                for r in range(row+1, 8):
                    c -= 1
                    if r == kingRow and c == kingCol:
                        capturingQueens.append([row, col])
                        break

                c = col
                for r in range(row+1, 8):
                    c += 1
                    if r == kingRow and c == kingCol:
                        capturingQueens.append([row, col])
                        break

if capturingQueens:
    for x in capturingQueens:
        print(x)
else:
    print("The king is safe!")
