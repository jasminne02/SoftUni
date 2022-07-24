class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.index is None:
            self.index = len(self.iterable) - 1

        if self.index > -1:
            x = self.iterable[self.index]
            self.index -= 1
            return x
        elif self.index == -1:
            self.index = None
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])

for item in reversed_list:
    print(item)
