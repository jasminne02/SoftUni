class Driver:
    def __init__(self, name: str):
        self.name = name
        self.car = None  # car of type Car()
        self.number_of_wins = 0  # increases when a race is won

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value or value.strip() == '':
            raise ValueError("Name should contain at least one character!")
        self.__name = value
