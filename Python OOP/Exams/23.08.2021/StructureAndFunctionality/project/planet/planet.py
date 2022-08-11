class Planet:
    def __init__(self, name: str):
        self.name = name
        self.items = []  # contains items that could be found

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value == ' ':
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value
