words = {}

while True:
    command = input()
    if command == 'end':
        break

    else:
        reversedWord = ''

        for letter in range(len(command)-1, -1, -1):
            reversedWord += command[letter]

        words[command] = reversedWord

for (key, value) in words.items():
    print(f'{key} = {value}')
