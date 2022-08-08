from project.rooms.room import Room
from project.appliances.tv import TV


class AloneYoung(Room):
    MEMBERS_COUNT = 1
    ROOM_COST = 10
    APPLIANCES = [TV()]

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, self.MEMBERS_COUNT)
        self.room_cost = self.ROOM_COST
        self.appliances = self.APPLIANCES
        self.calculate_expenses(self.appliances)
