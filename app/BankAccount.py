class BankAccount:

    def __init__(self, owner, credit_limit):
        if credit_limit < 0:
            raise RuntimeError("Forbidden credit limit")
        self.owner = owner
        self.credit_limit = credit_limit
