class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.__current_step = None
        self.__counter = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_step is None and self.__counter is None:
            self.__current_step = 0
            self.__counter = 0

        if self.__counter < self.count:
            steps = self.__current_step
            self.__current_step += self.step
            self.__counter += 1
            return steps
        else:
            raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

print()

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
