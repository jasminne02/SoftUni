from abc import ABC, abstractmethod


class Horse(ABC):
    MAX_SPEED = None
    TRAIN_SPEED_INCREASE = None

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value: int):
        if value > self.MAX_SPEED:
            raise ValueError(f"Horse speed is too high!")
        self.__speed = value

    def train(self):
        if self.speed + self.TRAIN_SPEED_INCREASE > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed += self.TRAIN_SPEED_INCREASE

    @abstractmethod
    def type(self):
        pass
