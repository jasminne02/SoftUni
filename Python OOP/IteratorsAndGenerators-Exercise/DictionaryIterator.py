class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.__index = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index is None:
            self.__index = 0

        if self.__index < len(self.dictionary):
            key, value = None, None
            count = 0

            for k, v in self.dictionary.items():
                if count == self.__index:
                    key = k
                    value = v
                    break
                count += 1

            self.__index += 1
            return (key, value)
        else:
            self.__index = None
            raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

print()

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
