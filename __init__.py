from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# from models.blockchain import Blockchain
# from models.user import User
# from models.artist import Artist
# from models.album import Album 
# from models.song import Song

from .models import *
from app import app
from .routes import *
