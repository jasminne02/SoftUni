import math
from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        capacity_consumption = math.floor(capacity_consumption + capacity_consumption * 0.5)
        memory_consumption = math.floor(memory_consumption * 0.5)
        super().__init__(name, "Light", capacity_consumption, memory_consumption)
