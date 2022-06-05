workingBees = list(map(int, input().split(' ')))
nectar = list(map(int, input().split(' ')))
nectar.reverse()
symbols = input().split(' ')
madeHoney = 0

while workingBees and nectar:
    currentBee = workingBees[0]
    currentNectar = nectar[0]

    if currentNectar >= currentBee:
        symbol = symbols[0]
        result = 0

        if symbol == '+':
            result = currentBee + currentNectar
        elif symbol == '-':
            result = currentBee - currentNectar
        elif symbol == '*':
            result = currentBee * currentNectar
        elif symbol == '/':
            if currentNectar != 0:
                result = currentBee / currentNectar
            else:
                result = 0

        madeHoney += abs(result)
        workingBees.pop(0)
        nectar.pop(0)
        symbols.pop(0)
    elif currentNectar < currentBee:
        nectar.pop(0)

print(f"Total honey made: {madeHoney}")
if workingBees:
    print(f"Bees left:", end=" ")
    for i in range(len(workingBees)):
        if i == len(workingBees) - 1:
            print(int(workingBees[i]))
        else:
            print(int(workingBees[i]), end=', ')
if nectar:
    print(f"Nectar left:", end=" ")
    nectar.reverse()
    for i in range(len(nectar)):
        if i == len(nectar) - 1:
            print(int(nectar[i]))
        else:
            print(int(nectar[i]), end=', ')
