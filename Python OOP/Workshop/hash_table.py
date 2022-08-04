class HashTable():
    def __init__(self):
        self.array = [None] * 4
        self.__dict = {}
        self.__array_idx = 0

    def hash(self, key: str):
        if key not in self.array:
            self.array.pop(self.__array_idx)
            self.array.insert(self.__array_idx, key)
            self.__array_idx += 1

    def add(self, key: str, value):
        if len(self.__dict) == len(self.array):
            for _ in range(len(self.array)):
                self.array.append(None)
        self.__dict[key] = value
        self.hash(key)

    def get(self, key: str):
        if key in self.__dict:
            return self.__dict[key]

    def __len__(self):
        return len(self.array)

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)
