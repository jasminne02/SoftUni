words = input().split(' ')
palindrome = input()
palindromeCount = words.count(palindrome)
palindromeList = []

for i in words:
    word = [letter for letter in i]
    word.reverse()
    reversedWord = ''
    for letter in word:
        reversedWord += letter

    if reversedWord == i:
        palindromeList.append(i)

print(f'{palindromeList}\nFound palindrome {palindromeCount} times')
