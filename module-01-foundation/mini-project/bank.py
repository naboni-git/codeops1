# =========================================================
# SINGLETON: Bank Configuration
# =========================================================
class BankConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000
        return cls._instance


# =========================================================
# OBSERVERS: Decoupled notification classes (SRP)
# =========================================================
class BankObserver:
    def update(self, account, action, amount):
        raise NotImplementedError


class SMSAlert(BankObserver):
    def update(self, account, action, amount):
        print(f"[SMS Alert] To {account.owner}: A {action} of {amount} ETB was processed on Account {account.number}. New Balance: {account.balance} ETB.")


class AuditLog(BankObserver):
    def update(self, account, action, amount):
        print(f"[Audit Log] ACTION: {action.upper()} | Account: {account.number} | Owner: {account.owner} | Amount: {amount} ETB | Final Balance: {account.balance} ETB.")


# =========================================================
# SUBJECT: Base Bank Account
# =========================================================
class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self.balance = balance
        self._observers = []

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def _notify(self, action, amount):
        for observer in self._observers:
            observer.update(self, action, amount)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._notify("deposit", amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # To be implemented by subclasses
        raise NotImplementedError


# =========================================================
# CONCRETE ACCOUNTS: Savings & Current Subclasses
# =========================================================
class SavingsAccount(Account):
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self._notify("withdrawal", amount)
        else:
            print(f"[Error] Overdraft blocked. Savings accounts cannot go below 0 ETB.")

    def apply_interest(self):
        config = BankConfig()
        interest = self.balance * config.interest_rate
        self.balance += interest
        self._notify("interest calculation", interest)


class CurrentAccount(Account):
    def withdraw(self, amount):
        config = BankConfig()
        # Allows balance to drop negative up to the overdraft limit
        max_allowed_withdrawal = self.balance + config.overdraft_limit
        if 0 < amount <= max_allowed_withdrawal:
            self.balance -= amount
            self._notify("withdrawal", amount)
        else:
            print(f"[Error] Overdraft limit of {config.overdraft_limit} ETB exceeded!")


# =========================================================
# FACTORY: Account Creation Pattern
# =========================================================
class AccountFactory:
    @staticmethod
    def create(kind, owner, number, balance=0):
        kind = kind.lower()
        if kind == "savings":
            return SavingsAccount(owner, number, balance)
        elif kind == "current":
            return CurrentAccount(owner, number, balance)
        else:
            raise ValueError(f"Unknown account type: '{kind}'")


# =========================================================
# RUNNING & TESTING DEMO
# =========================================================
if __name__ == "__main__":
    print("=== Creating Observers ===")
    sms = SMSAlert()
    audit = AuditLog()

    print("\n=== Creating Accounts via AccountFactory ===")
    # Creating a Savings and Current Account
    savings_acc = AccountFactory.create("savings", "Almaz", "SAV-101", 2000)
    current_acc = AccountFactory.create("current", "Dawit", "CUR-202", 500)

    # Subscribing Observers to both accounts
    savings_acc.subscribe(sms)
    savings_acc.subscribe(audit)

    current_acc.subscribe(sms)
    current_acc.subscribe(audit)

    print("\n=== Simulating Transactions ===")
    
    # 1. Deposit into Savings
    print("\n--- 1. Almaz Deposits 500 ETB ---")
    savings_acc.deposit(500)

    # 2. Withdraw from Savings
    print("\n--- 2. Almaz Withdraws 1000 ETB ---")
    savings_acc.withdraw(1000)

    # 3. Apply Interest to Savings (using Singleton interest rate of 0.05)
    print("\n--- 3. Bank Applies Interest to Almaz ---")
    savings_acc.apply_interest()

    # 4. Withdraw beyond balance on Current Account (within limit)
    print("\n--- 4. Dawit Withdraws 1200 ETB (Using Overdraft) ---")
    current_acc.withdraw(1200)

    # 5. Overdraft Limit Violation
    print("\n--- 5. Dawit Attempts to Withdraw 1000 ETB More (Will fail) ---")
    current_acc.withdraw(1000)