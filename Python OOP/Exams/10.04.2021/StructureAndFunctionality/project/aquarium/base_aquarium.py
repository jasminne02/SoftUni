from abc import ABC
from project.fish.base_fish import BaseFish
from project.decoration.base_decoration import BaseDecoration


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        comfort_sum = 0
        for decoration in self.decorations:
            comfort_sum += decoration.comfort
        return comfort_sum

    def add_fish(self, fish: BaseFish):
        if not self.__has_enough_capacity():
            return "Not enough capacity."
        if self.__appropriate_aquarium_type(fish):
            self.fish.append(fish)
            return f"Successfully added {fish.type()} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result_info = f"{self.name}:\nFish: "
        if self.fish:
            for fish in self.fish:
                result_info += f"{fish.name} "
        else:
            result_info += "none\n"
        result_info += f"Decorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}"
        return result_info

    def type(self):
        return self.__class__.__name__

    def calculate_total_fish_price(self):
        price = 0
        for fish in self.fish:
            price += fish.price
        return price

    def calculate_total_decoration_price(self):
        price = 0
        for decoration in self.decorations:
            price += decoration.price
        return price

    #  PRIVATE METHODS  #
    def __has_enough_capacity(self):
        if len(self.fish) + 1 > self.capacity:
            return False
        return True

    def __appropriate_aquarium_type(self, fish: BaseFish):
        if self.type() == fish.aquarium_type():
            return True
        return False
