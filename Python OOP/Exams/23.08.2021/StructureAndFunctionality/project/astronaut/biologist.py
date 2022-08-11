from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    INITIAL_OXYGEN_UNITS = 70
    NEEDED_OXYGEN_TO_BREATHE = 5

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN_UNITS)
