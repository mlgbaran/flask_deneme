
from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from sqlalchemy import create_engine, inspect, table
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, engine, session, LoginManager
from flask_login import login_user, login_required, logout_user, current_user
import pymysql
import mysql.connector
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

pymysql.install_as_MySQLdb()

from flask_sqlalchemy import SQLAlchemy



"""class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")"""

auth = Blueprint('auth', __name__)

"""engine = create_engine('mysql://httpdhbu123_atlmue1qu:barancicek07@localhost/httpdhbu123_atlmue1q',echo=True)
q = engine.execute('SELECT * FROM TABLE2')
bilgi = q.fetchall()

print(bilgi)

Session=sessionmaker(bind=engine)
ss = Session()

Base = declarative_base()"""



@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = session.query(User).filter_by(email=email).first()

        if user:
            if check_password_hash(user.password,password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = session.query(User).filter_by(email=email).first()
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
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1,method="sha256"))

            """if not engine.dialect.has_table(engine.connect(),'Users'):
                db.create_all(engine)"""

            session.add(new_user)
            session.commit()


            flash('Account Created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")

@auth.route('/check-connection', methods=['GET','POST'])
def checkConnection():


    #mydb = mysql.connector.connect(host="localhost",user="httpdhbu123_atlmue1qu",passwd=")w*{M{;02ovh")
    
    #my_cursor = mydb.cursor()
    #q = my_cursor.execute('SHOW DATABASES')
    #bilgi = q.fetchall()




    """if not engine.dialect.has_table(engine.connect(),'Users'):
        Base.metadata.create_all(engine)"""
    
    """form = UploadFileForm()

    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),"website/static/csv_files",secure_filename(file,filename)))
        return "file has been uploaded" """
    #return render_template("check_connection.html", bilgi=bilgi)
    return render_template("check_connection.html", users=bilgi, table=db.Model)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))