def naughty_or_nice_list(kids_names, *args, **kwargs):
    nice = []
    naughty = []
    not_found = []
    return_string = ''

    for command in args:
        command = command.split('-')
        num = int(command[0])
        command = command[1]

        count = 0
        kid_info = ''
        name = ''
        for info in kids_names:
            if num in info:
                count += 1
                kid_info = info
                _, name = info

        if command == 'Naughty' and count == 1:
            naughty.append(name)
            kids_names.remove(kid_info)
        elif command == 'Nice' and count == 1:
            nice.append(name)
            kids_names.remove(kid_info)

    for name, value in kwargs.items():
        count = 0
        kid_info = ''

        for info in kids_names:
            if name in info:
                count += 1
                kid_info = info

        if value == 'Naughty' and count == 1:
            naughty.append(name)
            kids_names.remove(kid_info)
        elif value == 'Nice' and count == 1:
            nice.append(name)
            kids_names.remove(kid_info)

    for info in kids_names:
        _, name = info
        not_found.append(name)

    if nice:
        return_string = 'Nice: '
        for idx in range(len(nice)):
            if idx == len(nice)-1:
                return_string += nice[idx] + '\n'
            else:
                return_string += nice[idx] + ', '

    if naughty:
        return_string += 'Naughty: '
        for idx in range(len(naughty)):
            if idx == len(naughty)-1:
                return_string += naughty[idx] + '\n'
            else:
                return_string += naughty[idx] + ', '

    if not_found:
        return_string += 'Not found: '
        for idx in range(len(not_found)):
            if idx == len(not_found)-1:
                return_string += not_found[idx]
            else:
                return_string += not_found[idx] + ', '

    return return_string


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print()

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))
print()

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
