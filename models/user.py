from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/block_party'

db = SQLAlchemy(app)



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    password = db.Column(db.Text)
    date_joined = db.Column(db.DateTime, default=datetime.now())
    profile_image = db.Column(db.Text, default=None)
    spotify_id = db.Column(db.Integer, default=None)
    platforms = db.Column(db.JSON)
    wallet_address = db.Column(db.Text)


    def __init__(self, id, name, email, password, date_joined, profile_image, spotify_id, platforms, wallet_address):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.date_joined = date_joined
        self.profile_image = profile_image
        self.spotify_id = spotify_id
        self.platforms = platforms
        self.wallet_address = wallet_address
    
    def __repr__(self):
        return '<id {}>'.format(self.id)