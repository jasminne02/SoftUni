def list_manipulator(numbersList, command, part, *args):
    if command == 'add':
        if part == 'beginning':
            return list(args) + numbersList
        elif part == 'end':
            return numbersList + list(args)
    elif command == 'remove':
        x = 'none'
        for i in args:
            x = i

        if part == 'beginning':
            if x != 'none':
                for _ in range(x):
                    numbersList.pop(0)
            else:
                numbersList.pop(0)
        if part == 'end':
            if x != 'none':
                for _ in range(x):
                    numbersList.pop()
            else:
                numbersList.pop()

        return numbersList


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
