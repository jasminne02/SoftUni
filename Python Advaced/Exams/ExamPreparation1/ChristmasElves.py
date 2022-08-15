from collections import deque

elfEnergy = deque(map(int, input().split(' ')))
materialsNumber = deque(map(int, input().split(' ')))

energyUsed = 0
toysMade = 0
count = 0

while elfEnergy and materialsNumber:
    elf = elfEnergy[0]
    material = materialsNumber[-1]
    count += 1

    if elf < 5:
        elfEnergy.popleft()
        count -= 1
        continue

    if count % 3 == 0:
        material *= 2

    if elf >= material:
        if count % 3 == 0:
            toysMade += 2
            energyUsed += material
            elf -= material
            materialsNumber.pop()
            elfEnergy.popleft()
            elfEnergy.append(elf)
            if count % 5 == 0:
                toysMade -= 2
        else:
            toysMade += 1
            elf -= material
            materialsNumber.pop()
            if count % 5 == 0:
                toysMade -= 1
            else:
                elf += 1
            elfEnergy.popleft()
            elfEnergy.append(elf)
            energyUsed += material
    else:
        elf *= 2
        elfEnergy.popleft()
        elfEnergy.append(elf)

print(f"Toys: {toysMade}")
print(f"Energy: {energyUsed}")

if elfEnergy:
    print("Elves left: ", end="")
    for idx in range(len(elfEnergy)):
        if idx == len(elfEnergy) - 1:
            print(elfEnergy[idx])
        else:
            print(elfEnergy[idx], end=', ')
if materialsNumber:
    print("Boxes left: ", end="")
    for idx in range(len(materialsNumber)):
        if idx == len(materialsNumber) - 1:
            print(materialsNumber[idx])
        else:
            print(materialsNumber[idx], end=', ')
