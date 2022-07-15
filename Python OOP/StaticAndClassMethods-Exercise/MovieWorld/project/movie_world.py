from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name= name
        self.customers = []
        self.dvd = []

    @classmethod
    def dvd_capacity(cls):
        return cls.DVD_CAPACITY

    @classmethod
    def customer_capacity(cls):
        return cls.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvd) < MovieWorld.DVD_CAPACITY:
            self.dvd.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        current_dvd = None
        current_customer = None

        for dvd in self.dvd:
            if dvd.id == dvd_id:
                current_dvd = dvd
                break

        for customer in self.customers:
            if customer.id == customer_id:
                current_customer = customer
                break

        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"
        if current_dvd.is_rented:
            return f"DVD is already rented"
        if current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"

        current_customer.rented_dvds.append(current_dvd)
        current_dvd.is_rented = True
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        current_customer = None
        current_dvd = None

        for dvd in self.dvd:
            if dvd.id == dvd_id:
                current_dvd = dvd
                break

        for customer in self.customers:
            if customer.id == customer_id:
                current_customer = customer
                break

        if current_dvd in current_customer.rented_dvds:
            current_customer.rented_dvds.remove(current_dvd)
            current_dvd.is_rented = False
            return f"{current_customer.name} has successfully returned {current_dvd.name}"

        return f"{current_customer.name} does not have that DVD"

    def __repr__(self):
        result = ""

        for customer in self.customers:
            result += customer.__repr__() + '\n'

        for dvd in self.dvd:
            result += dvd.__repr__() + '\n'

        return result
