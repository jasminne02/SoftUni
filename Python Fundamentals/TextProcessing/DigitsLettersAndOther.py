string = input()

allDigits = ''
allLetters = ''
allChars = ''

for c in string:
    if c.isdigit():
        allDigits += c
    elif c.isalpha():
        allLetters += c
    else:
        allChars += c

print(f'{allDigits}\n{allLetters}\n{allChars}')
