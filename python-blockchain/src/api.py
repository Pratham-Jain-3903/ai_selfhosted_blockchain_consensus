from flask import Flask, jsonify, request
import uuid
from .blockchain import Blockchain
from .transaction import Transaction, TransactionType

# Initialize our Flask app
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid.uuid4()).replace('-', '')

# Initialize the blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    """Mine a new block with the current transactions"""
    # Mine a new block
    block = blockchain.add_block(blockchain.last_block)
    
    response = {
        'message': 'New block forged',
        'index': block.index,
        'transactions': block.transactions,
        'hash': block.hash,
        'previous_hash': block.previous_hash,
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """Add a new transaction to the pool"""
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    
    if not all(k in values for k in required):
        return 'Missing values', 400
        
    transaction = Transaction(
        sender=values['sender'],
        recipient=values['recipient'],
        amount=values['amount']
    )
    
    index = blockchain.add_transaction(transaction)
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/flower/add', methods=['POST'])
def add_flower_data():
    """Add flower data to the blockchain"""
    values = request.get_json()
    required = ['sender', 'sepal_length', 'sepal_width', 
                'petal_length', 'petal_width', 'flower_type']
                
    if not all(k in values for k in required):
        return 'Missing values', 400
        
    features = [
        float(values['sepal_length']),
        float(values['sepal_width']),
        float(values['petal_length']),
        float(values['petal_width'])
    ]
    
    try:
        block_index = blockchain.add_flower_data(
            values['sender'], 
            features, 
            values['flower_type']
        )
        response = {'message': f'Flower data will be added to Block {block_index}'}
        return jsonify(response), 201
    except ValueError as e:
        return str(e), 400

@app.route('/flower/predict', methods=['POST'])
def predict_flower():
    """Predict flower type based on features"""
    values = request.get_json()
    required = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    
    if not all(k in values for k in required):
        return 'Missing values', 400
        
    features = [
        float(values['sepal_length']),
        float(values['sepal_width']),
        float(values['petal_length']),
        float(values['petal_width'])
    ]
    
    prediction = blockchain.predict_flower_type(features)
    return jsonify(prediction), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    """Return the full blockchain"""
    response = {
        'chain': [block.__dict__ for block in blockchain.chain],
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/model/info', methods=['GET'])
def model_info():
    """Get information about the ML model"""
    response = {
        'is_trained': blockchain.ml_model.is_trained,
        'data_points': blockchain.ml_model.data_count,
        'classes': blockchain.ml_model.classes
    }
    return jsonify(response), 200

@app.route('/model/evaluate', methods=['GET'])
def evaluate_model():
    """Evaluate the current model accuracy using test data"""
    evaluation_results = blockchain.ml_model.evaluate_model()
    return jsonify(evaluation_results), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)