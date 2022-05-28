from collections import deque


class Robot:
    def __init__(self, name, processingTime):
        self.name = name
        self.processingTime = processingTime
        self.finishWorkTime = 0

    def start_work(self, end):
        self.finishWorkTime = int(end)

    def is_free(self, current):
        if self.finishWorkTime <= int(current):
            return True
        elif self.finishWorkTime > int(current):
            return False


# Convert seconds to hour:min:seconds
def seconds_to_hours(current_seconds):
    current_hours = current_seconds // 3600
    current_seconds -= current_hours * 3600
    current_minutes = current_seconds // 60
    current_seconds -= current_minutes * 60

    if current_hours >= 24:
        current_hours = current_hours - 24 * (current_hours // 24)

    if current_hours < 10:
        current_hours = '0' + str(current_hours)
    if current_minutes < 10:
        current_minutes = '0' + str(current_minutes)
    if current_seconds < 10:
        current_seconds = '0' + str(current_seconds)

    return f'{current_hours}:{current_minutes}:{current_seconds}'


robots = list()
timeInSeconds = 0
productsQueue = deque()
endProductReceiving = False

# Robots info input -> create objects & add to list
info = [x for x in input().split(';')]
for i in info:
    i = i.split('-')
    rName = i[0]
    processTime = int(i[1])
    robot = Robot(rName, processTime)
    robots.append(robot)

# Starting time input -> starting time in seconds
startingTime = [int(x) for x in input().split(':')]
hours = startingTime[0]
minutes = startingTime[1]
seconds = startingTime[2]
timeInSeconds = seconds + minutes * 60 + hours * 3600

# Products
while True:
    product = ''
    thereIsFreeRobot = False

    timeInSeconds += 1

    if not endProductReceiving:
        product = input()
    elif endProductReceiving and len(productsQueue) > 0:
        product = productsQueue.popleft()
    elif endProductReceiving and len(productsQueue) == 0:
        break

    if product == 'End':
        endProductReceiving = True
        if len(productsQueue) > 0:
            product = productsQueue.popleft()

    for r in robots:
        if r.is_free(timeInSeconds):
            r.start_work(timeInSeconds + r.processingTime)
            print(f"{r.name} - {product} [{seconds_to_hours(timeInSeconds)}]")
            thereIsFreeRobot = True
            break
    if not thereIsFreeRobot:
        productsQueue.append(product)
