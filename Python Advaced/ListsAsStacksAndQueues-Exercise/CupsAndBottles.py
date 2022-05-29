cups = [int(x) for x in input().split(' ')]
bottles = [int(x) for x in input().split(' ')]
cups.reverse()
wastedWater = 0

while len(cups) > 0 and len(bottles) > 0:
    currentCup = cups[-1]
    currentBottle = bottles.pop()

    if currentBottle > currentCup:
        wastedWater += currentBottle - currentCup

    currentCup -= currentBottle
    if currentCup <= 0:
        cups.pop()
    elif currentCup > 0:
        while currentCup > 0 and len(bottles) > 0:
            currentBottle = bottles.pop()
            if currentBottle > currentCup:
                wastedWater += currentBottle - currentCup
            currentCup -= currentBottle
        if currentCup <= 0:
            cups.pop()

if len(cups) == 0:
    print('Bottles: ', end='')
    for bottle in bottles:
        print(bottle, end=' ')
if len(bottles) == 0:
    print('Cups: ', end='')
    cups.reverse()
    for cup in cups:
        print(cup, end=' ')

print(f"\nWasted litters of water: {wastedWater}")
