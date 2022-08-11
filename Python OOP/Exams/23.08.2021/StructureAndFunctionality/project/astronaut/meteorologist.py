from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    INITIAL_OXYGEN_UNITS = 90
    NEEDED_OXYGEN_TO_BREATHE = 15

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN_UNITS)
