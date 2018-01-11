from datetime import datetime
from app import db

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    date_joined = db.Column(db.DateTime, default=datetime.now())
    profile_image = db.Column(db.Text, default=None)
    email_address = db.Column(db.Text)
    # spotify_id = db.Column(db.Integer, default=None)
    wallet_address = db.Column(db.Text)


    def __init__(self, id, name, email, password, date_joined, profile_image, wallet_address):
        self.id = id
        self.name = name
        self.date_joined = date_joined
        self.profile_image = profile_image
        self.wallet_address = wallet_address
        self.email_address = email