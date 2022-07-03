from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel: float, horse_power: int, fuel_consumption = 3):
        super().__init__(fuel, horse_power, fuel_consumption)
