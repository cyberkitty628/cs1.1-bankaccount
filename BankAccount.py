import random 

class BankAccount:

    def __init__(self, full_name):
        self.full_name = full_name
        self.account_number = random.randint(00000000, 99999999)
        self.routing_number = 987654321
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f'Amount Deposited: ${float(amount)}')

    def withdraw(self, amount):
        self.balance -= amount
        print(f'Amount Withdrawn: ${float(amount)}')

    def get_balance(self):
        print(f'Your account balance is {self.balance}.')
        return self.balance

account_1 = BankAccount('Kristina Kamphuis')

account_1.deposit(800)

account_1.withdraw(600)

# print(account_1.balance)

account_1.get_balance()