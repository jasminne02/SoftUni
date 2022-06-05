string = input().split(' ')
mainColors = ['red', 'yellow', 'blue']
secondaryColors = ['orange', 'purple', 'green']
colorsCreated = list()
secondaryColorsCreated = dict()
index = 0

while string:
    if len(string) > 1:
        first = string[0]
        last = string[-1]
        colorOne = first + last
        colorTwo = last + first

        if colorOne in mainColors:
            string.pop(0)
            string.pop()
            colorsCreated.append(colorOne)
            index += 1
        elif colorTwo in mainColors:
            string.pop(0)
            string.pop()
            colorsCreated.append(colorTwo)
            index += 1
        elif colorOne in secondaryColors:
            string.pop(0)
            string.pop()
            secondaryColorsCreated[colorOne] = index
        elif colorTwo in secondaryColors:
            string.pop(0)
            string.pop()
            secondaryColorsCreated[colorTwo] = index
        else:
            first = first[:-1]
            last = last[:-1]
            string.pop(0)
            string.pop()
            if len(string) % 2 == 0:
                middle = len(string) // 2
            else:
                middle = len(string) // 2 + 1
            if first != '':
                string.insert(middle, first)
            if last != '':
                string.insert(middle, last)
    else:
        first = string[0]
        colorOne = first

        if colorOne in mainColors:
            string.pop()
            colorsCreated.append(colorOne)
            index += 1
        elif colorOne in secondaryColors:
            string.pop()
            secondaryColorsCreated[colorOne] = index
        else:
            first = first[:-1]
            string.pop()
            if len(string) % 2 == 0:
                middle = len(string) // 2
            else:
                middle = len(string) // 2 + 1
            if first != '':
                string.insert(middle, first)

if secondaryColorsCreated:
    if ('orange' in secondaryColorsCreated) and ('red' and 'yellow' in colorsCreated):
        colorsCreated.insert(secondaryColorsCreated['orange'], 'orange')
    if ('purple' in secondaryColorsCreated) and ('red' and 'blue' in colorsCreated):
        colorsCreated.insert(secondaryColorsCreated['purple'], 'purple')
    if ('green' in secondaryColorsCreated) and ('yellow' and 'blue' in colorsCreated):
        colorsCreated.insert(secondaryColorsCreated['green'], 'green')

print(colorsCreated)
