def create(count):
    n1, n2 = 0, 1
    sequence = ''

    if count >= 2:
        sequence = str(n1) + ' ' + str(n2) + ' '
        count -= 2

    while count > 0:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count -= 1
        sequence += str(nth) + ' '

    return sequence


def locate(number, sequence):
    if str(number) in sequence:
        sqnce = list(sequence.split(' '))
        index = sqnce.index(str(number))

        print(f"The number - {number} is at index {index}")
    else:
        print(f"The number {number} is not in the sequence")
