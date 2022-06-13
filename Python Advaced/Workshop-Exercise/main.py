def player_setup():
    first_name = input('Player one name: ')
    second_name = input('Player two name: ')
    first_symbol = input(f"{first_name} would like to play with 'X' or 'O'? ")
    second_symbol = ''
    if first_symbol == 'X':
        second_symbol = 'O'
    elif first_symbol == 'O':
        second_symbol = 'X'

    return {first_name: first_symbol, second_name: second_symbol}


def board_numeration():
    count = 1
    board = []
    for r in range(3):
        board.append([])
        for c in range(3):
            board[r].append(count)
            count += 1
    return board


def clear_board(board):
    board.clear()
    for r in range(3):
        board.append([])
        for c in range(3):
            board[r].append(' ')
    return board


def play_turn(board, position, symbol):
    row = 0
    col = 0

    for n in range(1, 10):
        if n == position:
            break

        col += 1
        if col % 3 == 0:
            col = 0
            row += 1

    if board[row][col] != 'X' and board[row][col] != 'O':
        board[row][col] = symbol
    else:
        print('Invalid command')

    return board


def check_win(board):
   for r in range(3):
       if board[r][0] == 'X' and board[r][1] == 'X' and board[r][2] == 'X':
           return 'X'
   for c in range(3):
       if board[0][c] == 'X' and board[1][c] == 'X' and board[2][c] == 'X':
           return 'X'
   if (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') \
           or (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
       return 'X'

   for r in range(3):
       if board[r][0] == 'O' and board[r][1] == 'O' and board[r][2] == 'O':
           return 'O'
   for c in range(3):
       if board[0][c] == 'O' and board[1][c] == 'O' and board[2][c] == 'O':
           return 'O'
   if (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') \
           or (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
       return 'O'

   return None


def print_board(board):
    for r in range(3):
        for c in range(3):
            if c == 0:
                print(f'|', end=' ')
            print(f'{board[r][c]}', end=' | ')
        print()


playersInfo = player_setup()
firstPlayer = ''
secondPlayer = ''
firstSymbol = ''
secondSymbol = ''
count = 0
for name, symbol in playersInfo.items():
    if count % 2 == 0:
        firstPlayer = name
        firstSymbol = symbol
    else:
        secondPlayer = name
        secondSymbol = symbol
    count += 1

board = board_numeration()
print_board(board)
board = clear_board(board)

turnCounter = 0
currentPlayer = firstPlayer
currentSymbol = firstSymbol

while True:
    if turnCounter % 2 == 0:
        currentPlayer = firstPlayer
        currentSymbol = firstSymbol
    else:
        currentPlayer = secondPlayer
        currentSymbol = secondSymbol

    turnCounter += 1

    position = int(input(f'{currentPlayer} choose a free position [1-9]: '))
    board = play_turn(board, position, currentSymbol)
    print_board(board)
    check = check_win(board)

    if check is None:
        continue
    elif check == 'X' or check == 'O':
        if firstSymbol == check:
            print(f'{firstPlayer} won!')
        elif secondSymbol == check:
            print(f'{secondPlayer} won!')
        break
