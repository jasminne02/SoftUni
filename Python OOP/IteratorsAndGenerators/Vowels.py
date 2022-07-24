class vowels:
    __VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

    def __init__(self, string):
        self.string = string
        self.index = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.index is None:
            self.index = 0

        if self.index < len(self.string):
            character = self.string[self.index]
            self.index += 1
            if character.lower() in vowels.__VOWELS:
                return character
            else:
                while self.index < len(self.string):
                    character = self.string[self.index]
                    if character.lower() in vowels.__VOWELS:
                        self.index += 1
                        return character
                    self.index += 1
        else:
            self.index = None
            raise StopIteration


my_string = vowels('Abcedifuty0o')

for char in my_string:
    print(char)
