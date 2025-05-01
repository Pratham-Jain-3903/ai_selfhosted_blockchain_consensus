import unittest
from src.transaction import Transaction

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.sender = "Alice"
        self.recipient = "Bob"
        self.amount = 50
        self.transaction = Transaction(self.sender, self.recipient, self.amount)

    def test_transaction_creation(self):
        self.assertEqual(self.transaction.sender, self.sender)
        self.assertEqual(self.transaction.recipient, self.recipient)
        self.assertEqual(self.transaction.amount, self.amount)

    def test_transaction_validation(self):
        self.assertTrue(self.transaction.validate())

    def test_transaction_invalid_amount(self):
        invalid_transaction = Transaction(self.sender, self.recipient, -10)
        self.assertFalse(invalid_transaction.validate())

if __name__ == '__main__':
    unittest.main()