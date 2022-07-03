from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel: float, horse_power: int, fuel_consumption = 8):
        super().__init__(fuel, horse_power, fuel_consumption)
