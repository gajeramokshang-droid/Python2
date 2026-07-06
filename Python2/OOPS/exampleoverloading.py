# Create a class Account with attribute balance.
# Overload the += operator to add money to the account.

class Account:
    def __init__(self, balance):
        self.balance = balance

    def __iadd__(self, amount):
        self.balance += amount
        return self

    def __str__(self):
        return str(self.balance)


p1 = Account(20000)
print(p1)

p1 += 30000
print(p1)
