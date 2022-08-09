from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    DEFAULT_CAPACITY = 50

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_CAPACITY)
