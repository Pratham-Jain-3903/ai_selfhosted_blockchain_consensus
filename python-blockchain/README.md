# Python Blockchain Implementation

This project is a simple implementation of a blockchain in Python. It includes the core components necessary to create a blockchain, manage transactions, and implement a consensus algorithm.

rSee blogs for reference and inspiration: "https://hackernoon.com/learn-blockchains-by-building-one-117428612f46",
"https://bitsonblocks.net/2015/09/09/gentle-introduction-blockchain-technology/",
"https://ecomunsing.com/build-your-own-blockchain"


## Project Structure

```
python-blockchain
├── src
│   ├── __init__.py
│   ├── blockchain.py
│   ├── block.py
│   ├── transaction.py
│   ├── wallet.py
│   ├── ml_model.py
│   ├── consensus
│   │   ├── __init__.py
│   │   └── proof_of_work.py
│   ├── networking
│   │   ├── __init__.py
│   │   └── node.py
│   └── utils
│       ├── __init__.py
│       └── crypto.py
├── tests
│   ├── __init__.py
│   ├── test_blockchain.py
│   ├── test_block.py
│   └── test_transaction.py
├── requirements.txt
└── README.md
```

## Features

- **Blockchain**: The main class that manages the chain of blocks and handles transactions.
- **Blocks**: Each block contains a list of transactions and a hash of the previous block.
- **Transactions**: Represents a transaction with sender, recipient, and amount.
- **Wallet**: Manages user wallets, including key generation and transaction signing.
- **Consensus Algorithm**: Implements Proof of Work to validate new blocks.
- **Networking**: Allows nodes to communicate and sync the blockchain.
- **Machine Learning**: Integrates an Iris flower classification model that learns from blockchain data.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/python-blockchain.git
   cd python-blockchain
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python -m src.api
   ```

## Usage Examples

### Standard Blockchain Operations

#### Creating a Transaction

Using curl:
```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "sender": "wallet_address_123",
    "recipient": "wallet_address_456",
    "amount": 5
}' http://localhost:5000/transactions/new
```

Using Python requests:
```python
import requests
import json

transaction = {
    "sender": "wallet_address_123",
    "recipient": "wallet_address_456",
    "amount": 5
}

response = requests.post("http://localhost:5000/transactions/new", 
                         json=transaction)
print(response.json())
```

#### Mining a Block

Using curl:
```bash
curl -X GET http://localhost:5000/mine
```

Using Python requests:
```python
import requests
response = requests.get("http://localhost:5000/mine")
print(response.json())
```

#### Viewing the Blockchain

Using curl:
```bash
curl -X GET http://localhost:5000/chain
```

Using Python requests:
```python
import requests
response = requests.get("http://localhost:5000/chain")
print(response.json())
```

### Machine Learning Features

#### Adding Iris Flower Data

Using curl:
```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "sender": "botanist_123",
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "flower_type": "setosa"
}' http://localhost:5000/flower/add
```

Using Python requests:
```python
import requests

flower_data = {
    "sender": "botanist_123",
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "flower_type": "setosa"
}

response = requests.post("http://localhost:5000/flower/add", 
                         json=flower_data)
print(response.json())
```

#### Predicting Flower Type

Using curl:
```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "sepal_length": 6.3,
    "sepal_width": 3.3,
    "petal_length": 6.0,
    "petal_width": 2.5
}' http://localhost:5000/flower/predict
```

Using Python requests:
```python
import requests

features = {
    "sepal_length": 6.3,
    "sepal_width": 3.3,
    "petal_length": 6.0,
    "petal_width": 2.5
}

response = requests.post("http://localhost:5000/flower/predict", 
                        json=features)
print(response.json())
```

#### Getting Model Information

Using curl:
```bash
curl -X GET http://localhost:5000/model/info
```

Using Python requests:
```python
import requests
response = requests.get("http://localhost:5000/model/info")
print(response.json())
```

### Full Training Example

This example shows how to train the model with a batch of Iris data:

```python
import requests
import time

# Sample Iris dataset entries
iris_samples = [
    {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2, "flower_type": "setosa"},
    {"sepal_length": 4.9, "sepal_width": 3.0, "petal_length": 1.4, "petal_width": 0.2, "flower_type": "setosa"},
    {"sepal_length": 7.0, "sepal_width": 3.2, "petal_length": 4.7, "petal_width": 1.4, "flower_type": "versicolor"},
    {"sepal_length": 6.3, "sepal_width": 3.3, "petal_length": 6.0, "petal_width": 2.5, "flower_type": "virginica"},
]

# Add each sample to the blockchain
for sample in iris_samples:
    # Add sender field
    sample["sender"] = "training_script"
    
    # Send data to blockchain
    response = requests.post("http://localhost:5000/flower/add", json=sample)
    print(f"Added sample: {response.json()}")

# Mine a block to include all transactions
response = requests.get("http://localhost:5000/mine")
print(f"Mined block: {response.json()}")

# Check model info
response = requests.get("http://localhost:5000/model/info")
print(f"Model info: {response.json()}")

# Make a prediction
test_flower = {
    "sepal_length": 5.0,
    "sepal_width": 3.4,
    "petal_length": 1.5,
    "petal_width": 0.2
}

response = requests.post("http://localhost:5000/flower/predict", json=test_flower)
print(f"Prediction: {response.json()}")
```

## Testing

To run the tests, execute:
```
python -m pytest
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.