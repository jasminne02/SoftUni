from project.animal import Animal
from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.worker import Worker
from project.keeper import Keeper
from project.caretaker import Caretaker
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: float):
        if price <= self.__budget and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif price > self.__budget and self.__animal_capacity-1 >= 0:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary

        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_for_animals = 0
        for animal in self.animals:
            total_money_for_animals += animal.money_for_care

        if total_money_for_animals <= self.__budget:
            self.__budget -= total_money_for_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: float):
        self.__budget += amount

    def animals_status(self):
        info = f"You have {len(self.animals)} animals\n"
        total_lions = 0
        total_tigers = 0
        total_cheetah = 0
        lions = []
        tigers = []
        cheetahs = []

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                total_lions += 1
                lions.append(animal)
            elif animal.__class__.__name__ == "Tiger":
                total_tigers += 1
                tigers.append(animal)
            elif animal.__class__.__name__ == "Cheetah":
                total_cheetah += 1
                cheetahs.append(animal)

        info += f"----- {total_lions} Lions:\n"
        for lion in lions:
            info += lion.__repr__() + "\n"
        info += f"----- {total_tigers} Tigers:\n"
        for tiger in tigers:
            info += tiger.__repr__() + "\n"
        info += f"----- {total_cheetah} Cheetahs:\n"
        for cheetah in cheetahs:
            info += cheetah.__repr__() + "\n"

        return info

    def workers_status(self):
        info = f"You have {len(self.workers)} workers\n"
        total_keepers = 0
        total_vets = 0
        total_caretakers = 0
        vets = []
        caretakers = []
        keepers = []

        for worker in self.workers:
            if worker.__class__.__name__ == "Vet":
                total_vets += 1
                vets.append(worker)
            elif worker.__class__.__name__ == "Keeper":
                total_keepers += 1
                keepers.append(worker)
            elif worker.__class__.__name__ == "Caretaker":
                total_caretakers += 1
                caretakers.append(worker)

        info += f"----- {total_keepers} Keepers:\n"
        for keeper in keepers:
            info += keeper.__repr__() + "\n"
        info += f"----- {total_caretakers} Caretakers:\n"
        for caretaker in caretakers:
            info += caretaker.__repr__() + "\n"
        info += f"----- {total_vets} Vets:\n"
        for vet in vets:
            info += vet.__repr__() + "\n"

        return info
