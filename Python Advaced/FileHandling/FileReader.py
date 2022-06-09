try:
    file = open("numbers.txt", "r")
    numSum = 0
    for number in file:
        numSum += int(number)
    print(numSum)

except FileNotFoundError:
    print("File not found")
