wagons = int(input())
train = [0 for i in range(wagons)]

command = input()
add = 0
wagon = 0

while command != 'End':
    command = command.split(' ')

    if command[0] == 'add':
        add = train[-1] + int(command[1])
        train.pop()
        train.append(add)

    elif command[0] == 'insert':
        wagon = train[int(command[1])] + int(command[2])
        train.pop(int(command[1]))
        train.insert(int(command[1]), wagon)

    elif command[0] == 'leave':
        wagon = train[int(command[1])] - int(command[2])
        train.pop(int(command[1]))
        train.insert(int(command[1]), wagon)

    command = input()

print(train)
