class Jockey:
    MIN_AGE = 18

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = None  # Horse object

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value or value.strip() == '':
            raise ValueError(f"Name should contain at least one character!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < self.MIN_AGE:
            raise ValueError(f"Jockeys must be at least 18 to participate in the race!")
        self.__age = value
