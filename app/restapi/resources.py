from flask_restful import Resource

customers = [
    {
        'name': 'Filipe',
        'email': 'filipe@email.com',
        'phone': '991264747',
        'doc': '04082684955',
    },
    {
        'name': 'Luis',
        'email': 'luis@email.com',
        'phone': '233456788',
        'doc': '04061804566',
    },
    {
        'name': 'Livia',
        'email': 'livia@email.com',
        'phone': '899876353',
        'doc': '04084971833',
    }
]


class CustomersResource(Resource):
    def get(self):
        return {'customers': customers}


class CustomersItemResource(Resource):
    pass
