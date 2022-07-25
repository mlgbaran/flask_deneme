from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/upload-csv', methods = ['GET','POST'])
@login_required
def upload_csv():
    return render_template("upload_csv.html",user=current_user)