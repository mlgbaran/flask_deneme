
from flask import Blueprint, render_template, request, flash, redirect, url_for
from sqlalchemy import create_engine
#from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
#from . import db
from flask_login import login_user, login_required, logout_user, current_user
import pymysql
import mysql.connector

pymysql.install_as_MySQLdb()

from flask_sqlalchemy import SQLAlchemy


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        #user = User.query.filter_by(email=email).first()

        #if user:
            #if check_password_hash(user.password,password):
                #flash('Logged in successfully!', category='success')
                #login_user(user, remember=True)
                #return redirect(url_for('views.home'))
            #else:
                #flash('Incorrect password, try again.', category='error')
         #else:
            #flash('Email does not exist.', category='error')

    return render_template("login.html", boolean=True)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            #new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1,method="sha256"))
            #db.session.add(new_user)
            #db.session.commit()

            flash('Account Created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")

@auth.route('/check-connection', methods=['GET'])
def checkConnection():


    #mydb = mysql.connector.connect(host="localhost",user="httpdhbu123_atlmue1qu",passwd=")w*{M{;02ovh")
    
    #my_cursor = mydb.cursor()
    #q = my_cursor.execute('SHOW DATABASES')
    #bilgi = q.fetchall()
    engine = create_engine('mysql://httpdhbu123_atlmue1qu:barancicek07@localhost/httpdhbu123_atlmue1q',echo=True)
    q = engine.execute('SHOW TABLES')
    bilgi = q.fetchall()

    return render_template("check_connection.html", bilgi=bilgi)
