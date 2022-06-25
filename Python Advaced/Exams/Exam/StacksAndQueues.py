from collections import deque

eggs = deque(map(int, input().split(', ')))
piecesOfPaper = deque(map(int, input().split(', ')))
boxes = 0

while eggs and piecesOfPaper:
    egg = eggs[0]
    paper = piecesOfPaper[-1]

    if egg <= 0:
        eggs.popleft()
        continue
    elif egg == 13:
        eggs.popleft()
        first = piecesOfPaper.popleft()
        last = piecesOfPaper.pop()
        piecesOfPaper.insert(0, last)
        piecesOfPaper.append(first)
        continue

    if egg + paper <= 50:
        eggs.popleft()
        piecesOfPaper.pop()
        boxes += 1
    else:
        eggs.popleft()
        piecesOfPaper.pop()

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: ", end="")
    for idx in range(len(eggs)):
        if idx == len(eggs)-1:
            print(eggs[idx])
        else:
            print(eggs[idx], end=", ")

if piecesOfPaper:
    print(f"Pieces of paper left: ", end="")
    for idx in range(len(piecesOfPaper)):
        if idx == len(piecesOfPaper)-1:
            print(piecesOfPaper[idx])
        else:
            print(piecesOfPaper[idx], end=", ")
