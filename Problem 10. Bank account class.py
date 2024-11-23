class BankAccount:
    def __init__(self, starting_balance):
        self.__balance = starting_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        elif amount > 0:
            self.__balance -= amount
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance

# Sample usage
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())
account.withdraw(300)
print(account.get_balance())
account.withdraw(1500)
