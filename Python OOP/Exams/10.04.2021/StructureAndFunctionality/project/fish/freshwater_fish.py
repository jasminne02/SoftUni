from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    DEFAULT_SIZE = 3
    DEFAULT_EAT_INCREASE = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.DEFAULT_SIZE, price)

    def aquarium_type(self):
        return 'FreshwaterAquarium'
