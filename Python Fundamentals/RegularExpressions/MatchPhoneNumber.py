import re

text = input()
matches = re.finditer(r"\+359([ -])2\1\d{3}\1\d{4}\b", text)

listM = []

for match in matches:
    listM.append(match.group())

print(', '.join(listM))
