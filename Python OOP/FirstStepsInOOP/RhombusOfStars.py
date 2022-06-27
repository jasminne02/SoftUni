def print_rhombus(size):
    for n in range(size):
        spaces_count = size - 1 - n
        stars_count = n + 1
        print(' ' * spaces_count + '* ' * stars_count)
    for n in range(size - 1, -1, -1):
        spaces_count = size - n
        stars_count = n
        print(' ' * spaces_count + '* ' * stars_count)


num = int(input())
print_rhombus(num)
