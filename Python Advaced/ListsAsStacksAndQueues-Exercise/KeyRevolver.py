from collections import deque

bulletPrice = int(input())
gunBarrelSize = int(input())
bullets = deque(int(x) for x in input().split(' '))  # going back-to-front
locks = [int(x) for x in input().split(' ')]  # going front-to-back
intelligenceValue = int(input())
currentBarrel = gunBarrelSize

while locks and bullets:
    if currentBarrel == 0:
        print('Reloading!')
        if len(bullets) < gunBarrelSize:
            currentBarrel = len(bullets)
        else:
            currentBarrel = gunBarrelSize

    if locks[0] >= bullets[-1]:
        print('Bang!')
        locks.pop(0)
    else:
        print('Ping!')

    bullets.pop()
    intelligenceValue -= bulletPrice
    currentBarrel -= 1

if currentBarrel == 0 and len(bullets) > 0:
    print('Reloading!')
    if len(bullets) < gunBarrelSize:
        currentBarrel = len(bullets)
    else:
        currentBarrel = gunBarrelSize

if len(locks) == 0:
    print(f"{len(bullets)} bullets left. Earned ${intelligenceValue}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
