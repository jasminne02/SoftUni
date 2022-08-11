from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    valid_car_types = {
        'MuscleCar': MuscleCar,
        'SportsCar': SportsCar
    }

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.valid_car_types:
            return
        if self.__is_car_model_existing(model):
            raise Exception(f"Car {model} is already created!")
        car = self.valid_car_types[car_type](model, speed_limit)
        self.cars.append(car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if not self.__is_driver_name_unique(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if not self.__is_race_name_unique(race_name):
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__get_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        car = self.__get_available_car(car_type)
        if car is None:
            raise Exception(f"Car {car_type} could not be found!")
        if driver.car:
            old_model = driver.car.model
            driver.car.is_taken = False
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."
        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__get_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        driver = self.__get_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__get_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        winners = self.__get_race_winners(race)
        output = ''
        for winner in winners:
            winner.number_of_wins += 1
            output += f"Driver {winner.name} wins the {race_name} race with a speed of {winner.car.speed_limit}.\n"
        return output.strip()

    #  PRIVATE METHODS  #
    def __is_car_model_existing(self, model: str):
        for car in self.cars:
            if car.model == model:
                return True
        return False

    def __is_driver_name_unique(self, name: str):
        for driver in self.drivers:
            if driver.name == name:
                return False
        return True

    def __is_race_name_unique(self, name: str):
        for race in self.races:
            if race.name == name:
                return False
        return True

    def __get_driver_by_name(self, name: str):
        for driver in self.drivers:
            if driver.name == name:
                return driver

    def __get_race_by_name(self, name: str):
        for race in self.races:
            if race.name == name:
                return race

    def __get_available_car(self, car_type: str):
        available_car = None
        for car in self.cars:
            if car.type() == car_type and not car.is_taken:
                available_car = car
        return available_car

    @staticmethod
    def __get_race_winners(race: Race):
        driver_speed_dict = {}  # {} -> driver: speed_limit
        for driver in race.drivers:
            driver_speed_dict[driver] = driver.car.speed_limit

        sorted_driver_speed_dict = sorted(driver_speed_dict.items(), key=lambda x: -x[1])
        winners = []
        for driver, speed in sorted_driver_speed_dict:
            winners.append(driver)
            if len(winners) == 3:
                break

        return winners
