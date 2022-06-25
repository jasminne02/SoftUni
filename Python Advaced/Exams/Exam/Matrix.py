playersOrder = input().split(', ')
board = [[x for x in input().split(' ')] for line in range(6)]

firstPlayer, secondPlayer = playersOrder
firstPlayerIgnored, secondPlayerIgnored = False, False
playerCounter = 0  # if the counter is even -> first player move

while True:
    command = input()
    row, col = 0, 0
    for idx in range(len(command)):
        if idx == 1:
            row = int(command[idx])
        elif idx == 4:
            col = int(command[idx])

    if playerCounter % 2 == 0 and firstPlayerIgnored:
        firstPlayerIgnored = False
        playerCounter += 1
        continue
    elif playerCounter % 2 != 0 and secondPlayerIgnored:
        secondPlayerIgnored = False
        playerCounter += 1
        continue

    if playerCounter % 2 == 0:
        if board[row][col] == "E":
            print(f"{firstPlayer} found the Exit and wins the game!")
            break
        elif board[row][col] == "T":
            print(f"{firstPlayer} is out of the game! The winner is {secondPlayer}.")
            break
        elif board[row][col] == "W":
            print(f"{firstPlayer} hits a wall and needs to rest.")
            firstPlayerIgnored = True
    else:
        if board[row][col] == "E":
            print(f"{secondPlayer} found the Exit and wins the game!")
            break
        elif board[row][col] == "T":
            print(f"{secondPlayer} is out of the game! The winner is {firstPlayer}.")
            break
        elif board[row][col] == "W":
            print(f"{secondPlayer} hits a wall and needs to rest.")
            secondPlayerIgnored = True

    playerCounter += 1
