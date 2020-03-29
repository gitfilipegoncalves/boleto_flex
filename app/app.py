from flask import Flask

from config import BaseConfig
from app import restapi
from app.ext.database import db, migrate
from app.ext.auth import jwt
from app.restapi.customer.models import CustomerModel  # utilizado pelo migrate


def create_app(config_class=BaseConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # ext
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # restapi
    restapi.init_app(app)

    @app.route('/')
    def hello():
        return 'Hello Flask'

    return app
