from collections import deque

petrolPumpsNumber = int(input())
pumps = deque()

for pump in range(petrolPumpsNumber):
    pumps.append([int(x) for x in input().split(' ')])

for attempt in range(petrolPumpsNumber):
    trunk = 0
    failed = False

    for petrol, distance in pumps:
        trunk += petrol - distance
        if trunk < 0:
            failed = True
            break

    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break
