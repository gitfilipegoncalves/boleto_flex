from config import BaseConfig
from flask import Flask
from app.ext.database import db
from app import restapi


def create_app(config_class=BaseConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # ext
    db.init_app(app)

    # restapi
    restapi.init_app(app)

    @app.route('/')
    def hello():
        return 'Hello Flask'

    return app
