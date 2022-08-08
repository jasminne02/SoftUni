from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.laptop import Laptop


class YoungCoupleWithChildren(Room):
    MEMBERS_COUNT = 2
    ROOM_COST = 30
    APPLIANCES = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, self.__calculate_budget(salary_one, salary_two), self.MEMBERS_COUNT)
        self.room_cost = self.ROOM_COST
        self.__add_children(*children)
        self.appliances = self.APPLIANCES * self.members_count
        self.calculate_expenses(self.appliances, self.children)

    def __add_children(self, *children):
        for child in children:
            self.children.append(child)
            self.members_count += 1

    @staticmethod
    def __calculate_budget(salary_one, salary_two):
        return salary_one + salary_two
