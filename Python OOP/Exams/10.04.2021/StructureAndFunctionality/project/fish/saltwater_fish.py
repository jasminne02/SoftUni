from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    DEFAULT_SIZE = 5
    DEFAULT_EAT_INCREASE = 2

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.DEFAULT_SIZE, price)

    def aquarium_type(self):
        return 'SaltwaterAquarium'
