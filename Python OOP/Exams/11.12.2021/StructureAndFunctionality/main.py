from project.controller import Controller


def test1():
    controller = Controller()
    print(controller.create_car('SportsCar', 'A111', 550))
    print(controller.create_car('MuscleCar', '6151', 340))
    print(controller.create_car('MuscleCar', '7861', 370))
    print(controller.create_car('SportsCar', 'W123', 500))
    print(controller.create_car('MuscleCar', '3425', 300))
    print(controller.create_driver('Mike'))
    print(controller.create_driver('John'))
    print(controller.create_driver('Will'))
    print(controller.create_driver('Alex'))
    print(controller.create_driver('Gabriel'))
    print(controller.add_car_to_driver('Mike', 'MuscleCar'))
    print(controller.add_car_to_driver('John', 'SportsCar'))
    print(controller.add_car_to_driver('Will', 'MuscleCar'))
    print(controller.add_car_to_driver('Alex', 'SportsCar'))
    print(controller.add_car_to_driver('Gabriel', 'MuscleCar'))
    print(controller.create_race('Summer race'))
    print(controller.add_driver_to_race('Summer race', 'Mike'))
    print(controller.add_driver_to_race('Summer race', 'John'))
    print(controller.add_driver_to_race('Summer race', 'Will'))
    print(controller.add_driver_to_race('Summer race', 'Alex'))
    print(controller.add_driver_to_race('Summer race', 'Gabriel'))
    print('\n\n')
    print(controller.start_race('Summer race'))


def test2():
    controller = Controller()
    print(controller.create_driver("Peter"))
    print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
    print(controller.add_car_to_driver("Peter", "SportsCar"))
    print(controller.create_car("SportsCar", "Porsche 911", 580))
    print(controller.add_car_to_driver("Peter", "SportsCar"))
    print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
    print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
    print(controller.create_driver("John"))
    print(controller.create_driver("Jack"))
    print(controller.create_driver("Kelly"))
    print(controller.add_car_to_driver("Kelly", "MuscleCar"))
    print(controller.add_car_to_driver("Jack", "MuscleCar"))
    print(controller.add_car_to_driver("John", "SportsCar"))
    print(controller.create_race("Christmas Top Racers"))
    print(controller.add_driver_to_race("Christmas Top Racers", "John"))
    print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
    print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
    print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
    print(controller.start_race("Christmas Top Racers"))
    [print(d.name, d.number_of_wins) for d in controller.drivers]


if __name__ == '__main__':
    # test1()
    test2()
