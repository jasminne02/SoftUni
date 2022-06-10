symbols = ['-', ',', '.', '?', '!']

with open('text.txt', 'r') as file:
    for idx, line in enumerate(file):
        if idx % 2 != 0:
            result = ' '.join(line.strip().split()[::-1])
            if line[0] != '-':
                result += ' ' + x
            for s in symbols:
                result = result.replace(s, '@')
            print(result)
        else:
            x = ' '.join(line.strip().split()[::-1])
