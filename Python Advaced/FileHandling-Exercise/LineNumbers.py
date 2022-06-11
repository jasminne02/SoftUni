symbols = ['-', ',', '.', '?', '!']

with open("text.txt", "r") as file:
    otherFile = open("output.txt", "w")

    for idx, line in enumerate(file):
        symbolsCount = 0
        lettersCount = 0

        for el in line:
            if el in symbols:
                symbolsCount += 1
            elif el != " ":
                lettersCount += 1

        newLine = f"Line {idx+1}: {line} ({lettersCount}) ({symbolsCount})\n"
        otherFile.write(newLine)

    otherFile.close()
