def print_triangle(size):
    x = []
    for row in range(1, size+1):
        x.append(str(row))
        print(' '.join(x))
    for row in range(size, 1, -1):
        x.remove(str(row))
        print(' '.join(x))
