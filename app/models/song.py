from datetime import datetime
from app import db


class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    # album_id = db.Column(db.Integer, db.ForeignKey('albums.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    photo = db.Column(db.Text, default=None)
    claps = db.Column(db.Integer, default=None)
    shares = db.Column(db.Integer, default=None)
    value = db.Column(db.Integer, default=None)

    def __init__(self, id, name, artist_id, created_at, photo, claps, shares, value):
        self.id = id
        self.name = name
        self.artist_id = artist_id
        # self.album = album
        self.created_at = created_at
        self.photo = photo
        self.claps = claps
        self.shares = shares
        self.value = value

    def __repr__(self):
        return '<Song {}, {}>'.format(self.id, self.name)
