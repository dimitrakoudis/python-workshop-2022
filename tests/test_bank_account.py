import unittest

from app.BankAccount import BankAccount
from app.Transaction import Transaction


class BankAccountTests(unittest.TestCase):

    def test_can_create_bank_account(self):
        ba = BankAccount(owner="John Doe", credit_limit=250)
        self.assertIsInstance(ba, BankAccount)

    def test_can_deposit_on_bank_account(self):
        ba = BankAccount(owner="John Doe", credit_limit=100)
        tx = Transaction(200)
        ba.add_transaction(tx)

        self.assertEqual(ba.get_balance(), 200)

    def test_can_withdraw_from_bank_account(self):
        ba = BankAccount(owner="John Doe", credit_limit=100)
        tx = Transaction(-100)
        ba.add_transaction(tx)

        self.assertEqual(ba.get_balance(), -100)

    def test_cannot_create_bank_account_with_negative_credit_limit(self):
        with self.assertRaises(RuntimeError):
            BankAccount(owner="John Doe", credit_limit=-50)

    def test_cannot_create_bank_account_with_credit_limit_over_500(self):
        with self.assertRaises(RuntimeError):
            BankAccount(owner="John Doe", credit_limit=501)

    def test_cannot_withdraw_from_bank_account_exceeding_credit_limit(self):
        ba = BankAccount(owner="John Doe", credit_limit=100)
        tx = Transaction(-200)

        with self.assertRaises(RuntimeError):
            ba.add_transaction(tx)

# Optional:
# if __name__ == '__main__':
#     unittest.main()
