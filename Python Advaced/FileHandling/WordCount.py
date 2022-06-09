import re

firstFile = 'words.txt'
secondFile = 'text.txt'

with open(firstFile, 'w') as file:
    file.write('quick is fault')
with open(secondFile, 'w') as file:
    file.write("-I was quick to judge him, but it wasn't his fault.")
    file.write("-Is this some kind of joke?! Is it?")
    file.write("-Quick, hide here…It is safer.")

try:
    wordsFile = open(firstFile, 'r')
    textFile = open(secondFile, 'r')
except FileNotFoundError:
    print('File not found!')
else:
    words = dict()
    textWords = list()

    for line in wordsFile:
        for word in line.split(' '):
            words[word] = 0

    for line in textFile:
        for word in re.split(' |-|,|\?|\.|!', line):
            word = word.lower()
            textWords.append(word)

    for word in words.keys():
        words[word] = textWords.count(word)

    words = {k: v for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True)}

    for word, count in words.items():
        print(f'{word} - {count}')

    wordsFile.close()
    textFile.close()
