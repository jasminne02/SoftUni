class Customer:
    PERSONAL_ID = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.PERSONAL_ID
        Customer.PERSONAL_ID += 1

    @classmethod
    def get_next_id(cls):
        return cls.PERSONAL_ID

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
