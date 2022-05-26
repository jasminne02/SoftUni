# Reads an input string
# Reverses it using a stack
# Prints the result back on the console

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

    def count(self):
        return len(self.stack)


stringInput = input()
stack = Stack()
reversedString = ""

for element in stringInput:
    stack.push(element)

for i in range(stack.count()):
    reversedString += stack.pop()

print(reversedString)
