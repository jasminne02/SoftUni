import math
from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        capacity = math.floor(capacity*0.25)
        memory = math.floor(memory + memory*0.75)
        super().__init__(name, "Power", capacity, memory)
