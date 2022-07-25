class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.__counter = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter is None:
            self.__counter = self.count

        if self.__counter >= 0:
            number = self.__counter
            self.__counter -= 1
            return number
        else:
            self.__counter = None
            raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
