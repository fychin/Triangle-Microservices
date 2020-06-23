from app import db


class Store(db.Model):
    __tablename__ = 'store'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())
    country = db.Column(db.String())

    def __init__(self, name, address, country):
        self.name = name
        self.address = address
        self.country = country

    def __repr(self):
        return '<Store_id: {}, country: {}'.format(self.id, self.country)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'country': self.country
        }
