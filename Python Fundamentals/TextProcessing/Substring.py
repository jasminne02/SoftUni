stringF = input()
stringS = input()

while stringF in stringS:
    stringS = stringS.replace(stringF, "")

print(stringS)
