from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.decoration.plant import Plant
from project.decoration.ornament import Ornament
from project.controller import Controller


controller = Controller()

fish1 = FreshwaterFish("John", "species", 12.01)

controller.add_aquarium('FreshwaterAquarium', 'FreshwaterAquarium')
controller.add_aquarium('SaltwaterAquarium', 'SaltwaterAquarium')
controller.add_aquarium('SaltwaterAquarium', 'SaltwaterAquarium')
controller.add_decoration('Plant')
controller.add_decoration('Ornament')
controller.add_decoration('Ornament')
controller.add_decoration('Plant')
controller.add_decoration('Plant')
print(controller.add_fish("FreshwaterAquarium", "FreshwaterFish", "Mike", "species", 23.4))

