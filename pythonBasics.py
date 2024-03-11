class Account:
    def __init__(self, name, balance):
        self._name = name           # Intended as a private attribute
        self._balance = balance     # Intended as a private attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._updateLedger(amount)  # Private method call

    def _updateLedger(self, amount):     # Private method
        print(f"{amount} deposited to the ledger.")

# External access
account = Account("John Doe", 1000)
account.deposit(500)
# account.__updateLedger(500)  # This would raise an AttributeError
