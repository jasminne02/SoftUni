import sys
from collections import deque

foodQuantity = int(input())
ordersFoodQuantity = deque(input().split(' '))
biggestOrder = -sys.maxsize
leftOrders = deque()
stopServing = False

for i in range(len(ordersFoodQuantity)):
    order = int(ordersFoodQuantity.popleft())

    if order > biggestOrder:
        biggestOrder = order

    if order <= foodQuantity:
        foodQuantity -= order
    else:
        stopServing = True

    if stopServing:
        leftOrders.append(order)

print(biggestOrder)
if len(leftOrders) == 0:
    print('Orders complete')
else:
    x = ''
    for i in range(len(leftOrders)):
        if i < len(leftOrders):
            x += str(leftOrders.popleft()) + ' '
        else:
            x += str(leftOrders.popleft())
    print(f"Orders left: {x}")
