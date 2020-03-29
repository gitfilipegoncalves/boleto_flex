from flask_jwt_extended import JWTManager
from flask import jsonify
from blacklist import BLACKLIST


jwt = JWTManager()


@jwt.token_in_blacklist_loader
def verify_blacklist(token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def revoked_token_access():
    return jsonify({'message': 'Seu token não está logado!'}), 401


def init_app(app):
    jwt.init_app(app)
