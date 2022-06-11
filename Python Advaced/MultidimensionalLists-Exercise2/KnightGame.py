size = int(input())
board = [[x for x in input()] for line in range(size)]


def find_count(board, row, col):
    moves = [
        [row-2, col-1],
        [row-2, col+1],
        [row-1, col-2],
        [row-1, col+2],
        [row+1, col-2],
        [row+1, col+2],
        [row+2, col-1],
        [row+2, col+1]
    ]

    result = 0
    for r, c in moves:
        if 0 <= r < len(board) and 0 <= c < len(board) and board[r][c] == 'K':
            result += 1
    return result


removedKnightCount = 0

while True:
    bestCount = 0
    knightRow = 0
    knightCol = 0
    for row in range(size):
        for col in range(size):
            if board[row][col] == '0':
                continue
            count = find_count(board, row, col)
            if count > bestCount:
                bestCount = count
                knightRow = row
                knightCol = col
    if bestCount == 0:
        break

    board[knightRow][knightCol] = '0'
    removedKnightCount += 1

print(removedKnightCount)
