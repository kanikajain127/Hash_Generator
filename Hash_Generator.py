#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_str = str(self.index) + str(self.timestamp) + self.data + self.previous_hash
        return hashlib.sha256(data_str.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

if __name__ == "__main__":
    blockchain = Blockchain()

    while True:
        user_data = input("Enter data for the new block (or 'q' to quit): ")
        
        if user_data.lower() == 'q':
            break

        blockchain.add_block(Block(len(blockchain.chain), blockchain.get_latest_block().hash, user_data))

    # Print the blockchain
    for block in blockchain.chain:
        print(f"Block #{block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print()


# In[ ]:




