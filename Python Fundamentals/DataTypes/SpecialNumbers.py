n = int(input())
for i in range(1, n + 1):
    k = i
    number = 0
    specialNum = False

    while k != 0:
        number += k % 10
        k = k // 10

    if number == 5 or number == 7 or number == 11:
        specialNum = True

    print(f'{i} -> {specialNum}')
