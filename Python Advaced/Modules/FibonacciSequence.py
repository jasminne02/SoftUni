from FibonacciSequencePackage import *

sequence = ''

while True:
    command = input()
    if command == 'Stop':
        break

    if 'Create' in command:
        command, _, number = command.split(' ')
        number = int(number)
        sequence = create(number)
        print(sequence)
    elif 'Locate' in command:
        command, number = command.split(' ')
        number = int(number)
        locate(number, sequence)
