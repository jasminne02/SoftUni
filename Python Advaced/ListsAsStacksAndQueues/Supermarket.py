from collections import deque

queue = deque()

while True:
    command = input()

    if command == 'End':
        print(f"{len(queue)} people remaining.")

        break
    elif command == 'Paid':
        for i in range(len(queue)):
            print(queue.popleft())

        continue

    queue.append(command)
