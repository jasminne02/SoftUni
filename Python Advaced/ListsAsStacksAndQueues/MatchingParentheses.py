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

for element in algebraicExpression:
    if element == '(' or element == ')':
        parenthesesStack.push(algebraicExpression.index(element))

for i in range(parenthesesStack.count()):
    lastClosingParenthesesIndex = parenthesesStack.pop()
    lastOpeningParenthesesIndex = parenthesesStack.pop()

    

print("\n".join(setsOfParentheses))
