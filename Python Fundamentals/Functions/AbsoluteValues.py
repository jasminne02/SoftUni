numberSequence = input().split(' ')
newSequence = []

for number in numberSequence:
    newSequence.append(abs(float(number)))

print(newSequence)
