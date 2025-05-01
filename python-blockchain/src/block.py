class Block:
    def __init__(self, index, previous_hash, timestamp, transactions):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        import hashlib
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.transactions}".encode()
        return hashlib.sha256(block_string).hexdigest()