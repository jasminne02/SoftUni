from collections import deque

waterQuantity = int(input())
startReceived = False
peopleQueue = deque()

while True:
    command = input()

    if command == 'Start':
        startReceived = True
        continue
    elif command == 'End':
        print(f"{waterQuantity} liters left")
        break

    if not startReceived:
        peopleQueue.append(command)
    elif command.isdigit():
        litersWanted = int(command)

        if litersWanted <= waterQuantity:
            print(f"{peopleQueue.popleft()} got water")
            waterQuantity -= litersWanted
        else:
            print(f"{peopleQueue.popleft()} must wait")

    elif 'refill' in command:
        command = command.split(' ')
        liters = int(command[1])

        waterQuantity += liters
