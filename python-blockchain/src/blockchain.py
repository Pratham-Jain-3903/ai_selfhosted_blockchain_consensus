import hashlib
import time
import json
from .block import Block
from .transaction import Transaction, TransactionType
from .ml_model import IrisModel
from .consensus.proof_of_work import ProofOfWork

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        self.pow = ProofOfWork(difficulty=4)
        self.ml_model = IrisModel()
        
        # Create the genesis block
        self.create_genesis_block()
        
    def create_genesis_block(self):
        """Create the first block in the chain with no previous hash"""
        genesis_block = Block(0, "0", time.time(), [], 0)
        genesis_block.hash = self.pow.mine(genesis_block)
        self.chain.append(genesis_block)
        return genesis_block
        
    def add_block(self, previous_block):
        """Mine a new block and add it to the chain"""
        block = Block(
            index=previous_block.index + 1,
            previous_hash=previous_block.hash,
            timestamp=time.time(),
            transactions=self.current_transactions,
            nonce=0
        )
        
        # Find the proof of work for this block
        block.hash = self.pow.mine(block)
        
        # Process any ML transactions in this block
        self._process_ml_transactions(block.transactions)
        
        # Reset the current list of transactions and add block to chain
        self.current_transactions = []
        self.chain.append(block)
        return block
        
    def add_transaction(self, transaction):
        """Add a transaction to the list of current transactions"""
        if not isinstance(transaction, Transaction):
            raise ValueError("Transaction must be a Transaction object")
            
        if not transaction.validate():
            raise ValueError("Invalid transaction")
            
        self.current_transactions.append(transaction.to_dict())
        return self.last_block.index + 1
        
    def add_flower_data(self, sender, features, flower_type):
        """Add flower data to the blockchain"""
        transaction = Transaction.create_flower_data_transaction(
            sender, features, flower_type
        )
        return self.add_transaction(transaction)
        
    def _process_ml_transactions(self, transactions):
        """Process ML transactions in a newly mined block"""
        for tx in transactions:
            if tx.get('type') == TransactionType.FLOWER_DATA.value:
                # Extract flower features from transaction
                data = tx.get('data', {})
                features = [
                    float(data.get("sepal_length", 0)),
                    float(data.get("sepal_width", 0)),
                    float(data.get("petal_length", 0)),
                    float(data.get("petal_width", 0))
                ]
                flower_type = data.get("flower_type", "")
                
                # Update the ML model with this data point
                self.ml_model.add_data_point(features, flower_type)
                
    def predict_flower_type(self, features):
        """Make prediction using the blockchain's ML model"""
        return self.ml_model.predict(features)
        
    def validate_chain(self):
        """Validate the integrity of the blockchain"""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            
            # Check hash integrity
            if current.previous_hash != previous.hash:
                return False
                
            # Verify block hash
            if not self.pow.validate(current):
                return False
                
        return True
        
    @property
    def last_block(self):
        """Return the last block in the chain"""
        return self.chain[-1]
        
    def serialize_model(self):
        """Serialize the ML model for storage or transmission"""
        return self.ml_model.serialize()
        
    def load_model(self, serialized_model):
        """Load a serialized ML model"""
        self.ml_model = IrisModel.deserialize(serialized_model)
        
    def evaluate_model(self):
        """Evaluate the current ML model performance"""
        return self.ml_model.evaluate_model()