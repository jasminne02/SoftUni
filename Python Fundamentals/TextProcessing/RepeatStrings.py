stringSequence = input().split(' ')
finalString = ''

for substring in stringSequence:
    repeat = len(substring)

    finalString += substring * repeat

print(finalString)
