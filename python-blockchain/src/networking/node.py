class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.peers = set()
        self.blockchain = []

    def connect_to_peer(self, peer_node):
        self.peers.add(peer_node)

    def broadcast_transaction(self, transaction):
        for peer in self.peers:
            peer.receive_transaction(transaction)

    def sync_blockchain(self, other_node):
        if len(other_node.blockchain) > len(self.blockchain):
            self.blockchain = other_node.blockchain

    def receive_transaction(self, transaction):
        # Logic to handle received transaction
        pass

    def add_block(self, block):
        self.blockchain.append(block)