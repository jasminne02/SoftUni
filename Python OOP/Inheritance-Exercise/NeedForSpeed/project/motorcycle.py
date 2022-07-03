from project.vehicle import Vehicle


class Motorcycle(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int, fuel_consumption = 1.25):
        super().__init__(fuel, horse_power, fuel_consumption)
