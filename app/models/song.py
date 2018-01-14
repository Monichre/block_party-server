from datetime import datetime
from app import db


class Song(db.Model):
    __tablename__ = 'songs'
    __table_args__ = {'extend_existing': True} 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    # album_id = db.Column(db.Integer, db.ForeignKey('albums.id'))
    spotify_id = db.Column(db.Text, default=None)
    created_at = db.Column(db.DateTime, default=datetime.now())
    photo = db.Column(db.Text, default=None)
    claps = db.Column(db.Integer, default=None)
    shares = db.Column(db.Integer, default=None)
    popularity = db.Column(db.Integer, default=None)
    value = db.Column(db.Integer, default=None)

    def __init__(self, id, name, artist_id, created_at, photo, claps, shares, value, spotify_id, popularity):
        self.id = id
        self.name = name
        self.popularity = popularity
        self.artist_id = artist_id
        # self.album = album
        self.spotify_id = spotify_id
        self.created_at = created_at
        self.photo = photo
        self.claps = claps
        self.shares = shares
        self.value = value

    def __repr__(self):
        return '<Song {}, {}>'.format(self.id, self.name)
