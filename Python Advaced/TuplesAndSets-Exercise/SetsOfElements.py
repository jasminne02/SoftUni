n, m = tuple(int(x) for x in input().split(' '))
first = set()
second = set()

for i in range(n):
    line = int(input())
    first.add(line)
for i in range(m):
    line = int(input())
    second.add(line)

[print(x) for x in first.intersection(second)]