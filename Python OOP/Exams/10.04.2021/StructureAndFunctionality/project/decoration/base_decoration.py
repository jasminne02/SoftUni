from abc import ABC


class BaseDecoration(ABC):
    def __init__(self, comfort: int, price: float):
        self.comfort = comfort
        self.price = price

    def type(self):
        return self.__class__.__name__
