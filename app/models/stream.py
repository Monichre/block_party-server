from datetime import datetime
from app import db


class Stream(db.Model):
    __tablename__ = 'songs'
    __table_args__ = {'extend_existing': True} 

    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    played_at = db.Column(db.DateTime, default=None)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    duration = db.Column(db.Integer, default=None)
    value = db.Column(db.Integer, default=None)

    def __init__(self, id, song_id ,user_id ,artist_id ,created_at ,played_at ,duration ,value):
        self.id = id
        self.song_id = song_id
        self.user_id = user_id
        self.artist_id = artist_id
        self.created_at = created_at
        self.played_at = played_at
        self.duration = duration
        self.value = value

    def __repr__(self):
        return '<Stream {}, {}>'.format(self.id)
