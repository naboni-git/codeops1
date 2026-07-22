# =====================================================================
# ACCOUNT CLASS (Simplified & Self-Contained)
# =====================================================================
class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        self.history_stack = []  # LIFO Stack to track deposits/withdrawals

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        # Record transaction to history stack
        self.history_stack.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        # Record transaction to history stack
        self.history_stack.append(("withdraw", amount))


# =====================================================================
# THE ACCOUNT REGISTRY
# =====================================================================
class AccountRegistry:
    def __init__(self):
        # 1. Store accounts in a dictionary keyed by account number for O(1) find
        self.by_number = {}
        # 2. Store account numbers in a list to remember the order they were added
        self.order = []

    def add(self, acc):
        # O(1) insertion to hash table
        self.by_number[acc.account_number] = acc
        # Track insertion order
        self.order.append(acc.account_number)

    def find(self, number):
        # O(1) instant dictionary lookup
        return self.by_number.get(number)

    def list_all(self):
        # Returns all accounts sorted by their insertion order
        return [self.by_number[number] for number in self.order]

    def undo_last(self, number):
        account = self.find(number)
        if account is None:
            print("Account not found.")
            return

        # Check if the account has any transaction history in its stack
        if len(account.history_stack) == 0:
            print(f"No transactions to undo for account {number}.")
            return

        # Pop the latest transaction (Last In, First Out)
        action, amount = account.history_stack.pop()

        if action == "deposit":
            # Reversing a deposit means subtracting the money
            account.balance -= amount
            print(f"[UNDO] Reversed deposit of {amount} ETB. New Balance: {account.balance} ETB")
        elif action == "withdraw":
            # Reversing a withdrawal means adding the money back
            account.balance += amount
            print(f"[UNDO] Reversed withdrawal of {amount} ETB. New Balance: {account.balance} ETB")


# =====================================================================
# REGISTRY TEST DRIVE
# =====================================================================
if __name__ == "__main__":
    print("=== Creating Account Registry ===")
    registry = AccountRegistry()

    # Create and add accounts
    acc1 = Account("Naboni", "SAV-101", 1000)
    acc2 = Account("Almaz", "SAV-102", 500)
    acc3 = Account("Dawit", "SAV-103", 250)

    registry.add(acc1)
    registry.add(acc2)
    registry.add(acc3)

    print("\n=== Testing O(1) Find ===")
    found = registry.find("SAV-101")
    if found:
        print(f"Found Account: {found.owner} | Balance: {found.balance} ETB")

    print("\n=== Testing Insertion Order Listing ===")
    for account in registry.list_all():
        print(f"- {account.account_number}: {account.owner}")

    print("\n=== Performing Transactions ===")
    acc1.deposit(500)   # Balance becomes 1500
    acc1.withdraw(200)  # Balance becomes 1300
    print(f"Current Balance for {acc1.owner}: {acc1.balance} ETB")

    print("\n=== Performing Undo Transactions (LIFO Stack) ===")
    # First undo: Should reverse the withdrawal of 200 ETB
    registry.undo_last("SAV-101")  # Should bring balance back to 1500 ETB

    # Second undo: Should reverse the deposit of 500 ETB
    registry.undo_last("SAV-101")  # Should bring balance back to 1000 ETB