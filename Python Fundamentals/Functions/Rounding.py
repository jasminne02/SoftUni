numberSequence = input().split(' ')
newSequence = []

for number in numberSequence:
    newSequence.append(round(float(number)))

print(newSequence)
