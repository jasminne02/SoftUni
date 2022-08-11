from abc import ABC, abstractmethod


class Astronaut(ABC):
    NEEDED_OXYGEN_TO_BREATHE = 10

    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []  # contains collected items

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value == ' ':
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.NEEDED_OXYGEN_TO_BREATHE

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
