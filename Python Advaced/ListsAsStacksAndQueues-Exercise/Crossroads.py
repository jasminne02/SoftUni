from collections import deque

greenLightDuration = int(input())
freeWindowDuration = int(input())
carsQueue = deque()
enteredInCrossroad = deque()
safelyPassed = 0
crashHappened = False

while not crashHappened:
    command = input()
    if command == 'END':
        break

    if command == 'green':
        currentGreen = greenLightDuration

        while carsQueue and currentGreen > 0:
            car = carsQueue.popleft()
            if currentGreen >= len(car) or currentGreen + freeWindowDuration >= len(car):
                safelyPassed += 1
                currentGreen -= len(car)
            else:
                crashedIndex = currentGreen + freeWindowDuration
                print("A crash happened!")
                print(f"{car} was hit at {car[crashedIndex]}.")
                crashHappened = True
                break
    else:
        carsQueue.append(command)

if not crashHappened:
    print(f'Everyone is safe.')
    print(f'{safelyPassed} total cars passed the crossroads.')
