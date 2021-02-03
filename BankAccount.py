class BankAccount:

    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

account_1 = BankAccount('Kristina Kamphuis', 123456789, 987654321, 1500)

print(account_1.routing_number)