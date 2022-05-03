names = input().split(', ')
sortedNames = sorted(names, key=lambda x: (-len(x), x))
print(sortedNames)
