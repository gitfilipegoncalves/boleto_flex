from flask_restful import Resource, reqparse
from .models import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST


atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True,
                       help="O campo 'login' não pode ficar em branco")
atributos.add_argument('password', type=str, required=True,
                       help="O campo 'login' não pode ficar em branco")


class UserItemResource(Resource):
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'Usuário não existe!'}, 404

    @jwt_required
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            user.delete_user()
            return {'message': 'Usuario deletado'}
        return {'message': 'Usuário não encontrado'}, 404


class UserRegister(Resource):
    def post(self):
        data = atributos.parse_args()

        if UserModel.find_by_login(data['login']):
            return {"message": "Usuário '{}' já existe!".format(data['login'])}

        user = UserModel(**data)
        user.save_user()
        return {'message': 'Usuário criado com sucesso!'}, 201


class UserLogin(Resource):
    @classmethod
    def post(cls):
        data = atributos.parse_args()

        user = UserModel.find_by_login(data['login'])

        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity=user.user_id)
            return {'access_token': access_token}, 200
        return {'message': 'Usuário ou senha incorreto!'}, 401


class UserLogout(Resource):
    @jwt_required
    def post(self):
        jwt_id = get_raw_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return {'message': 'Deslogado com sucesso!'}, 200
