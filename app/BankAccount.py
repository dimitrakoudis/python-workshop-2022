class BankAccount:

    def __init__(self, owner, credit_limit):
        if not 0 <= credit_limit <= 500:
            raise RuntimeError("Forbidden credit limit")
        self.owner = owner
        self.credit_limit = credit_limit
        self.transactions = []

    def get_balance(self):
        return sum([transaction.amount for transaction in self.transactions])

    def add_transaction(self, transaction):
        if transaction.amount < 0 and self.credit_limit < abs(
                self.get_balance() + transaction.amount
        ):
            raise RuntimeError("Insufficient amount")
        self.transactions.append(transaction)
