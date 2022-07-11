from flask import Flask
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
import pymysql
from os import path
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from sqlalchemy import create_engine, inspect, table

#from website.models import User



pymysql.install_as_MySQLdb()

db = SQLAlchemy()

engine = create_engine('mysql://httpdhbu123_atlmue1qu:barancicek07@localhost/httpdhbu123_atlmue1q',echo=True)

Base = declarative_base()

Session=sessionmaker(bind=engine)
session = Session()

#DB_NAME = "database.db"

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'denemesecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://httpdhbu123_atlmue1qu:barancicek07@localhost/httpdhbu123_atlmue1q'
    db.init_app(app)
    app.config['UPLOAD_FOLDER'] = 'static/csv_files'
    
    
    from .views import views
    from .auth import auth

    

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return session.query(User).get(int(id))



    return app

def create_database(app):


    Base.metadata.create_all(engine, checkfirst=True)

    
    print('Created database!')