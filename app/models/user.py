from datetime import datetime
from app import db
from .stream import Stream

# user_stream_table = db.Table('user_streams', db.Model.metadata,
#                                       db.Column('id', db.Integer, primary_key=True),
#                                       db.Column('stream_id', db.Integer, db.ForeignKey('stream.id')),
#                                       db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
# )


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True} 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    password = db.Column(db.Text)
    date_joined = db.Column(db.DateTime, default=datetime.now())
    profile_image = db.Column(db.Text, default=None)
    spotify_id = db.Column(db.Integer, default=None)
    followers = db.Column(db.Integer, default=None)
    platforms = db.Column(db.JSON)
    wallet_address = db.Column(db.Text)
    streams = db.relationship('Stream', secondary='streams', backref='stream')


    def __init__(self, id, name, email, password, date_joined, profile_image, spotify_id, platforms, wallet_address, followers):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.date_joined = date_joined
        self.profile_image = profile_image
        self.spotify_id = spotify_id
        self.platforms = platforms
        self.followers = followers
        self.wallet_address = wallet_address
    
    def __repr__(self):
        return '<User {}, {}>'.format(self.id, self.name)
