from collections import deque

customers = deque(map(int, input().split(', ')))  # start from first
taxis = deque(map(int, input().split(', ')))  # start from last
totalTime = 0

while customers and taxis:
    customer = customers.popleft()
    taxi = taxis.pop()

    if customer <= taxi:
        totalTime += customer
    elif customer > taxi:
        customers.insert(0, customer)

if len(customers) == 0:
    print(f"All customers were driven to their destinations\nTotal time: {totalTime} minutes")
elif len(taxis) == 0 and len(customers) > 0:
    customersLeft = ''
    for idx in range(len(customers)):
        if idx == len(customers)-1:
            customersLeft += str(customers[idx])
        else:
            customersLeft += str(customers[idx]) + ', '

    print(f"Not all customers were driven to their destinations\nCustomers left: {customersLeft}")
