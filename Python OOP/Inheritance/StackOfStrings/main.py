class Stack:
    def __init__(self):
        self.data = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if len(self.data) == 0:
            return True
        return False

    def __str__(self):
        info = ', '.join(self.data[::-1])
        return f"[{info}]"


stack = Stack()
stack.push("apple")
stack.push("carrot")
print(stack)
print(stack.pop())
print(stack.top())
stack.push("cucumber")
print(stack)
print(stack.is_empty())
