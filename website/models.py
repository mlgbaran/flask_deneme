
from . import db
from flask_login import UserMixin

"""class Urun(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    urun_kodu = db.Column(db.String(150),unique=True)
    urun_grubu = db.Column(db.String(150))
    model_adi = db.Column(db.String(150))
    fiyat = db.column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))"""


class User(db.Model, UserMixin):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    first_name = db.column(db.String(150))



