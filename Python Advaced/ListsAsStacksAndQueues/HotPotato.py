from collections import deque

kids = deque(input().split(' '))
tosses = int(input())
currentCount = 0

while len(kids) > 1:
    currentCount += 1
    currentKid = kids.popleft()

    if currentCount < tosses:
        kids.append(currentKid)
    elif currentCount == tosses:
        print(f'Removed {currentKid}')
        currentCount = 0

print(f'Last is {kids.popleft()}')
