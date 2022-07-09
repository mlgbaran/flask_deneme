from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from os import path



db = SQLAlchemy()

#DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'denemesecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://httpdhbu123_atlmue1qu:barancicek07@localhost/httpdhbu123_atlmue1q'
    #db.init_app(app)
    app.config['UPLOAD_FOLDER'] = 'static/csv_files'
    from .views import views
    from .auth import auth

    

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #from .models import User, Urun


    #create_database(app)


    return app

 #def create_database(app):
    #if not path.exists('website/' + DB_NAME):
        #db.create_all(app=app)
        #print('Created database!')