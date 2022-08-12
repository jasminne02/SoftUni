class Player:
    DEFAULT_STAMINA = 100
    MAX_STAMINA = DEFAULT_STAMINA
    MIN_STAMINA = 0
    MIN_AGE = 12

    taken_names = []  # contains all players' names

    def __init__(self, name: str, age: int, stamina=DEFAULT_STAMINA):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("Name not valid!")
        if value in self.taken_names:
            raise Exception(f"Name {value} is already used!")
        self.taken_names.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < self.MIN_AGE:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value: int):
        if value < self.MIN_STAMINA or value > self.MAX_STAMINA:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        if self.stamina < self.MAX_STAMINA:
            return True
        return False

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
