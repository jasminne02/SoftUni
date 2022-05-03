wordsCount = int(input())
synonymsDic = {}

for count in range(wordsCount):
    key = input()
    value = input()

    if key not in synonymsDic:
        synonymsDic[key] = []

    synonymsDic[key].append(value)

for key in synonymsDic.keys():
    print(f"{key} - {', '.join(synonymsDic[key])}")
