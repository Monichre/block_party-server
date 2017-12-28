from flask import Flask, jsonify, request, json, redirect, render_template, send_from_directory
from flask_cors import CORS
from uuid import uuid4
from textwrap import dedent
from models.blockchain import Blockchain
from config import apply_config


# Instantiate the server --> will move this out of this file at some point
app = Flask(__name__)

# general config
apply_config(app)

# apply CORS
CORS(app)

# Create a globally unique address or this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()


@app.route('/mine', methods=['POST'])
def mine():

    request_data = request.get_json()    
    required = ['musician_id', 'user_id']

    print(request_data['user_id'] + ' is listening to ' + request_data['musician_id'] + '. 25% of this BlockNote attributed to ' + request_data['user_id'] + ', 50% to ' + request_data['musician_id'])

    if not all(k in request_data for k in required):
        return 'Missing Necessary Data in Request', 400


    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # Receive a reward for finding this proof
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1
    )

    # Forge new block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': 'New Block Forged',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }

    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():

    values = request.get_json()

    # Check that the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new Transaction
    index = blockchain.new_transaction(
        values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201


@app.route('/chain', methods=['GET'])
def full_chain():

    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }

    return jsonify(response), 200

@app.route('/spotify/signup', methods = ['POST'])
def signup():

    data = request.get_json()
    print(data)
    
    client_id = data['client_id']
    client_secret = data['client_secret']
    scopes = data['scopes']
    redirect_uri = data['redirect_URI']

    print(client_id)
    print(client_secret)
    print(scopes)
    print(redirect_uri)
    
    redirect('https://accounts.spotify.com/authorize' + '?response_type=code' + '&client_id=' + client_id + '&scope=' + json.dumps(scopes) + '&redirect_uri=' + redirect_uri)

    return 'success'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

