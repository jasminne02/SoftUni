text = input()
characters = dict()

for char in text:
    if char not in characters:
        characters[char] = 1
    elif char in characters:
        characters[char] += 1

for char in sorted(characters.keys()):
    print(f'{char}: {characters[char]} time/s')