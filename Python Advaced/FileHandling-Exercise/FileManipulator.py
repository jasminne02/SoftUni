import os

while True:
    command = input()
    if command == 'End':
        break

    command = command.split('-')

    if 'Create' in command:
        fileName = command[1]
        with open(fileName, 'w') as file:
            pass
    elif 'Add' in command:
        fileName = command[1]
        content = command[2]
        with open(fileName, 'a') as file:
            file.write(content + '\n')
    elif 'Replace' in command:
        fileName = command[1]
        oldString = command[2]
        newString = command[3]
        try:
            with open(fileName, 'r+') as file:
                content = file.read().replace(oldString, newString)
                file.seek(0)
                file.truncate()
                file.write(content)
        except FileNotFoundError:
            print('An error occurred')
    elif 'Delete' in command:
        fileName = command[1]
        try:
            os.remove(fileName)
        except FileNotFoundError:
            print('An error occurred')
