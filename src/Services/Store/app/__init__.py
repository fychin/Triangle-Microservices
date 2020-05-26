from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Init Flask app with config
app = Flask(__name__)
app.config.from_object(Config)

# Configure db
db = SQLAlchemy(app)
migrate = Migrate(app, db)

