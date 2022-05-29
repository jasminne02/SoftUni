number = int(input())
cars = set()

for n in range(number):
    command = tuple(input().split(', '))
    direction, carNumber = command

    if direction == 'IN':
        cars.add(carNumber)
    elif direction == 'OUT':
        cars.remove(carNumber)

for car in cars:
    print(car)
if len(cars) == 0:
    print('Parking Lot is Empty')
