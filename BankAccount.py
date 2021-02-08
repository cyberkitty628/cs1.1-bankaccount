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
        overdraft_fee = 10
        self.balance -= amount
        if self.balance < 0:
            self.balance -= overdraft_fee
            print("Insufficient funds.")
        else:
            print(f'Amount Withdrawn: ${float(amount)}')

    def get_balance(self):
        print(f'Your account balance is {self.balance}.')
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        print(self.balance + interest)

    def print_receipt(self):
        print(f'''
        {self.full_name} 
        Account No.: {self.account_number} 
        Routing No.: {self.routing_number} 
        Balance: ${float(self.balance)}''')

account_1 = BankAccount('Kristina Kamphuis')

# Example 1: Depositing and withdrawing to test overdraft fee
account_1.deposit(800)

account_1.withdraw(850)

print(account_1.balance)

# Example 2: Making another deposit and withdraw to make sure withdraw print statement is working
account_1.deposit(900)

account_1.withdraw(60)

# Example 3: Testing out balance + interest statements
account_1.get_balance()

account_1.add_interest()

# Example 4: Testing out print_receipt method
account_1.print_receipt()