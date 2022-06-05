from collections import deque

materialBoxes = deque(map(int, input().split(' ')))
magicLevel = deque(map(int, input().split(' ')))
dolls = 0
woodenTrain = 0
teddyBear = 0
bicycle = 0

while materialBoxes and magicLevel:
    currentBox = materialBoxes[-1]
    currentMagicLevel = magicLevel[0]
    totalMagic = currentBox * currentMagicLevel

    if currentBox == 0 and currentMagicLevel == 0:
        materialBoxes.pop()
        magicLevel.popleft()
    elif currentBox == 0:
        materialBoxes.pop()
    elif currentMagicLevel == 0:
        magicLevel.popleft()

    if totalMagic == 150:
        dolls += 1
        materialBoxes.pop()
        magicLevel.popleft()
    elif totalMagic == 250:
        woodenTrain += 1
        materialBoxes.pop()
        magicLevel.popleft()
    elif totalMagic == 300:
        teddyBear += 1
        materialBoxes.pop()
        magicLevel.popleft()
    elif totalMagic == 400:
        bicycle += 1
        materialBoxes.pop()
        magicLevel.popleft()
    elif totalMagic < 0:
        sum = currentBox + currentMagicLevel
        materialBoxes.pop()
        magicLevel.popleft()
        materialBoxes.append(sum)
    elif totalMagic > 0:
        magicLevel.popleft()
        materialBoxes.pop()
        currentBox += 15
        materialBoxes.append(currentBox)

if (dolls >= 1 and woodenTrain >= 1) or (teddyBear >= 1 and bicycle >= 1):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materialBoxes:
    print("Materials left: ", end="")
    for i in range(len(materialBoxes)):
        if i == len(materialBoxes) - 1:
            k = len(magicLevel) - 1 - i
            print(int(materialBoxes[k]))
        else:
            k = len(magicLevel) - 1 - i
            print(int(materialBoxes[k]), end=', ')
if magicLevel:
    print("Magic left: ", end="")
    for i in range(len(magicLevel)):
        if i == len(magicLevel) - 1:
            print(int(magicLevel[i]))
        else:
            print(int(magicLevel[i]), end=', ')

if bicycle > 0:
    print(f"Bicycle: {bicycle}")
if dolls > 0:
    print(f"Doll: {dolls}")
if teddyBear > 0:
    print(f"Teddy bear: {teddyBear}")
if woodenTrain > 0:
    print(f"Wooden train: {woodenTrain}")
