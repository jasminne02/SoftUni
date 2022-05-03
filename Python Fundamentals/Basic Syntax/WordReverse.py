word = input()
reversedWord = ""
for i in range(len(word) - 1, -1, -1):
    reversedWord += word[i]
print(reversedWord)
