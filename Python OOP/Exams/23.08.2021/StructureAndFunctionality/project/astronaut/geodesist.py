from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    INITIAL_OXYGEN_UNITS = 50

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN_UNITS)
