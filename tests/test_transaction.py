import unittest

from app.Transaction import Transaction


class TransactionTests(unittest.TestCase):

    def test_can_create_transaction(self):
        tx = Transaction(50)
        self.assertIsInstance(tx, Transaction)

    def test_cannot_create_a_zero_amount_transaction(self):
        with self.assertRaises(RuntimeError):
            Transaction(0)

# Optional:
# if __name__ == '__main__':
#     unittest.main()
