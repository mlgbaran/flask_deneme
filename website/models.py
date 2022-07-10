
from . import Base
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String

"""class Urun(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    urun_kodu = db.Column(db.String(150),unique=True)
    urun_grubu = db.Column(db.String(150))
    model_adi = db.Column(db.String(150))
    fiyat = db.column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))"""


class User(Base, UserMixin):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    email = Column(String(150),unique=True)
    password = Column(String(150))
    first_name = Column(String(150))



