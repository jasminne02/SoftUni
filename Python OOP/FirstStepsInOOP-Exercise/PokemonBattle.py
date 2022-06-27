class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon_name == pokemon.name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        data = f"Pokemon Trainer {self.name}\n"
        data += f"Pokemon count {len(self.pokemons)}\n"
        for pokemon in self.pokemons:
            data += f"- {pokemon.name} with health {pokemon.health}\n"
        return data


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
