from collections import deque

ramenBowls = deque(map(int, input().split(', ')))
customers = deque(map(int, input().split(', ')))

while ramenBowls and customers:
    ramen = ramenBowls[-1]
    customer = customers[0]

    if ramen == customer:
        ramenBowls.pop()
        customers.popleft()
        continue
    elif ramen > customer:
        ramen -= customer
        ramenBowls.pop()
        ramenBowls.append(ramen)
        customers.popleft()
    elif customer > ramen:
        customer -= ramen
        customers.popleft()
        customers.insert(0, customer)
        ramenBowls.pop()

if len(customers) == 0:
    print("Great job! You served all the customers.")
    if ramenBowls:
        print("Bowls of ramen left: ", end='')
        for idx in range(len(ramenBowls)):
            if idx == len(ramenBowls) - 1:
                print(ramenBowls[idx])
            else:
                print(ramenBowls[idx], end=', ')
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print("Customers left: ", end='')
        for idx in range(len(customers)):
            if idx == len(customers) - 1:
                print(customers[idx])
            else:
                print(customers[idx], end=', ')
