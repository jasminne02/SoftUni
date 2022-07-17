from project.food import Food
from project.food import Meat
from project.food import Seed
from project.food import Vegetable
from project.food import Fruit
from project.animals.animal import Animal
from project.animals.animal import Bird
from project.animals.animal import Mammal
from project.animals.birds import Hen
from project.animals.birds import Owl
from project.animals.mammals import Mouse
from project.animals.mammals import Cat
from project.animals.mammals import Dog
from project.animals.mammals import Tiger


owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)

print("\n")

hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)
