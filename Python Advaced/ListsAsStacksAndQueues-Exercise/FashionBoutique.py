from Stack import Stack

clothingBoxString = input().split(' ')
rackCapacity = int(input())
clothingBox = Stack()
clothingSum = 0
racks = 0

for element in clothingBoxString:
    clothingBox.push(element)

for i in range(clothingBox.count()):
    currentCloth = int(clothingBox.pop())
    clothingSum += currentCloth

    if clothingSum == rackCapacity:
        racks += 1
        clothingSum = 0
    elif clothingSum > rackCapacity:
        clothingSum = currentCloth
        racks += 1

    elif i == clothingBox.count():
        racks += 1

if clothingSum > 0:
    racks += 1

print(racks)
