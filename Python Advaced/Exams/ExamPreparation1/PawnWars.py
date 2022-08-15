def rank(col):
    if col == 0:
        return 8
    elif col == 1:
        return 7
    elif col == 2:
        return 6
    elif col == 3:
        return 5
    elif col == 4:
        return 4
    elif col == 5:
        return 3
    elif col == 6:
        return 2
    elif col == 7:
        return 1


board = [[x for x in input().split(' ')] for line in range(8)]

wRow = 0
wCol = 0
bRow = 0
bCol = 0

for r in range(8):
    for c in range(8):
        if board[r][c] == 'w':
            wRow = r
            wCol = c
        elif board[r][c] == 'b':
            bRow = r
            bCol = c

if wCol-1 == bCol or wCol+1 == bCol:
    if wRow - 1 == bRow:
        if wCol - 1 == bCol:
            print(f"Game over! White win, capture on {chr(wCol - 1 + 97)}{rank(wRow-1)}.")
        elif wCol + 1 == bCol:
            print(f"Game over! White win, capture on {chr(wCol + 1 + 97)}{rank(wRow-1)}.")
    else:
        while True:
            wRow -= 1
            if wRow - 1 == bRow:
                if wCol - 1 == bCol:
                    print(f"Game over! White win, capture on {chr(wCol - 1 + 97)}{rank(bRow-1)}.")
                elif wCol + 1 == bCol:
                    print(f"Game over! White win, capture on {chr(wCol + 1 + 97)}{rank(bRow-1)}.")
                break

            bRow += 1
            if bRow + 1 == wRow:
                if bCol - 1 == wCol:
                    print(f"Game over! Black win, capture on {chr(bCol - 1 + 97)}{rank(bRow+1)}.")
                elif bCol + 1 == wCol:
                    print(f"Game over! Black win, capture on {chr(bCol + 1 + 97)}{rank(bRow+1)}.")
                break
else:
    if 7 - wRow == bRow:
        print(f"Game over! White pawn is promoted to a queen at {chr(wCol+97)}{8}.")
    elif 7 - wRow > bRow:
        print(f"Game over! White pawn is promoted to a queen at {chr(wCol + 97)}{8}.")
    elif 7 - wRow < bRow:
        print(f"Game over! Black pawn is promoted to a queen at {chr(bCol + 97)}{1}.")
