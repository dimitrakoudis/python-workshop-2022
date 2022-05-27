class Transaction:

    def __init__(self, amount, notes=None):
        if amount == 0:
            raise RuntimeError("Cannot create zero amount transaction")
        self.amount = amount
        self.notes = notes
