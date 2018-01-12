import os
from app import app
from flask import Flask, jsonify, request, json, redirect, render_template, send_from_directory, make_response, current_app
from flask_cors import CORS, cross_origin
from uuid import uuid4
from textwrap import dedent
from .models.blockchain import Blockchain
from .models.user import User
from .models.artist import Artist
from .models.album import Album 
from .models.song import Song


CORS(app, origins=['*', 'https://block-party-client.herokuapp.com'])

node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()

@app.route('/mine', methods=['POST'])
@cross_origin()
def mine():

    data = request.get_json()
    print(data)

    artist_id = data['artist_id']
    user_id = data['user_id']

    print(artist_id)
    print(user_id)

    artist = Artist.query.filter_by(id=int(artist_id)).first()
    listener = User.query.filter_by(id=int(user_id)).first()

    print(artist)
    print(listener)
    print(listener.name + ' is listening to ' + artist.name + '. 25% of this BlockNote attributed to ' + listener.name + ', 50% to ' + artist.name)

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

    response = {'message': f'Transaction will be added to Block {index}' }

    return jsonify(response), 201


@app.route('/chain', methods=['GET'])
def full_chain():

    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }

    return jsonify(response), 200


@app.route('/users/signup', methods=['POST'])
def signup():

    data = request.get_json()
    address = str(uuid4())

    if data['platform'] == True:

        incoming_user = data['platform_user']
        print(incoming_user)

        user_name = incoming_user.get('user_name')
        profile_photo = incoming_user.get('profile_photo')
        email = incoming_user.get('email')
        followers = incoming_user.get('followers')
        platforms = incoming_user.get('platforms')
        account_tier = incoming_user.get('account_tier')
        accessToken = incoming_user.get('accessToken')

        new_user = User(id=None,
                        password=accessToken,
                        date_joined=None,
                        spotify_id=None,
                        name=user_name,
                        followers=followers,
                        email=email,
                        profile_image=profile_photo,
                        platforms=platforms,
                        wallet_address=address
                        )
    else:
        user_name = data['user_name']
        profile_photo = data['profile_photo']
        email = data['email']
        platforms = data['platforms']

        print(user_name)
        print(profile_photo)
        print(email)
        print(platforms)
        print(address)

        new_user = User(id=None,
                        password=None,
                        date_joined=None,
                        spotify_id=None,
                        name=user_name,
                        email=email,
                        followers=None,
                        profile_image=profile_photo,
                        platforms=platforms,
                        wallet_address=address
                        )

    db.session.add(new_user)
    db.session.commit()

    resp_data = {
        'success': True,
        'new_user': {
            'user_name': new_user.name,
            'profile_photo': new_user.profile_image,
            'email': new_user.email,
            'followers': new_user.followers,
            'platforms': new_user.platforms,
            'accessToken': new_user.password
        }
    }

    resp = make_response(jsonify(resp_data), 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp


@app.route('/artists/signup', methods=['POST'])
# @cross_origin()
def artist_signup():

    data = request.get_json()
    print(data)

    artist_name = data['artist_name']
    password = data['password']
    email = data['email']
    address = str(uuid4())

    new_artist = Artist(id=None,
                        password=password,
                        date_joined=None,
                        name=artist_name,
                        email=email,
                        profile_image=None,
                        wallet_address=address
                        )

    db.session.add(new_artist)
    db.session.commit()

    resp_data = {
        'artist': {
            'artist_name': artist_name,
            'email': email,
            'wallet_address': address,
            'id': new_artist.id
        }
    }

    resp = make_response(jsonify(resp_data), 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp


@app.route('/login', methods=['POST'])
def login():
    req = request.get_json()
    data = req['data']

    print(data)

    if data.get('isArtist'):
        artist = Artist.query.filter_by(email_address=data['email']).first()
        print(artist)

        if artist:
            print(artist)
            resp_data = {
                'artist': {
                    'artist_name': artist.name,
                    'email': artist.email_address,
                    'wallet_address': artist.wallet_address,
                    'id': artist.id
                }
            }

            resp = make_response(jsonify(resp_data), 200)
            resp.headers['Access-Control-Allow-Origin'] = '*'

            return resp
    elif data.get('spotify_login'):
        email = data['platform_user']['email']
        print(email)
        user = User.query.filter_by(email=email).first()

        if user:
            resp_data = {
                'user': {
                    'user_name': user.name,
                    'email': user.email,
                    'password': user.password,
                    'wallet_address': user.wallet_address,
                    'id': user.id
                }
            }

            resp = make_response(jsonify(resp_data), 200)
            resp.headers['Access-Control-Allow-Origin'] = '*'

            return resp



@app.route('/artists/<string:artist_id>/onboard', methods=['GET', 'POST'])
@cross_origin()
def artist_onboard(artist_id):
    if request.method == "GET":
        print(artist_id)
        print(int(artist_id))
        new_artist = Artist.query.filter_by(id=int(artist_id)).first()

        if new_artist:
            name = new_artist.name
            wallet_address = new_artist.wallet_address

            resp = {
                'name': name,
                'wallet_address': wallet_address
            }

            return jsonify(resp), 200
        else:
            return 'Error'

    # elif request.method == 'POST':


@app.route('/nodes/register/', methods=['POST'])
@cross_origin()
def register_nodes():

    values = request.get_json()
    nodes = values.get('nodes')

    if nodes is None:
        return 'Error Please supply a valid list of nodes', 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes)
    }

    return jsonify(response), 201


@app.route('/nodes/resolve', methods=['GET'])
def consensus():

    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }
    return jsonify(response), 200


if __name__ == "__main__":
    app.run()
