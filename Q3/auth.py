# paste teachers init code into auth, from there add other function
from flask import Flask
from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from flask_login import LoginManager 
from models import User, fitwellUser

def create_app():
    # create cookies
    app = Flask(__name__)

    app.config['SECRET_KEY'] ='mySecretKey'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'

    login_manager = LoginManager()
    login_manager.login_view ='login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return fitwellUser.get_user_byId(email=user_id)
    return app

# get information function from app.py login route, send it to models.py