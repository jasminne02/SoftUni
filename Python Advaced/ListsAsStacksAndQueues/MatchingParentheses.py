class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def count(self):
        return len(self.stack)


algebraicExpression = input()
parenthesesStack = Stack()
setsOfParentheses = list()
oneSet = ""

for index in range(len(algebraicExpression)):
    element = algebraicExpression[index]

    if element == '(':
        parenthesesStack.push(index)
    elif element == ')':
        for i in range(parenthesesStack.pop(), index + 1):
            oneSet += algebraicExpression[i]

        setsOfParentheses.append(oneSet)
        oneSet = ""

print("\n".join(setsOfParentheses))
