from project.planet.planet_repository import PlanetRepository
from project.planet.planet import Planet
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class SpaceStation:
    valid_astronaut_types = {
        'Biologist': Biologist,
        'Geodesist': Geodesist,
        'Meteorologist': Meteorologist
    }

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.__successful_missions = 0
        self.__not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.valid_astronaut_types:
            raise Exception("Astronaut type is not valid!")
        if not self.__is_astronaut_name_unique(name):
            return f"{name} is already added."
        astronaut = self.valid_astronaut_types[astronaut_type](name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if not self.__is_planet_name_unique(name):
            return f"{name} is already added."
        planet = Planet(name)
        planet.items = items.split(', ')
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.__get_astronaut_by_name(name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.__get_planet_by_name(planet_name)
        if planet is None:
            self.__not_completed_missions += 1
            raise Exception("Invalid planet name!")
        astronauts = self.__get_suitable_astronauts()
        if astronauts is None:
            self.__not_completed_missions += 1
            raise Exception("You need at least one astronaut to explore the planet!")

        for astronaut in astronauts:
            while True:
                if planet.items:
                    item = planet.items.pop()
                    astronaut.backpack.append(item)
                    astronaut.breathe()
                    if astronaut.oxygen <= 0:
                        astronaut.oxygen = 0
                        break
                else:
                    break

        if planet.items:
            self.__not_completed_missions += 1
            return "Mission is not completed."
        self.__successful_missions += 1
        return f"Planet: {planet_name} was explored. {len(astronauts)} astronauts participated in collecting items."

    def report(self):
        output = f'{self.__successful_missions} successful missions!\n' \
                 f'{self.__not_completed_missions} missions were not completed!\n' \
                 f'Astronauts\' info:\n'
        for astronaut in self.astronaut_repository.astronauts:
            output += f'Name: {astronaut.name}\nOxygen: {astronaut.oxygen}\n'
            if len(astronaut.backpack) > 0:
                output += f'Backpack items: {", ".join([str(x) for x in astronaut.backpack])}\n'
            else:
                output += f'Backpack items: none\n'
        return output.strip()

    #  PRIVATE METHODS  #
    def __is_astronaut_name_unique(self, name: str):
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                return False
        return True

    def __is_planet_name_unique(self, name: str):
        for planet in self.planet_repository.planets:
            if planet.name == name:
                return False
        return True

    def __get_astronaut_by_name(self, name: str):
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                return astronaut

    def __get_planet_by_name(self, name: str):
        for planet in self.planet_repository.planets:
            if planet.name == name:
                return planet

    def __get_suitable_astronauts(self):
        suitable_astronauts = []
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.oxygen > 30:
                suitable_astronauts.append(astronaut)
        if len(suitable_astronauts) == 0:
            return
        suitable_astronauts = self.__sort_astronauts_by_descending_order_by_oxygen(suitable_astronauts)
        return suitable_astronauts

    @staticmethod
    def __sort_astronauts_by_descending_order_by_oxygen(suitable_astronauts):
        astronauts = {}
        for astronaut in suitable_astronauts:
            oxygen = astronaut.oxygen
            astronauts[astronaut] = oxygen
        sorted_astronauts = sorted(astronauts.items(), key=lambda x: x[1])

        while len(sorted_astronauts) > 5:
            sorted_astronauts.pop(0)

        astronauts = []
        for astronaut, oxygen in sorted_astronauts:
            astronauts.append(astronaut)
        return astronauts
