class BankAccount:

    def __init__(self, owner, credit_limit):
        if not 0 <= credit_limit <= 500:
            raise RuntimeError("Forbidden credit limit")
        self.owner = owner
        self.credit_limit = credit_limit
