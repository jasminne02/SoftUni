from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.horse_race import HorseRace


class HorseRaceApp:
    valid_horse_types = {
        'Appaloosa': Appaloosa,
        'Thoroughbred': Thoroughbred
    }

    created_valid_horse_races = {
        'Winter': False,
        'Spring': False,
        'Autumn': False,
        'Summer': False
    }

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []
        self.__horses_list_before_change = self.horses.copy()

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.valid_horse_types:
            return
        if not self.__is_horse_name_unique(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")
        horse = self.valid_horse_types[horse_type](horse_name, horse_speed)
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if not self.__is_jockey_name_unique(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in self.created_valid_horse_races:
            if self.created_valid_horse_races[race_type]:
                raise Exception(f"Race {race_type} has been already created!")
            self.created_valid_horse_races[race_type] = True
        horse_race = HorseRace(race_type)
        self.horse_races.append(horse_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__get_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        horse = self.__get_last_horse_by_type(horse_type)
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse:
            self.__decline_horse()
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = self.__get_horse_race_by_type(race_type)
        if horse_race is None:
            raise Exception(f"Race {race_type} could not be found!")
        jockey = self.__get_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = self.__get_horse_race_by_type(race_type)
        if horse_race is None:
            raise Exception(f"Race {race_type} could not be found!")
        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        winner = self.__get_horse_race_winner(horse_race)
        return f"The winner of the {race_type} race, with a speed of " \
               f"{winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."

    #  PRIVATE METHODS  #
    def __is_horse_name_unique(self, name: str):
        for horse in self.horses:
            if horse.name == name:
                return False
        return True

    def __is_jockey_name_unique(self, name: str):
        for jockey in self.jockeys:
            if jockey.name == name:
                return False
        return True

    def __get_jockey_by_name(self, name: str):
        for jockey in self.jockeys:
            if jockey.name == name:
                return jockey

    def __get_horse_race_by_type(self, race_type: str):
        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                return horse_race

    def __get_last_horse_by_type(self, horse_type: str):
        self.__horses_list_before_change = self.horses.copy()
        self.horses.reverse()
        for horse in self.horses:
            if horse.type() == horse_type and not horse.is_taken:
                self.horses.remove(horse)
                self.horses.reverse()
                return horse

    def __decline_horse(self):
        self.horses = self.__horses_list_before_change

    @staticmethod
    def __get_horse_race_winner(horse_race: HorseRace):
        jockey_with_fastest_horse = horse_race.jockeys[0]
        max_speed = jockey_with_fastest_horse.horse.speed
        for jockey in horse_race.jockeys:
            if jockey.horse.speed > max_speed:
                max_speed = jockey.horse.speed
                jockey_with_fastest_horse = jockey
        return jockey_with_fastest_horse
