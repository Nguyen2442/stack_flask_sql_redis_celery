from flask_sqlalchemy import SQLAlchemy
from .db import *
from flask_migrate import Migrate
from app.config import settings

db = SQLAlchemy()


def setup_db(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = settings.SECRET_KEY
    
    db.app = app
    db.init_app(app)

    migrate = Migrate(app, db)

    return db
