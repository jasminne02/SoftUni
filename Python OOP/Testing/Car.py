class Car:
    def __init__(self, make, model, fuel_consumption, fuel_amount, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_amount = fuel_amount
        self.fuel_capacity = fuel_capacity

    def add_fuel(self, amount):
        if amount < 0:
            raise Exception
        if self.fuel_amount + amount > self.fuel_capacity:
            raise Exception

        self.fuel_amount += amount

    def drive(self, distance):
        if distance < 0:
            raise Exception
        if self.fuel_consumption * distance > self.fuel_amount:
            raise Exception

        self.fuel_amount -= self.fuel_consumption * distance
