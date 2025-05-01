class ProofOfWork:
    def __init__(self, difficulty=2):
        self.difficulty = difficulty
        self.prefix_str = '0' * difficulty

    def mine(self, block):
        nonce = 0
        while True:
            block.nonce = nonce
            block_hash = block.calculate_hash()
            if block_hash.startswith(self.prefix_str):
                print(f"Block mined: {block_hash} with nonce: {nonce}")
                return block_hash
            nonce += 1

    def validate(self, block):
        return block.calculate_hash().startswith(self.prefix_str)