string_input = input()
counter_input = int(input())


def new_string(string, counter):
    new_string_return = ''
    for count in range(counter):
        new_string_return += string

    return new_string_return


print(new_string(string_input, counter_input))
