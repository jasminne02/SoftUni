import sys
from Stack import Stack

stack = Stack()
number = int(input())
maxNum = -sys.maxsize
minNum = sys.maxsize
stack2 = Stack()

for i in range(number):
    command = input()

    if '1' in command:
        command = command.split(' ')
        num = int(command[1])
        stack.push(num)
    elif '2' in command:
        if stack.count() > 0:
            stack.pop()
    elif '3' in command:
        if stack.count() > 0:
            for p in range(stack.count()):
                x = stack.pop()
                stack2.push(x)

                if x > maxNum:
                    maxNum = x

            for p in range(stack2.count()):
                x = stack2.pop()
                stack.push(x)

            print(maxNum)
    elif '4' in command:
        if stack.count() > 0:
            for p in range(stack.count()):
                x = stack.pop()
                stack2.push(x)

                if x < minNum:
                    minNum = x

            for p in range(stack2.count()):
                x = stack2.pop()
                stack.push(x)

            print(minNum)

stackLen = stack.count()

for i in range(stackLen):
    if i == stackLen - 1:
        print(stack.pop())
    else:
        print(stack.pop(), end=', ')
