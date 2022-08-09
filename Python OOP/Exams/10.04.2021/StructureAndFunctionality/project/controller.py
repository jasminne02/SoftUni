from project.decoration.decoration_repository import DecorationRepository
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.fish.saltwater_fish import SaltwaterFish
from project.fish.freshwater_fish import FreshwaterFish
from project.decoration.plant import Plant
from project.decoration.ornament import Ornament


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        aquarium = self.__create_aquarium_by_type_and_name(aquarium_type, aquarium_name)
        if aquarium is None:
            return "Invalid aquarium type."
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        decoration = self.__create_decoration_by_type(decoration_type)
        if decoration is None:
            return "Invalid decoration type."
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.__get_aquarium_by_name(aquarium_name)
        decoration = self.__get_decoration_by_type(decoration_type)
        if decoration is None:
            return f"There isn't a decoration of type {decoration_type}."
        if aquarium:
            self.decorations_repository.decorations.remove(decoration)
            aquarium.add_decoration(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        aquarium = self.__get_aquarium_by_name(aquarium_name)
        fish = self.__create_fish_by_type_and_params(fish_type, fish_name, fish_species, price)
        if fish is None:
            return f"There isn't a fish of type {fish_type}."
        result = aquarium.add_fish(fish)
        if result:
            return result
        return "Water not suitable."

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__get_aquarium_by_name(aquarium_name)
        aquarium.feed()
        fed_count = len(aquarium.fish)
        return f"Fish fed: {fed_count}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__get_aquarium_by_name(aquarium_name)
        price = aquarium.calculate_total_decoration_price() + aquarium.calculate_total_fish_price()
        return f"The value of Aquarium {aquarium_name} is {price:.2f}."

    def report(self):
        result_info = ""
        for aquarium in self.aquariums:
            result_info += aquarium.__str__()
        return result_info

    #  PRIVATE METHODS  #
    def __get_aquarium_by_name(self, aquarium_name: str):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
        return None

    def __get_decoration_by_type(self, decoration_type: str):
        for decoration in self.decorations_repository.decorations:
            if decoration.type() == decoration_type:
                return decoration

    @staticmethod
    def __create_aquarium_by_type_and_name(aquarium_type: str, aquarium_name: str):
        if aquarium_type == 'FreshwaterAquarium':
            return FreshwaterAquarium(aquarium_name)
        elif aquarium_type == 'SaltwaterAquarium':
            return SaltwaterAquarium(aquarium_name)

    @staticmethod
    def __create_decoration_by_type(decoration_type: str):
        if decoration_type == 'Plant':
            return Plant()
        elif decoration_type == 'Ornament':
            return Ornament()

    @staticmethod
    def __create_fish_by_type_and_params(fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type == 'SaltwaterFish':
            return SaltwaterFish(fish_name, fish_species, price)
        elif fish_type == 'FreshwaterFish':
            return FreshwaterFish(fish_name, fish_species, price)
