class IntegerList:
    def __init__(self, initial_integers: list):
        for element in initial_integers:
            if not isinstance(element, int):
                raise ValueError
        self.list = initial_integers

    def add(self, value):
        if isinstance(value, int):
            self.list.append(value)
            return self.list
        else:
            raise ValueError

    def remove_index(self, index):
        if index < 0 or index >= len(self.list):
            raise IndexError
        else:
            self.list.pop(index)
            return self.list

    def get(self, index):
        if index < 0 or index >= len(self.list):
            raise IndexError
        else:
            return self.list[index]

    def insert(self, index, value):
        if index < 0 or index >= len(self.list):
            raise IndexError
        if not isinstance(value, int):
            raise ValueError

        self.list.insert(index, value)

    def get_biggest(self):
        return max(self.list)

    def get_index(self, value):
        if value in self.list:
            return self.list.index(value)
