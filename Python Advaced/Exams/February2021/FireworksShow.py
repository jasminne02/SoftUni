from collections import deque

fireworkEffect = deque(map(int, input().split(', ')))  # start from first
explosivePower = deque(map(int, input().split(', ')))  # start from last
palmFirework = 0
willowFirework = 0
crossetteFirework = 0

while fireworkEffect and explosivePower:
    firework = fireworkEffect[0]
    explosive = explosivePower[-1]

    if firework <= 0:
        fireworkEffect.popleft()
        continue
    if explosive <= 0:
        explosivePower.pop()
        continue

    if (firework + explosive) % 3 == 0 and (firework + explosive) % 5 != 0:
        palmFirework += 1
        fireworkEffect.popleft()
        explosivePower.pop()
    elif (firework + explosive) % 3 != 0 and (firework + explosive) % 5 == 0:
        willowFirework += 1
        fireworkEffect.popleft()
        explosivePower.pop()
    elif (firework + explosive) % 3 == 0 and (firework + explosive) % 5 == 0:
        crossetteFirework += 1
        fireworkEffect.popleft()
        explosivePower.pop()
    else:
        firework -= 1
        fireworkEffect.popleft()
        fireworkEffect.append(firework)

    if palmFirework >= 3 and willowFirework >= 3 and crossetteFirework >= 3:
        break

if palmFirework >= 3 and willowFirework >= 3 and crossetteFirework >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworkEffect:
    print("Firework Effects left: ", end='')
    for idx in range(len(fireworkEffect)):
        if idx == len(fireworkEffect)-1:
            print(fireworkEffect[idx])
        else:
            print(fireworkEffect[idx], end=', ')

if explosivePower:
    print("Explosive Power left: ", end='')
    for idx in range(len(explosivePower)):
        if idx == len(explosivePower)-1:
            print(explosivePower[idx])
        else:
            print(explosivePower[idx], end=', ')

print(f"Palm Fireworks: {palmFirework}")
print(f"Willow Fireworks: {willowFirework}")
print(f"Crossette Fireworks: {crossetteFirework}")
