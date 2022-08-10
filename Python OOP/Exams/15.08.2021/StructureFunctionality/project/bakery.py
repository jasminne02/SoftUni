from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.table import Table
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value == ' ':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        food = self.__create_food(food_type, name, price)
        if food is None:
            return
        if food in self.food_menu:
            raise Exception(f"{food_type} {name} is already in the menu!")
        self.food_menu.append(food)
        return f"Added {food.name} ({food.type()}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand:str):
        drink = self.__create_drink(drink_type, name, portion, brand)
        if drink is None:
            return
        if drink in self.drinks_menu:
            raise Exception("{drink_type} {name} is already in the menu!")
        self.drinks_menu.append(drink)
        return f"Added {drink.name} ({drink.brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table = self.__create_table(table_type, table_number, capacity)
        if table is None:
            return
        if not self.__is_table_number_unique(table):
            raise Exception(f"Table {table_number} is already in the bakery!")
        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = self.__get_suitable_table(number_of_people)
        if table:
            table.reserve(number_of_people)
            return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self.__get_table_by_table_number(table_number)
        if not table:
            return f"Could not find table {table_number}"
        return self.__get_food_order_info(table, *food_names)

    def order_drink(self, table_number: int, *drink_names):
        table = self.__get_table_by_table_number(table_number)
        if not table:
            return f"Could not find table {table_number}"
        return self.__get_drink_order_info(table, *drink_names)

    def leave_table(self, table_number: int):
        table = self.__get_table_by_table_number(table_number)
        if table:
            bill = table.get_bill()
            table.clear()
            table.is_reserved = False
            self.total_income += bill
            return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        result_info = ''
        for table in self.tables_repository:
            result_info += table.free_table_info() + '\n'
        return result_info.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    # PRIVATE METHODS #
    @staticmethod
    def __create_food(food_type: str, name: str, price: float):
        if food_type == 'Bread':
            return Bread(name, price)
        elif food_type == 'Cake':
            return Cake(name, price)

    @staticmethod
    def __create_drink(drink_type: str, name: str, portion: float, brand:str):
        if drink_type == 'Water':
            return Water(name, portion, brand)
        elif drink_type == 'Tea':
            return Tea(name, portion, brand)

    @staticmethod
    def __create_table(table_type: str, table_number: int, capacity: int):
        if table_type == 'InsideTable':
            return InsideTable(table_number, capacity)
        elif table_type == 'OutsideTable':
            return OutsideTable(table_number, capacity)

    def __get_table_by_table_number(self, table_number: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    def __is_table_number_unique(self, table):
        for current_table in self.tables_repository:
            if table == current_table:
                continue
            if current_table.table_number == table.table_number:
                return False
        return True

    def __get_suitable_table(self, number_if_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_if_people:
                return table

    def __get_food_by_name(self, food_name: str):
        for food in self.food_menu:
            if food.name == food_name:
                return food

    def __get_drink_by_name(self, drink_name: str):
        for drink in self.drinks_menu:
            if drink.name == drink_name:
                return drink

    def __get_food_order_info(self, table: Table, *food_names):
        ordered_food = f'Table {table.table_number} ordered:'
        food_not_in_the_menu = f'{self.name} does not have in the menu:'
        for food_name in food_names:
            food = self.__get_food_by_name(food_name)
            if food:
                table.order_food(food)
                ordered_food += f'\n - {food_name}: {food.portion:.2f}g - {food.price:.2f}lv'
                continue
            food_not_in_the_menu += f'\n{food_name}'
        return ordered_food + "\n" + food_not_in_the_menu

    def __get_drink_order_info(self, table: Table, *drink_names):
        ordered_drinks = f'Table {table.table_number} ordered:'
        drinks_not_in_the_menu = f'{self.name} does not have in the menu:'
        for drink_name in drink_names:
            drink = self.__get_drink_by_name(drink_name)
            if drink:
                table.order_drink(drink)
                ordered_drinks += f'\n - {drink_name}: {drink.portion:.2f}ml - {drink.price:.2f}lv'
                continue
            drinks_not_in_the_menu += f'\n{drink_name}'
        return ordered_drinks + "\n" + drinks_not_in_the_menu
