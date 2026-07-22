from abc import ABC, abstractmethod

# =====================================================================
# 1. BANK CONFIGURATION (SINGLETON)
# =====================================================================
class BankConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000
        return cls._instance


# =====================================================================
# 2. OBSERVER INTERFACE & CONCRETE OBSERVERS (SRP alert logic)
# =====================================================================
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class SMSAlert(Observer):
    def update(self, message):
        print(f"[SMS ALERT] {message}")

class AuditLog(Observer):
    def update(self, message):
        print(f"[AUDIT LOG] Recorded Transaction: {message}")


# =====================================================================
# 3. ACCOUNT BASE CLASS (With Observer Registry)
# =====================================================================
class Account(ABC):
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self._balance = balance
        self._observers = []  # List of registered observers

    def subscribe(self, observer):
        self._observers.append(observer)

    def _notify(self, message):
        for observer in self._observers:
            observer.update(message)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount
        self._notify(f"Account {self.account_number} deposited {amount} ETB. Balance: {self._balance} ETB.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._notify(f"Account {self.account_number} withdrew {amount} ETB. Balance: {self._balance} ETB.")

    def statement(self):
        print(f"Owner: {self.owner} | Account: {self.account_number} | Balance: {self._balance} ETB")


# =====================================================================
# 4. CONCRETE ACCOUNT TYPES
# =====================================================================
class SavingsAccount(Account):
    def __init__(self, owner, number, balance=0):
        super().__init__(owner, number, balance)
        # Read interest rate from our Singleton configuration
        self.rate = BankConfig().interest_rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)

    def statement(self):
        print("--- Savings Account ---")
        super().statement()


class CurrentAccount(Account):
    def __init__(self, owner, number, balance=0):
        super().__init__(owner, number, balance)
        # Read overdraft limit from our Singleton configuration
        self.overdraft_limit = BankConfig().overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self._balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")
        self._balance -= amount
        self._notify(f"Account {self.account_number} withdrew {amount} ETB (Overdraft utilized). Balance: {self._balance} ETB.")

    def statement(self):
        print("--- Current Account ---")
        super().statement()


# =====================================================================
# 5. ACCOUNT FACTORY
# =====================================================================
class AccountFactory:
    @staticmethod
    def create(kind, owner, number, balance=0):
        if kind == "savings":
            return SavingsAccount(owner, number, balance)
        elif kind == "current":
            return CurrentAccount(owner, number, balance)
        else:
            raise ValueError(f"Unknown account type: {kind}")


# =====================================================================
# TESTING OUR REFACTORED BANK
# =====================================================================
if __name__ == "__main__":
    print("=== Creating Accounts via Factory ===")
    acc1 = AccountFactory.create("savings", "Naboni", "SAV-110", 1000)
    acc2 = AccountFactory.create("current", "Dawit", "CUR-220", 200)

    print("\n=== Subscribing Observers ===")
    sms = SMSAlert()
    audit = AuditLog()

    acc1.subscribe(sms)
    acc1.subscribe(audit)  # acc1 has two observers

    acc2.subscribe(sms)    # acc2 has one observer

    print("\n=== Testing Transactions ===")
    acc1.deposit(500)
    print()
    acc2.withdraw(600)  # Uses overdraft limit