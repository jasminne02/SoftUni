class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.__index = None
        self.__counter = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index is None and self.__counter is None:
            self.__index = 0
            self.__counter = 0
        elif self.__index == len(self.sequence):
            self.__index = 0

        if self.__counter >= self.number:
            self.__index = None
            self.__counter = None
            raise StopIteration

        if self.__index < len(self.sequence):
            char = self.sequence[self.__index]
            self.__index += 1
            self.__counter += 1
            return char


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

print()

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
