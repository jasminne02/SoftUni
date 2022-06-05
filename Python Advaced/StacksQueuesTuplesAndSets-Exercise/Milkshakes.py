from collections import deque

chocolate = input().split(', ')  # start from last
chocolate.reverse()
cupsOfMilk = input().split(', ')  # start from first
milkshakes = 0
index = 0

for i in range(len(chocolate)):
    if milkshakes == 5 or len(cupsOfMilk) <= 0 or len(chocolate) <= 0:
        break

    currentChocolate = int(chocolate[index])
    currentMilk = int(cupsOfMilk[0])

    if currentChocolate <= 0 and currentMilk <= 0:
        chocolate.pop(index)
        cupsOfMilk.pop(0)
        continue
    elif currentChocolate <= 0:
        chocolate.pop(index)
        continue
    elif currentMilk <= 0:
        cupsOfMilk.pop(0)
        continue

    if currentChocolate == currentMilk:
        chocolate.pop(index)
        cupsOfMilk.pop(0)
        index -= 1
        milkshakes += 1
    else:
        cupsOfMilk.pop(0)
        cupsOfMilk.append(str(currentMilk))
        chocolate.pop(index)
        chocolate.insert(index, str(currentChocolate - 5))
        index -= 1

    index += 1

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

if len(chocolate) > 0:
    print(f"Chocolate:", end=' ')
    chocolate.reverse()
    for i in range(len(chocolate)):
        if i == len(chocolate) - 1:
            print(int(chocolate[i]))
        else:
            print(int(chocolate[i]), end=', ')
else:
    print(f"Chocolate: empty")

if len(cupsOfMilk) > 0:
    print(f"Milk:", end=' ')
    for i in range(len(cupsOfMilk)):
        if i == len(cupsOfMilk) - 1:
            print(int(cupsOfMilk[i]))
        else:
            print(int(cupsOfMilk[i]), end=', ')
else:
    print(f"Milk: empty")
