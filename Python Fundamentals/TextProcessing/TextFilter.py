bannedWords = input().split(', ')
text = input()

for word in bannedWords:
    if word in text:
        text = text.replace(word, '*' * len(word))

print(text)
