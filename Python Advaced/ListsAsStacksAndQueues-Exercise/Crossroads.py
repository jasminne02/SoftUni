from collections import deque

greenLightDurationInSeconds = int(input())
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
        carString = ''
        car = ''
        index = 0

        for second in range(1, greenLightDurationInSeconds + 1):
            if carString == '' and len(carsQueue) > 0:
                car = carsQueue.popleft()
            elif len(carsQueue) == 0 and len(enteredInCrossroad) == 0:
                break

            if index == 0:
                carString += car[index]
                enteredInCrossroad.append(car)
            elif index < len(car):
                carString += car[index]

            if carString == car:
                enteredInCrossroad.popleft()
                safelyPassed += 1
                carString = ''
                index = 0

            if carString != '':
                index += 1

        if len(enteredInCrossroad) > 0:
            for second in range(1, freeWindowDuration + 1):
                if carString == car:
                    enteredInCrossroad.popleft()
                    safelyPassed += 1
                    break
                elif index < len(car):
                    carString += car[index]

                index += 1

                if second == freeWindowDuration and car != carString:
                    print("A crash happened!")
                    print(f'{car} was hit at {car[index]}.')
                    crashHappened = True
                    break
    else:
        carsQueue.append(command)

if not crashHappened:
    print(f'Everyone is safe.')
    print(f'{safelyPassed} total cars passed the crossroads.')
