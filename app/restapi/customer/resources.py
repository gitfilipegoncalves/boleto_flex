from flask_restful import Resource, reqparse
from .models import CustomerModel
from flask_jwt_extended import jwt_required


class CustomersResource(Resource):
    def get(self):
        return {'customers': [customers.json() for customers in
                              CustomerModel.query.all()]}


class CustomersItemResource(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('name', type=str, required=True,
                           help="Campo 'nome' não pode ser deixado em branco")
    atributos.add_argument('email', type=str, required=True,
                           help="Campo 'email' não pode ser deixado em branco")
    atributos.add_argument('phone')
    atributos.add_argument('doc')

    def get(self, customer_id):
        customer = CustomerModel.find_customer(customer_id)
        if customer:
            return customer.json()
        return {'message': 'Cliente não existe!'}

    @jwt_required
    def post(self, customer_id):
        if CustomerModel.find_customer(customer_id):
            return {"message": "Cliente com id '{}' já existe!".format(customer_id)}, 400
        data = CustomersItemResource.atributos.parse_args()
        customer = CustomerModel(customer_id, **data)
        try:
            customer.save_customer()
        except:
            return {'message': 'Erro ao tentar salvar o cliente'}, 500
        return customer.json()
