# Python Blockchain Implementation with ML Integration

This project is a simple implementation of a blockchain in Python with integrated machine learning capabilities. It includes the core components necessary to create a blockchain, manage transactions, implement a consensus algorithm, and train a machine learning model on blockchain data.

## Research Inspiration

This project was inspired by several research papers and blog posts:

- **"Decentralized & Collaborative AI on Blockchain"** (Harris and Waggoner, 2019 IEEE International Conference on Blockchain) - This research from Microsoft explores frameworks for participants to collaboratively build datasets and use smart contracts to host continuously updated ML models on a blockchain.

- **"Learn Blockchains by Building One"** - https://hackernoon.com/learn-blockchains-by-building-one-117428612f46

- **"Gentle Introduction to Blockchain Technology"** - https://bitsonblocks.net/2015/09/09/gentle-introduction-blockchain-technology/

- **"Build Your Own Blockchain"** - https://ecomunsing.com/build-your-own-blockchain

## Literature Review

Recent research has highlighted several innovative approaches at the intersection of blockchain technology and machine learning, revealing important research gaps that this project aims to address:

### Recent Developments in Blockchain-based ML

- **"Opp/ai: Optimistic Privacy-Preserving AI on Blockchain"** (So et al., 2024) - This groundbreaking work introduces a hybrid framework combining Zero-Knowledge Machine Learning (zkML) for privacy with Optimistic Machine Learning (opML) for efficiency. The researchers demonstrate how this approach balances the critical concerns of privacy protection and computational efficiency in blockchain environments.

- **"OpML: Optimistic Machine Learning on Blockchain"** (Conway et al., 2024) - This paper presents opML as an innovative approach enabling blockchain systems to conduct AI model inference through an interactive fraud proof protocol. Unlike zkML approaches, opML offers significantly improved cost efficiency while maintaining verification capabilities, even allowing execution of large language models (7B-LLaMA) on standard PCs without GPUs.

- **"A New Consensus Mechanism for Blockchained Federated Learning Systems Using Optimistic Rollups"** (Gonçalves et al., 2024) - This research explores using optimistic rollups to enhance security in federated learning frameworks on blockchain. The authors highlight how decentralized approaches can mitigate corruption risks in the training phase.

- **"A Quality-of-Service Compliance System using Federated Learning and Optimistic Rollups"** (Gonçalves et al., 2023) - This work examines privacy preservation in edge computing, using federated learning to keep sensitive data on source machines while leveraging blockchain for security and incentive mechanisms.

### Research Gap

While recent research has made significant advances in blockchain-based ML systems focusing on complex models and optimistic approaches, there remains a notable gap in accessible implementations that demonstrate the fundamental principles of blockchain-ML integration. Most existing solutions require specialized knowledge in both domains and substantial computational resources. 

Our project addresses this gap by providing:

1. A lightweight implementation that clearly demonstrates the core concepts
2. A simpler model (KNN classifier) appropriate for educational purposes and blockchain storage constraints
3. A practical example of incremental learning on blockchain without requiring advanced cryptographic knowledge
4. An accessible entry point for developers interested in blockchain-ML integration

While advanced approaches like zkML and opML represent the cutting edge of the field, our implementation serves as a foundation for understanding the fundamental principles that underpin these more sophisticated systems. This project aims to bridge the gap between theoretical research and practical implementation, making blockchain-ML integration more accessible to a wider audience.

## Project Structure

```
python-blockchain 
├── src 
│  ├── __init__.py 
|  ├── blockchain.py 
|  ├── block.py 
|  ├── transaction.py 
|  ├── wallet.py 
|  ├── ml_model.py 
|  │ 
|  ├── consensus 
|  │ │ ├── __init__.py 
|  │ │ └── proof_of_work.py 
|  ├── networking 
|  │ │ ├── __init__.py 
|  │ │ └── node.py 
|  |── utils 
|  │ ├── __init__.py 
|  │ └── crypto.py 
|
├── tests 
│ ├── __init__.py 
│ ├── test_blockchain.py 
│ ├── test_block.py 
│ └── test_transaction.py 
|
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
  - Pre-trained with scikit-learn Iris dataset
  - Supports incremental learning as new data points are added via blockchain
  - KNN classifier that improves with each transaction

## Pros and Cons of Blockchain-based ML

### Pros
1. **Decentralized Data Collection**: Enables collaborative dataset building without a central authority
2. **Immutable Model History**: Every update to the model is traceable and cannot be modified
3. **Transparency**: Model training process is publicly verifiable
4. **Incentivization**: Framework allows for rewarding data contributors
5. **Free Public Access**: Anyone can use the model for inference without cost
6. **Collaborative Training**: Model improves from contributions of many participants

### Cons
1. **Storage Limitations**: As noted in Microsoft's research, blockchain storage is expensive, making complex models like deep neural networks impractical
2. **Computational Cost**: On-chain computations (like model training) can be expensive
3. **Model Size Constraints**: Best suited for small models with efficient updates (like our KNN classifier)
4. **Data Type Limitations**: Works best with small inputs that can be compressed easily (text rather than images)
5. **Update Frequency**: Each model update requires mining a block, which can be time-consuming
6. **Scalability Issues**: As the blockchain grows, sync times and storage requirements increase

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

##Postman Collection

For API testing, a Postman collection is available at: Python Blockchain API Collection link - https://www.postman.com/luminouschatbotdevteam/workspace/cs21b1021-blockchain-consensus-testing/collection/41342955-0494f37a-cc20-4753-978d-6ee6d64a4209?action=share&creator=41342955

Implementation Details
Our KNN-based ML model is initialized with scikit-learn's Iris dataset and supports incremental learning as new data points are added through the blockchain. This follows the approach suggested in Microsoft's research paper, where models capable of efficiently updating with one sample are ideal for blockchain integration to lower transaction costs.

As described in the Microsoft Research paper:
 ```
 "We first propose to leverage the work in the Incremental Learning space by using models capable of efficiently updating with one sample. This should lower the transaction costs ('gas') to update a model hosted in an Ethereum smart contract because each data contribution will be small."
 ```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.