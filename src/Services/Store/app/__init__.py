from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name=Config):
    # Init Flask app with config
    app = Flask(__name__)
    app.config.from_object(config_name)

    # Configure db
    db.init_app(app)
    migrate.init_app(app, db)

    return app


from app import models
