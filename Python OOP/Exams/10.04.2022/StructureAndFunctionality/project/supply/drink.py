from project.supply.supply import Supply


class Drink(Supply):
    DEFAULT_ENERGY = 15

    def __init__(self, name: str, energy=DEFAULT_ENERGY):
        super().__init__(name, energy)
