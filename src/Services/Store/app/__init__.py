from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_type):
    # Init Flask app with config
    app = Flask(__name__)
    app.config.from_object(app_config[config_type])

    # Configure db
    db.init_app(app)
    migrate.init_app(app, db)

    return app


from app import models
