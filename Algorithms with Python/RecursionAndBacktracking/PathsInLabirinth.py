def find_paths(row, col, direction, lab, path):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab):
        return
    if lab[row][col] == '*':
        return
    if lab[row][col] == 'v':
        return

    path.append(direction)

    if lab[row][col] == 'e':
        print("".join(path))
    else:
        lab[row][col] = 'v'
        find_paths(row - 1, col, 'U', lab, path)
        find_paths(row + 1, col, 'D', lab, path)
        find_paths(row, col - 1, 'L', lab, path)
        find_paths(row, col + 1, 'R', lab, path)
        lab[row][col] = '-'

    path.pop()


rows = int(input())
cols = int(input())

lab = []

for _ in range(rows):
    lab.append(list(input()))

find_paths(0, 0, '', lab, [])
