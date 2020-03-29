from app.ext.database import db


class CustomerModel(db.Model):

    __tablename__ = 'customers'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    phone = db.Column(db.String(9))
    doc = db.Column(db.String(11))
