from collections import deque

vowels = deque(input().split(' '))
consonants = deque(input().split(' '))

roseLetters = ['r', 'o', 's', 'e']
tulipLetters = ['t', 'u', 'l', 'i', 'p']
lotusLetters = ['l', 'o', 't', 'u', 's']
daffodilLetters = ['d', 'a', 'f', 'f', 'o', 'd', 'i', 'l']
wordFound = False

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    if vowel in roseLetters:
        roseLetters.remove(vowel)
    if vowel in tulipLetters:
        tulipLetters.remove(vowel)
    if vowel in lotusLetters:
        lotusLetters.remove(vowel)
    if vowel in daffodilLetters:
        daffodilLetters.remove(vowel)

    if consonant in roseLetters:
        roseLetters.remove(consonant)
    if consonant in tulipLetters:
        tulipLetters.remove(consonant)
    if consonant in lotusLetters:
        lotusLetters.remove(consonant)
    if consonant in daffodilLetters:
        daffodilLetters.remove(consonant)

    if len(roseLetters) == 0 or len(tulipLetters) == 0 or \
            len(lotusLetters) == 0 or len(daffodilLetters) == 0:
        wordFound = True
        break

if wordFound:
    print("Word found: ", end="")
    if len(roseLetters) == 0:
        print("rose")
    elif len(tulipLetters) == 0:
        print("tulip")
    elif len(lotusLetters) == 0:
        print("lotus")
    elif len(daffodilLetters) == 0:
        print("daffodil")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
