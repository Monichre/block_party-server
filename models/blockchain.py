import hashlib
import json
from textwrap import dedent
from time import time
from urllib.parse import urlparse



class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        # Creates a new Block and adds it to the chain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        # Reset the current list of transactions
        self.current_transactions = []
        self.chain.append(block)

        return block
    
    
    def new_transaction(self, sender, recipient, amount):
        # Adds a new transaction to the list of transactions
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1

    def proof_of_work(self, last_proof):

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        
        return proof


    def register_node(self, address):

        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)


    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4] == '0000'

    @staticmethod
    def hash(block):
        # Hashes a block, creates a SHA-256 hash of a block
        block_string = json.dumps(block, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()
    
    @property
    def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1]