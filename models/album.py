from datetime import datetime
from manage import db, app

class Album(db.Model):
    __tablename__ = 'albums'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    artist_id = db.Column(db.Integer, db.ForeignKey(
        'artists.id'), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    photo = db.Column(db.Text, default=None)
    claps = db.Column(db.Integer, default=None)
    shares = db.Column(db.Integer, default=None)
    value = db.Column(db.Integer, default=None)

    def __init__(self, id, name, artist_id, created_at, photo, claps, shares, value):
        self.id = id
        self.name = name
        self.artist_id = artist_id
        self.created_at = created_at
        self.photo = photo
        self.claps = claps
        self.shares = shares
        self.value = value

    def __repr__(self):
        return '<Album {}, {}>'.format(self.id, self.name)
