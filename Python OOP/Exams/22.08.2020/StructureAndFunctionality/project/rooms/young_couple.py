from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.laptop import Laptop


class YoungCouple(Room):
    MEMBERS_COUNT = 2
    ROOM_COST = 20
    APPLIANCES = [TV(), Fridge(), Laptop()] * 2

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, self.__calculate_budget(salary_one, salary_two), self.MEMBERS_COUNT)
        self.room_cost = self.ROOM_COST
        self.appliances = self.APPLIANCES
        self.calculate_expenses(self.appliances)

    @staticmethod
    def __calculate_budget(salary_one, salary_two):
        return salary_one + salary_two
