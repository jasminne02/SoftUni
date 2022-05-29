guestNumber = int(input())
vipCodes = set()
regularCode = set()

for n in range(guestNumber):
    code = input()

    if code[0].isdigit():
        vipCodes.add(code)
    else:
        regularCode.add(code)

while True:
    code = input()
    if code == 'END':
        break

    if code[0].isdigit():
        vipCodes.remove(code)
    else:
        regularCode.remove(code)

vipCodes = list(vipCodes)
regularCode = list(regularCode)
vipCodes.sort()
regularCode.sort()

print(len(vipCodes) + len(regularCode))
for code in vipCodes:
    print(code)
for code in regularCode:
    print(code)
