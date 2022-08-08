from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove


class OldCouple(Room):
    MEMBERS_COUNT = 2
    ROOM_COST = 15
    APPLIANCES = [TV(), Fridge(), Stove()] * 2

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, self.__calculate_budget(pension_one, pension_two), self.MEMBERS_COUNT)
        self.room_cost = self.ROOM_COST
        self.appliances = self.APPLIANCES
        self.calculate_expenses(self.appliances)

    @staticmethod
    def __calculate_budget(pension_one, pension_two):
        return pension_one + pension_two
