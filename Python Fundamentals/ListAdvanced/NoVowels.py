text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
vowelsUpper = [letter.upper() for letter in vowels]
vowels.extend(vowelsUpper)
textList = [letter for letter in text if letter not in vowels]
print(''.join(textList))
