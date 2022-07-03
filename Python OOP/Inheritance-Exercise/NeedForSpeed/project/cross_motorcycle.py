from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
