from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
# manages user states w/r/t login/logout
from flask_login import LoginManager 

# this is the object that will be used for SQL functions (inserting, etc)
db = SQLAlchemy()
DB_NAME = "database.db"



def make_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "hello"
    # configures the app to store the database in the local folder
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # initializes the db
    db.init_app(app)

    # importing blueprints
    from .views import views
    from .auth import auth

    # register blueprints w/url_prefix
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # import the db models from relative folder
    from .models import User
    # create the database passing the app contents as arg
    create_database(app)

    # setup for login manager
    login_manager = LoginManager()
    login_manager.login_view = "auth.sign_in"
    login_manager.init_app(app)
    # load in the user to the webapp
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    # initialize the db if it does not yet exist
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
