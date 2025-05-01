import unittest
from src.blockchain import Blockchain
from src.block import Block
from src.transaction import Transaction

class TestBlockchain(unittest.TestCase):

    def setUp(self):
        self.blockchain = Blockchain()

    def test_create_genesis_block(self):
        self.assertEqual(len(self.blockchain.chain), 1)
        self.assertEqual(self.blockchain.chain[0].index, 0)

    def test_add_block(self):
        previous_block = self.blockchain.chain[-1]
        new_block = self.blockchain.add_block(previous_block)
        self.assertEqual(new_block.index, previous_block.index + 1)

    def test_validate_chain(self):
        self.blockchain.add_block(self.blockchain.chain[-1])
        self.assertTrue(self.blockchain.validate_chain())

    def test_invalid_chain(self):
        self.blockchain.chain[1].previous_hash = 'invalid_hash'
        self.assertFalse(self.blockchain.validate_chain())

    def test_add_transaction(self):
        transaction = Transaction("Alice", "Bob", 50)
        self.blockchain.add_transaction(transaction)
        self.assertEqual(len(self.blockchain.current_transactions), 1)

if __name__ == '__main__':
    unittest.main()