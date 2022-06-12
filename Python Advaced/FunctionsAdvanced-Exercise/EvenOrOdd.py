def even_odd(*args):
    result =[]
    command = args[-1]
    if command == 'even':
        for i in range(len(args) - 1):
            if args[i] % 2 == 0:
                result.append(i)
    elif command == 'odd':
        for i in range(len(args) - 1):
            if args[i] % 2 != 0:
                result.append(i)
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
