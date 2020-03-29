class BaseConfig:
    SECRET_KEY = 'boletoflex'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bf.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'super-secret'
    JWT_BLACKLIST_ENABLED = True

    @staticmethod
    def init_app(app):
        pass
