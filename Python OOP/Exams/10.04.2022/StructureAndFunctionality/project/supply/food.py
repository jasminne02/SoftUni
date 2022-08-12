from project.supply.supply import Supply


class Food(Supply):
    DEFAULT_ENERGY = 25

    def __init__(self, name: str, energy=DEFAULT_ENERGY):
        super().__init__(name, energy)
