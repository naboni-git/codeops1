# Parent class
class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number

        # One underscore allows child classes to use the balance.
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount

    def statement(self):
        print(
            f"Account: {self.account_number} | "
            f"Owner: {self.owner} | "
            f"Balance: {self.balance} ETB"
        )


# SavingsAccount inherits from Account
class SavingsAccount(Account):
    def __init__(self, owner, number, balance=0, rate=0.05):
        super().__init__(owner, number, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)

    def statement(self):
        print("--- Savings Account ---")
        super().statement()


# CurrentAccount inherits from Account
class CurrentAccount(Account):
    def __init__(self, owner, number, balance=0, overdraft=1000):
        super().__init__(owner, number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance + self.overdraft:
            raise ValueError("Overdraft limit exceeded")

        self._balance -= amount

    def statement(self):
        print("--- Current Account ---")
        super().statement()


# Create three account types
regular_account = Account("Naboni", "A001", 500)
savings_account = SavingsAccount("Almaz", "A002", 1000, 0.05)
current_account = CurrentAccount("Dawit", "A003", 200, 500)


# Test savings interest
savings_account.add_interest()

# Test current-account overdraft
current_account.withdraw(600)


# One loop for all account types
accounts = [
    regular_account,
    savings_account,
    current_account
]

for account in accounts:
    account.statement()
    print()
