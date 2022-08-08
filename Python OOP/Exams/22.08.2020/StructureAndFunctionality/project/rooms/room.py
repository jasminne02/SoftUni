from project.appliances.appliance import Appliance
from project.people.child import Child


class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []  # contains all kids in the room
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        total_expenses = 0
        for list_element in args:
            for element in list_element:
                if isinstance(element, Child):
                    total_expenses += element.cost * 30
                elif isinstance(element, Appliance):
                    total_expenses += element.get_monthly_expense()
        self.__expenses = total_expenses
