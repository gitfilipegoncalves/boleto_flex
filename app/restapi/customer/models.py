from app.ext.database import db


class CustomerModel(db.Model):

    __tablename__ = 'customers'

    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    phone = db.Column(db.String(9))
    doc = db.Column(db.String(11))

    def __init__(self, customer_id, name, email, phone, doc):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.doc = doc

    def json(self):
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'doc': self.doc
        }

    @classmethod
    def find_customer(cls, customer_id):
        customer = cls.query.filter_by(customer_id=customer_id).first()
        if customer:
            return customer
        return None

    def save_customer(self):
        db.session.add(self)
        db.session.commit()
