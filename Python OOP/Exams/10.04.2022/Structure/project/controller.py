from project.player import Player
from project.supply.supply import Supply
from project.supply.food import Food
from project.supply.drink import Drink


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players: Player):
        added = []

        for player in players:
            if player not in self.players:
                self.players.append(player)
                added.append(player.name)

        return f"Successfully added: {', '.join([str(x) for x in added])}"

    def add_supply(self, *supplies: Supply):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = None
        sustenance = None

        for p in self.players:
            if p.name == player_name:
                player = p
                break

        if sustenance_type == "Food" or sustenance_type == "Drink":
            for idx in range(len(self.supplies)-1, -1, -1):
                s = self.supplies[idx]
                if s.__class__.__name__ == sustenance_type:
                    sustenance = s
                    break

        if sustenance_type == "Drink" and sustenance is None:
            raise Exception("There are no drink supplies left!")
        if sustenance_type == "Food" and sustenance is None:
            raise Exception("There are no food supplies left!")

        if player and sustenance:
            if not player.need_sustenance:
                return f"{player_name} have enough stamina."

            self.supplies.remove(sustenance)
            player.stamina += sustenance.energy
            if player.stamina > 100:
                player.stamina = 100
            return f"{player_name} sustained successfully with {sustenance.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = None
        second_player = None

        for player in self.players:
            if player.name == first_player_name:
                first_player = player
            elif player.name == second_player_name:
                second_player = player
            if first_player and second_player:
                break

        if first_player.stamina == 0 and second_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina.\n" \
                   f"Player {second_player_name} does not have enough stamina."
        elif first_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        elif second_player.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        if first_player.stamina > second_player.stamina:
            first_player, second_player = second_player, first_player

        first_player_attack = first_player.stamina / 2

        second_player.stamina -= first_player_attack
        if second_player.stamina <= 0:
            second_player.stamina = 0
            return f"Winner: {first_player.name}"

        second_player_attack = second_player.stamina / 2
        first_player.stamina -= second_player_attack
        if first_player.stamina <= 0:
            first_player.stamina = 0
            return f"Winner: {second_player.name}"

        if first_player.stamina > second_player.stamina:
            return f"Winner: {first_player.name}"
        elif first_player.stamina < second_player.stamina:
            return f"Winner: {second_player.name}"

    def next_day(self):
        food = []
        drinks = []

        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)

        for supply in self.supplies:
            if isinstance(supply, Food):
                food.append(supply)
            elif isinstance(supply, Drink):
                drinks.append(supply)

        for player in self.players:
            f = food.pop()
            self.supplies.remove(f)
            d = drinks.pop()
            self.supplies.remove(d)
            player.stamina = min(player.stamina+f.energy, 100)
            player.stamina = min(player.stamina+d.energy, 100)

    def __str__(self):
        result = ""
        for player in self.players:
            result += "Player: " + str(player) + "\n"
        for supply in self.supplies:
            result += supply.details() + "\n"
        return result
