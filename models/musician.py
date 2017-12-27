class Musician(db.model):
    __tablename__ = 'musicians'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    date_joined = db.Column(db.DateTime, default=datetime.now())
    profile_image = db.Column(db.Text, default=None)
    spotify_id = db.Column(db.Integer, default=None)


    def __init__(self, id, name, email, password, date_joined, profile_image, spotify_id):
        self.id = id
        self.name = name
        self.date_joined = date_joined
        self.profile_image = profile_image
        self.spotify_id = spotify_id

        
