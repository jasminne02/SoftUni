from collections import deque

bombEffects = deque(map(int, input().split(', ')))  # popleft
bombCasings = deque(map(int, input().split(', ')))  # pop

cherryBomb = 0
daturaBomb = 0
smokeBomb = 0
pouchFilled = False

while bombEffects and bombCasings:
    if cherryBomb >= 3 and daturaBomb >= 3 and smokeBomb >= 3:
        pouchFilled = True
        break

    currentBombEffect = bombEffects[0]
    currentBombCasing = bombCasings[-1]
    bombSum = currentBombEffect + currentBombCasing

    if bombSum == 40:
        daturaBomb += 1
    elif bombSum == 60:
        cherryBomb += 1
    elif bombSum == 120:
        smokeBomb += 1
    else:
        bombCasings.pop()
        bombCasings.append(currentBombCasing-5)
        continue

    bombEffects.popleft()
    bombCasings.pop()

if pouchFilled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if len(bombEffects) == 0:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: ", end='')
    for i in range(len(bombEffects)):
        if i == len(bombEffects) - 1:
            print(bombEffects[i])
        else:
            print(bombEffects[i], end=', ')

if len(bombCasings) == 0:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: ", end='')
    for i in range(len(bombCasings)):
        if i == len(bombCasings) - 1:
            print(bombCasings[i])
        else:
            print(bombCasings[i], end=', ')

print(f"Cherry Bombs: {cherryBomb}")
print(f"Datura Bombs: {daturaBomb}")
print(f"Smoke Decoy Bombs: {smokeBomb}")
