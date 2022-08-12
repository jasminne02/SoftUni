from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []
        self.__supplies_before = self.supplies

    def add_player(self, *players: Player):
        added = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added.append(player.name)
        return f"Successfully added: {', '.join([str(n) for n in added])}"

    def add_supply(self, *supplies: Supply):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__get_player_by_name(player_name)
        if player is None:
            return
        if sustenance_type not in ['Food', 'Drink']:
            return
        sustenance = None
        if sustenance_type == 'Drink':
            sustenance = self.__get_last_drink_from_supplies()
            if sustenance is None:
                raise Exception("There are no drink supplies left!")
        elif sustenance_type == 'Food':
            sustenance = self.__get_last_food_from_supplies()
            if sustenance is None:
                raise Exception("There are no food supplies left!")

        if not player.need_sustenance:
            self.supplies = self.__supplies_before.copy()
            return f"{player_name} have enough stamina."

        if player.stamina + sustenance.energy > 100:
            player.stamina = 100
        else:
            player.stamina += sustenance.energy
        return f"{player_name} sustained successfully with {sustenance.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = self.__get_player_by_name(first_player_name)
        player2 = self.__get_player_by_name(second_player_name)
        if player1.stamina == 0 and player2.stamina == 0:
            return f"Player {player1.name} does not have enough stamina." \
                   f"Player {player2.name} does not have enough stamina."
        elif player1.stamina == 0:
            return f"Player {player1.name} does not have enough stamina."
        elif player2.stamina == 0:
            return f"Player {player2.name} does not have enough stamina."

        if player2.stamina < player1.stamina:
            player1, player2 = player2, player1

        # First player attacks
        self.__attack(player1, player2)
        if player2.stamina == 0:
            return f"Winner: {player1.name}"
        # Second player attacks
        self.__attack(player2, player1)
        if player1.stamina == 0:
            return f"Winner: {player2.name}"

        if player1.stamina > player2.stamina:
            return f"Winner: {player1.name}"
        return f"Winner: {player2.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - player.age * 2 < 0:
                player.stamina = 0
                continue
            player.stamina -= player.age * 2
        for player in self.players:
            self.__sustain(player, 'Food')
            self.__sustain(player, 'Drink')

    def __str__(self):
        output = ''
        for player in self.players:
            output += str(player) + '\n'
        for supply in self.supplies:
            output += supply.details() + '\n'
        return output.strip()

    #  PRIVATE METHODS  #
    def __get_player_by_name(self, name: str):
        for player in self.players:
            if player.name == name:
                return player

    def __get_last_drink_from_supplies(self):
        self.__supplies_before = self.supplies.copy()
        self.supplies.reverse()
        for supply in self.supplies:
            if supply.type() == 'Drink':
                self.supplies.remove(supply)
                self.supplies.reverse()
                return supply

    def __get_last_food_from_supplies(self):
        self.__supplies_before = self.supplies.copy()
        self.supplies.reverse()
        for supply in self.supplies:
            if supply.type() == 'Food':
                self.supplies.remove(supply)
                self.supplies.reverse()
                return supply

    @staticmethod
    def __attack(attacker, other_player):
        if other_player.stamina - attacker.stamina / 2 < 0:
            other_player.stamina = 0
        else:
            other_player.stamina -= attacker.stamina / 2

    def __sustain(self, player, sustenance_type):
        sustenance = None
        if sustenance_type == 'Drink':
            sustenance = self.__get_last_drink_from_supplies()
        elif sustenance_type == 'Food':
            sustenance = self.__get_last_food_from_supplies()
        if sustenance is None:
            return

        if not player.need_sustenance:
            self.supplies = self.__supplies_before.copy()

        if player.stamina + sustenance.energy > 100:
            player.stamina = 100
        else:
            player.stamina += sustenance.energy
