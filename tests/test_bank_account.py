import unittest

from app.BankAccount import BankAccount


class BankAccountTests(unittest.TestCase):

    def test_can_create_bank_account(self):
        ba = BankAccount(owner="John Doe", credit_limit=5000)
        self.assertIsInstance(ba, BankAccount)

    def test_cannot_create_bank_account_with_negative_credit_limit(self):
        with self.assertRaises(RuntimeError):
            BankAccount(owner="John Doe", credit_limit=-50)

# Optional:
# if __name__ == '__main__':
#     unittest.main()
