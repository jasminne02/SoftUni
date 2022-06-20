import sys

jobs = list(map(int, input().split(', ')))
index = int(input())

idxUsed = []
clockCycle = 0

while True:
    minJob = sys.maxsize
    minIdx = 0

    for idx in range(len(jobs)):
        if jobs[idx] < minJob and idx not in idxUsed:
            minJob = jobs[idx]
            minIdx = idx

    clockCycle += minJob
    idxUsed.append(minIdx)
    if index == minIdx:
        break

print(clockCycle)
