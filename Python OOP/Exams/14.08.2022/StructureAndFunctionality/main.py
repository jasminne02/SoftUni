from project.jockey import Jockey
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.horse_race import HorseRace
from project.horse_race_app import HorseRaceApp


def test1():
    horse_race_app = HorseRaceApp()
    # horses
    print(horse_race_app.add_horse('Appaloosa', 'Amilia', 90))
    print(horse_race_app.add_horse('Thoroughbred', 'Thunder', 110))
    print(horse_race_app.add_horse('Thoroughbred', 'Bold', 87))
    print(horse_race_app.add_horse('Appaloosa', 'Alisa', 105))
    print(horse_race_app.add_horse('Thoroughbred', 'Storm', 115))
    # jockeys
    print(horse_race_app.add_jockey('Rian', 19))
    print(horse_race_app.add_jockey('William', 24))
    print(horse_race_app.add_jockey('Daniel', 21))
    # races
    print(horse_race_app.create_horse_race('Winter'))
    print(horse_race_app.create_horse_race('Spring'))
    # add horse to jockey
    print(horse_race_app.add_horse_to_jockey('Rian', 'Appaloosa'))
    print(horse_race_app.add_horse_to_jockey('William', 'Appaloosa'))
    print(horse_race_app.add_horse_to_jockey('Daniel', 'Thoroughbred'))
    # add jockey to horse race
    print(horse_race_app.add_jockey_to_horse_race('Spring', 'Rian'))
    print(horse_race_app.add_jockey_to_horse_race('Spring', 'William'))
    print(horse_race_app.add_jockey_to_horse_race('Spring', 'Daniel'))
    # start horse race
    print(horse_race_app.start_horse_race('Spring'))


def test2():
    horseRaceApp = HorseRaceApp()
    print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
    print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
    print(horseRaceApp.add_jockey("Peter", 19))
    print(horseRaceApp.add_jockey("Mariya", 21))
    print(horseRaceApp.create_horse_race("Summer"))
    print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
    print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
    print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
    print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
    print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
    print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
    print(horseRaceApp.start_horse_race("Summer"))


if __name__ == '__main__':
    test2()
