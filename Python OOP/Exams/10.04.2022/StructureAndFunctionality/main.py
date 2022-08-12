from project.player import Player
from project.controller import Controller
from project.supply.drink import Drink
from project.supply.food import Food


def test1():
    controller = Controller()
    player1 = Player('John', 16, 78)
    player2 = Player('Ivan', 21, 30)
    player3 = Player('Kris', 19, 90)
    print(controller.add_player(player1, player2))
    print(controller.add_player(player1, player2, player3))
    food1 = Food('Cheese')
    food2 = Food('Bread')
    drink1 = Drink('Water')
    drink2 = Drink('Tea')
    controller.add_supply(food1, food2, drink1, drink2, food2, drink1, drink2)
    controller.next_day()
    print(controller.sustain('Kris', 'Drink'))


def test2():
    controller = Controller()
    apple = Food("apple", 22)
    cheese = Food("cheese")
    juice = Drink("orange juice")
    water = Drink("water")
    first_player = Player('Peter', 15)
    second_player = Player('Lilly', 12, 94)
    print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
    print(controller.add_player(first_player, second_player))
    print(controller.duel("Peter", "Lilly"))
    print(controller.add_player(first_player))
    print(controller.sustain("Lilly", "Drink"))
    first_player.stamina = 0
    print(controller.duel("Peter", "Lilly"))
    print(first_player)
    print(second_player)
    controller.next_day()
    print(controller)


if __name__ == '__main__':
    test1()
    # test2()
