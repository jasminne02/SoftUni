from project.rooms.room import Room
from project.rooms.young_couple import YoungCouple


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        monthly_consumptions = 0
        for room in self.rooms:
            monthly_consumptions += room.expenses + room.room_cost
        return f"Monthly consumption: {monthly_consumptions}$."

    def pay(self):
        result_info = []
        for room in self.rooms:
            if self.__is_budget_enough(room):
                result_info.append(self.__enough_budget_to_pay(room))
            else:
                result_info.append(self.__not_enough_budget_to_pay(room))
        return "\n".join(result_info)

    def status(self):
        result = f"Total population: {self.__count_of_people_in_the_hotel()}"
        for room in self.rooms:
            result += f"\n{room.family_name} with {room.members_count} members. " \
                      f"Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$"
            for n in range(len(room.children)):
                result += f"\n--- Child {n+1} monthly cost: {(room.children[n].cost*30):.2f}$"
            appliance_cost = 0
            for appliance in room.appliances:
                appliance_cost += appliance.get_monthly_expense()
            result += f"\n--- Appliances monthly cost: {appliance_cost:.2f}$"
        return result

    #  PRIVATE METHODS  #
    @staticmethod
    def __is_budget_enough(room: Room):
        if room.budget - room.expenses - room.room_cost >= 0:
            return True
        return False

    @staticmethod
    def __enough_budget_to_pay(room: Room):
        expenses = room.expenses + room.room_cost
        room.budget -= expenses
        return f"{room.family_name} paid {expenses:.2f}$ and have {room.budget:.2f}$ left."

    def __not_enough_budget_to_pay(self, room: Room):
        self.rooms.remove(room)
        return f"{room.family_name} does not have enough budget and must leave the hotel."

    def __count_of_people_in_the_hotel(self):
        count = 0
        for room in self.rooms:
            count += room.members_count
        return count
