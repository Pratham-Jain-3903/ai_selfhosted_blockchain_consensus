import unittest
from src.block import Block
import time

class TestBlock(unittest.TestCase):

    def setUp(self):
        self.index = 1
        self.previous_hash = '0' * 64
        self.timestamp = time.time()
        self.transactions = []
        self.block = Block(self.index, self.previous_hash, self.timestamp, self.transactions)

    def test_block_creation(self):
        self.assertEqual(self.block.index, self.index)
        self.assertEqual(self.block.previous_hash, self.previous_hash)
        self.assertAlmostEqual(self.block.timestamp, self.timestamp, delta=1)
        self.assertEqual(self.block.transactions, self.transactions)

    def test_block_hash(self):
        self.assertIsNotNone(self.block.hash)
        self.assertEqual(len(self.block.hash), 64)

    def test_block_hash_consistency(self):
        initial_hash = self.block.hash
        self.block.transactions.append({'sender': 'Alice', 'recipient': 'Bob', 'amount': 10})
        self.block.hash = self.block.calculate_hash()
        self.assertNotEqual(initial_hash, self.block.hash)

if __name__ == '__main__':
    unittest.main()