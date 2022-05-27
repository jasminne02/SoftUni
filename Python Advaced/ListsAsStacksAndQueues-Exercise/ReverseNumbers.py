from Stack import Stack

stringInput = input().split(' ')
stack = Stack()

for element in stringInput:
    stack.push(element)

for i in range(stack.count()):
    print(stack.pop(), end=' ')
