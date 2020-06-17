import os


class Config(object):
    TESTING = False
    SECRET_KEY = 'triangle-store-app'

    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///store-test.db'


app_config = {
    'development': Config,
    'testing': TestingConfig
}
