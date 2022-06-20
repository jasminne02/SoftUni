from collections import deque

males = deque(map(int, input().split(' ')))  # start from last
females = deque(map(int, input().split(' ')))  # start from first
matches = 0

while males and females:
    male = males[-1]
    female = females[0]

    if male <= 0:
        males.pop()
        continue
    elif female <= 0:
        females.popleft()
        continue
    elif male % 25 == 0:
        males.pop()
        males.pop()
        continue
    elif female % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    if male == female:
        matches += 1
        females.popleft()
        males.pop()
    else:
        male -= 2
        males.pop()
        males.append(male)
        females.popleft()

print(f'Matches: {matches}')

print("Males left: ", end='')
if males:
    males.reverse()
    for idx in range(len(males)):
        if idx == len(males)-1:
            print(males[idx])
        else:
            print(males[idx], end=', ')
else:
    print('none')

print("Females left: ", end='')
if females:
    for idx in range(len(females)):
        if idx == len(females)-1:
            print(females[idx])
        else:
            print(females[idx], end=', ')
else:
    print('none')
