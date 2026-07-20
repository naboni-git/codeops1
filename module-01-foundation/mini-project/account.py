class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self.__balance = balance

    # Read-only getter for the private balance
    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient funds")

        self.__balance -= amount

    def statement(self):
        print(f"Owner: {self.owner}")
        print(f"Account number: {self.account_number}")
        print(f"Balance: {self.__balance} ETB")


# Test the Account class

account = Account("Naboni", "1001", 500)

account.statement()

account.deposit(200)
print("\nAfter depositing 200 ETB:")
account.statement()

account.withdraw(100)
print("\nAfter withdrawing 100 ETB:")
account.statement()

# Test an invalid withdrawal
try:
    account.withdraw(1000)
except ValueError as error:
    print(f"\nError: {error}")
