from collections import deque

numbers = deque(input().split())
target = int(input())
counter = 0
pair = []
unique_pair = set()

while len(numbers) > 0:
    for index in range(len(numbers) - 1):
        counter += 1
        if int(numbers[0]) + int(numbers[index + 1]) == target:
            pair.append(int(numbers[0]))
            pair.append(int(numbers[index + 1]))
            pair = tuple(pair)
            unique_pair.add(pair)
            pair = []
            print(f"{int(numbers[0])} + {int(numbers[index + 1])} = {target}")

    numbers.popleft()

print(f"Iterations done: {counter}")
[print(x) for x in unique_pair]
