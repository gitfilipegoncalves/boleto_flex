class BaseConfig:
    SECRET_KEY = 'boletoflex'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bf.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

#config[config_name].init_app(app)