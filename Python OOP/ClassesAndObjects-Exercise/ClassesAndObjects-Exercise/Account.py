class Account:
    def __init__(self, id: float, name: str, *balance):
        self.id = id
        self.name = name
        if balance:
            self.balance = int(balance[0])
        else:
            self.balance = 0

    def credit(self, amount: float):
        self.balance += amount
        return self.balance

    def debit(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())
print()

account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())
