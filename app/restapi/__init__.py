from flask import Blueprint
from flask_restful import Api

from app.restapi.customer.resources import (
    CustomersResource, CustomersItemResource)
from app.restapi.user.resources import (
    UserItemResource, UserRegister, UserLogin, UserLogout)

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    # customers
    api.add_resource(CustomersResource, "/customers/")
    api.add_resource(CustomersItemResource, "/customers/<customer_id>")
    # users_auth
    api.add_resource(UserItemResource, "/users/<int:user_id>")
    api.add_resource(UserRegister, "/register")
    api.add_resource(UserLogin, "/login")
    api.add_resource(UserLogout, "/logout")

    app.register_blueprint(bp)
