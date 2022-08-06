import math
from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        capacity *= 2
        memory = math.floor(memory*0.75)
        super().__init__(name, "Heavy", capacity, memory)
