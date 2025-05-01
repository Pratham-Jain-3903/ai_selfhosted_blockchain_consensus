import time
import json
from enum import Enum

class TransactionType(Enum):
    TRANSFER = "transfer"
    FLOWER_DATA = "flower_data"

class Transaction:
    def __init__(self, sender, recipient, amount=0, transaction_type=TransactionType.TRANSFER, data=None):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()
        self.transaction_type = transaction_type
        self.data = data or {}
        
    def to_dict(self):
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': self.timestamp,
            'type': self.transaction_type.value,
            'data': self.data
        }
        
    def validate(self):
        """Validate the transaction based on its type"""
        if self.transaction_type == TransactionType.TRANSFER:
            return self._validate_transfer()
        elif self.transaction_type == TransactionType.FLOWER_DATA:
            return self._validate_flower_data()
        return False
        
    def _validate_transfer(self):
        """Validate a cryptocurrency transfer transaction"""
        if self.amount <= 0:
            return False
        if not self.sender or not self.recipient:
            return False
        return True
        
    def _validate_flower_data(self):
        """Validate an Iris flower data transaction"""
        if not self.sender:
            return False
            
        # Check that data contains valid flower measurements
        required_fields = ["sepal_length", "sepal_width", "petal_length", "petal_width", "flower_type"]
        if not all(field in self.data for field in required_fields):
            return False
            
        # Validate data types
        try:
            float(self.data["sepal_length"])
            float(self.data["sepal_width"])
            float(self.data["petal_length"])
            float(self.data["petal_width"])
        except (ValueError, TypeError):
            return False
            
        # Check flower type is valid
        valid_types = ["setosa", "versicolor", "virginica"]
        if self.data["flower_type"] not in valid_types:
            return False
            
        return True
        
    @staticmethod
    def create_flower_data_transaction(sender, features, flower_type):
        """Factory method for creating flower data transactions"""
        data = {
            "sepal_length": features[0],
            "sepal_width": features[1],
            "petal_length": features[2],
            "petal_width": features[3],
            "flower_type": flower_type
        }
        return Transaction(
            sender=sender,
            recipient="MODEL",  # Special recipient for model updates
            amount=0,  # No cryptocurrency transfer
            transaction_type=TransactionType.FLOWER_DATA,
            data=data
        )