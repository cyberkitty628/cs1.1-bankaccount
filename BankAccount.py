import random 

class BankAccount:

    def __init__(self, full_name):
        self.full_name = full_name
        self.account_number = random.randint(00000000, 99999999)
        self.routing_number = 987654321
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

account_1 = BankAccount('Kristina Kamphuis')

account_1.deposit(1000)

print(account_1.balance)